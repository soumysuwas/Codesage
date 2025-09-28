from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
import os
from pathlib import Path

from .config import Config
from .routes import interviews, analysis
from .services.websocket_manager import WebSocketManager

app = FastAPI(
    title="CodeSage AI Technical Interviewer",
    description="AI-powered technical interviewer with real-time code analysis and voice interaction",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# WebSocket manager
websocket_manager = WebSocketManager()

# Include routes
app.include_router(interviews.router, prefix="/api/interviews", tags=["interviews"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])

@app.get("/")
async def root():
    return {
        "message": "CodeSage AI Technical Interviewer API", 
        "status": "running",
        "version": "1.0.0",
        "gemini_configured": bool(Config.GEMINI_API_KEY)
    }

@app.get("/health")
async def health_check():
    return {
        "status": "OK",
        "service": "CodeSage AI Interviewer",
        "version": "1.0.0",
        "gemini_configured": bool(Config.GEMINI_API_KEY),
        "features": {
            "real_time_analysis": True,
            "voice_interaction": True,
            "code_execution": True,
            "ai_interviewer": bool(Config.GEMINI_API_KEY)
        }
    }

@app.websocket("/ws/{interview_id}")
async def websocket_endpoint(websocket: WebSocket, interview_id: str):
    await websocket_manager.connect(websocket, interview_id)
    try:
        while True:
            data = await websocket.receive_json()
            await websocket_manager.handle_message(websocket, interview_id, data)
    except WebSocketDisconnect:
        websocket_manager.disconnect(websocket, interview_id)

if __name__ == "__main__":
    Config.validate()
    uvicorn.run(
        "app.main:app",
        host=Config.HOST,
        port=Config.PORT,
        reload=Config.DEBUG
    )
