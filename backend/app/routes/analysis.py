from fastapi import APIRouter
from typing import Dict, Any
from ..services.code_analysis import CodeAnalysisService

router = APIRouter()
analysis_service = CodeAnalysisService()

@router.post("/analyze")
async def analyze_code(request: Dict[str, Any]):
    """Analyze code directly"""
    code = request.get("code", "")
    language = request.get("language", "python")
    
    analysis = await analysis_service.analyze_code(code, language)
    
    return {"success": True, "analysis": analysis}
