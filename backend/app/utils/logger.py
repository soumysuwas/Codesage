import logging
import sys
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('codesage.log')
    ]
)

logger = logging.getLogger('codesage-ai-interviewer')

def log_interview_event(event_type: str, interview_id: str, details: dict = None):
    """Log interview events"""
    logger.info(f"Interview Event: {event_type} - Interview: {interview_id} - Details: {details}")

def log_code_analysis(interview_id: str, analysis_result: dict):
    """Log code analysis results"""
    logger.info(f"Code Analysis - Interview: {interview_id} - Score: {analysis_result.get('overall_score', 0)}")

def log_ai_interaction(interview_id: str, interaction_type: str, response_length: int):
    """Log AI interactions"""
    logger.info(f"AI Interaction - Interview: {interview_id} - Type: {interaction_type} - Response Length: {response_length}")

def log_error(error: Exception, context: str = ""):
    """Log errors"""
    logger.error(f"Error in {context}: {str(error)}", exc_info=True)
