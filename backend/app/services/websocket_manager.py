from fastapi import WebSocket
from typing import Dict, List
import json
from datetime import datetime
from .gemini_service import GeminiInterviewer
from .code_analysis import CodeAnalysisService

class WebSocketManager:
    def __init__(self):
        self.active_connections: Dict[str, List[WebSocket]] = {}
        self.gemini_service = GeminiInterviewer()
        self.analysis_service = CodeAnalysisService()
        self.interview_data = {}
    
    async def connect(self, websocket: WebSocket, interview_id: str):
        await websocket.accept()
        if interview_id not in self.active_connections:
            self.active_connections[interview_id] = []
        self.active_connections[interview_id].append(websocket)
        
        # Initialize interview data
        if interview_id not in self.interview_data:
            self.interview_data[interview_id] = {
                "conversation_history": [],
                "code_submissions": [],
                "hints_used": [],
                "performance_metrics": []
            }
    
    def disconnect(self, websocket: WebSocket, interview_id: str):
        if interview_id in self.active_connections:
            self.active_connections[interview_id].remove(websocket)
    
    async def handle_message(self, websocket: WebSocket, interview_id: str, data: dict):
        message_type = data.get("type")
        
        if message_type == "analyze_code":
            await self._handle_code_analysis(websocket, interview_id, data)
        elif message_type == "send_message":
            await self._handle_chat_message(websocket, interview_id, data)
        elif message_type == "request_hint":
            await self._handle_hint_request(websocket, interview_id, data)
        elif message_type == "request_follow_up":
            await self._handle_follow_up_request(websocket, interview_id, data)
        elif message_type == "generate_report":
            await self._handle_report_generation(websocket, interview_id, data)
    
    async def _handle_code_analysis(self, websocket: WebSocket, interview_id: str, data: dict):
        code = data.get("code", "")
        language = data.get("language", "python")
        problem_description = data.get("problem_description", "")
        
        # Analyze code
        analysis = await self.analysis_service.analyze_code(code, language)
        
        # Store code submission
        self.interview_data[interview_id]["code_submissions"].append({
            "code": code,
            "language": language,
            "analysis": analysis,
            "timestamp": datetime.now().isoformat()
        })
        
        # Generate AI response
        conversation_context = self.interview_data[interview_id]["conversation_history"]
        ai_response = await self.gemini_service.generate_adaptive_response(
            code=code,
            analysis=analysis,
            conversation_context=conversation_context,
            problem_description=problem_description,
            interview_id=interview_id
        )
        
        # Store conversation
        self.interview_data[interview_id]["conversation_history"].append({
            "role": "user",
            "content": f"Code submission: {code[:100]}...",
            "timestamp": datetime.now().isoformat()
        })
        self.interview_data[interview_id]["conversation_history"].append({
            "role": "assistant",
            "content": ai_response,
            "timestamp": datetime.now().isoformat()
        })
        
        # Send response
        await websocket.send_json({
            "type": "code_analysis",
            "analysis": analysis,
            "ai_response": ai_response
        })
    
    async def _handle_chat_message(self, websocket: WebSocket, interview_id: str, data: dict):
        message = data.get("message", "")
        
        # Store user message
        self.interview_data[interview_id]["conversation_history"].append({
            "role": "user",
            "content": message,
            "timestamp": datetime.now().isoformat()
        })
        
        # Generate AI response
        conversation_context = self.interview_data[interview_id]["conversation_history"]
        ai_response = await self.gemini_service.generate_adaptive_response(
            code="",
            analysis={},
            conversation_context=conversation_context,
            problem_description="",
            interview_id=interview_id
        )
        
        # Store AI response
        self.interview_data[interview_id]["conversation_history"].append({
            "role": "assistant",
            "content": ai_response,
            "timestamp": datetime.now().isoformat()
        })
        
        # Send response
        await websocket.send_json({
            "type": "chat_message",
            "ai_response": ai_response
        })
    
    async def _handle_hint_request(self, websocket: WebSocket, interview_id: str, data: dict):
        code = data.get("code", "")
        problem_description = data.get("problem_description", "")
        hint_level = data.get("hint_level", 1)
        
        # Generate hint
        hint = await self.gemini_service.generate_hint(code, problem_description, hint_level, interview_id)
        
        # Store hint usage
        self.interview_data[interview_id]["hints_used"].append({
            "hint_level": hint_level,
            "hint": hint,
            "timestamp": datetime.now().isoformat()
        })
        
        # Send response
        await websocket.send_json({
            "type": "hint_response",
            "hint": hint,
            "hint_level": hint_level
        })
    
    async def _handle_follow_up_request(self, websocket: WebSocket, interview_id: str, data: dict):
        code = data.get("code", "")
        analysis = data.get("analysis", {})
        problem_description = data.get("problem_description", "")
        
        # Generate follow-up question
        question = await self.gemini_service.generate_follow_up_question(
            code, analysis, problem_description, interview_id
        )
        
        # Send response
        await websocket.send_json({
            "type": "follow_up_question",
            "question": question
        })
    
    async def _handle_report_generation(self, websocket: WebSocket, interview_id: str, data: dict):
        # Generate performance report
        report = await self.gemini_service.generate_performance_report(
            self.interview_data[interview_id], interview_id
        )
        
        # Send response
        await websocket.send_json({
            "type": "performance_report",
            "report": report
        })
    
    def get_interview_data(self, interview_id: str) -> dict:
        """Get interview data for reporting"""
        return self.interview_data.get(interview_id, {})
