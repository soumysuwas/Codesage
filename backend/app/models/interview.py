from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class InterviewStatus(str, Enum):
    CREATED = "created"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class DifficultyLevel(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class Question(BaseModel):
    id: str
    title: str
    description: str
    difficulty: DifficultyLevel
    category: str
    test_cases: List[Dict[str, Any]]
    constraints: str
    hints: List[str]
    expected_complexity: Optional[str] = None

class CodeSubmission(BaseModel):
    code: str
    language: str
    timestamp: datetime
    analysis: Dict[str, Any]
    execution_result: Dict[str, Any]

class ConversationRecord(BaseModel):
    role: str  # "user" or "assistant"
    content: str
    timestamp: datetime
    message_type: str = "text"  # "text", "code", "hint", "analysis"

class HintRecord(BaseModel):
    hint_level: int
    hint: str
    timestamp: datetime
    question_id: str

class PerformanceMetrics(BaseModel):
    overall_score: int
    syntax_score: int
    runtime_score: int
    quality_score: int
    complexity_score: int
    execution_time: float
    hints_used: int
    code_submissions: int

class Interview(BaseModel):
    id: str
    candidate_name: str
    difficulty: DifficultyLevel
    category: str
    questions: List[Question]
    status: InterviewStatus
    created_at: datetime
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    current_question: int = 0
    conversation_history: List[ConversationRecord] = []
    code_submissions: List[CodeSubmission] = []
    hints_used: List[HintRecord] = []
    performance_metrics: Optional[PerformanceMetrics] = None

class CreateInterviewRequest(BaseModel):
    candidate_name: str
    difficulty: DifficultyLevel
    category: str = "all"

class StartInterviewRequest(BaseModel):
    interview_id: str

class SubmitCodeRequest(BaseModel):
    code: str
    language: str
    question_id: str

class SendMessageRequest(BaseModel):
    message: str
    message_type: str = "text"

class RequestHintRequest(BaseModel):
    question_id: str
    hint_level: int = 1
    current_code: str = ""
