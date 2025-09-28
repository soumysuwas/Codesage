import os
from typing import List
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    # Server Configuration
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    
    # CORS Configuration
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "http://localhost:3000").split(",")
    
    # Gemini API Configuration
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        print("⚠️  WARNING: GEMINI_API_KEY not set. AI features will be limited.")
        GEMINI_API_KEY = None
    
    # Security
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-this")
    
    # Code Execution
    CODE_TIMEOUT = int(os.getenv("CODE_TIMEOUT", 5))
    MAX_MEMORY_MB = int(os.getenv("MAX_MEMORY_MB", 128))
    
    # Interview Configuration
    MAX_QUESTIONS = int(os.getenv("MAX_QUESTIONS", 5))
    INTERVIEW_DURATION_MINUTES = int(os.getenv("INTERVIEW_DURATION_MINUTES", 60))
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        if not cls.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is required for AI functionality")
        
        print(f"🚀 Server starting on {cls.HOST}:{cls.PORT}")
        print(f"🌐 CORS origins: {cls.CORS_ORIGINS}")
        print(f"🤖 AI Service: Gemini API configured")
        print(f"⚡ Code timeout: {cls.CODE_TIMEOUT}s")
        print(f"💾 Max memory: {cls.MAX_MEMORY_MB}MB")
