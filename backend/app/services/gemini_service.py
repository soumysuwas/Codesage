import google.generativeai as genai
from typing import Dict, Any, List
import json
import asyncio
from ..config import Config

class GeminiInterviewer:
    def __init__(self):
        if Config.GEMINI_API_KEY:
            genai.configure(api_key=Config.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-2.5-pro')
        else:
            self.model = None
        self.conversation_history = {}
    
    async def generate_adaptive_response(
        self, 
        code: str, 
        analysis: Dict[str, Any], 
        conversation_context: List[Dict],
        problem_description: str = "",
        interview_id: str = ""
    ) -> str:
        """Generate adaptive AI response using Gemini"""
        if not self.model:
            return self._get_fallback_response(analysis)
            
        try:
            prompt = self._build_interview_prompt(code, analysis, conversation_context, problem_description)
            
            # Use asyncio to run the synchronous generate_content in a thread
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: self.model.generate_content(prompt)
            )
            
            # Store in conversation history
            if interview_id not in self.conversation_history:
                self.conversation_history[interview_id] = []
            
            self.conversation_history[interview_id].append({
                "role": "assistant",
                "content": response.text
            })
            
            return response.text
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self._get_fallback_response(analysis)
    
    async def generate_hint(self, code: str, problem_description: str, hint_level: int, interview_id: str = "") -> str:
        """Generate progressive hints"""
        if not self.model:
            return self._get_fallback_hint(hint_level)
            
        try:
            hint_prompts = {
                1: f"""Directly provide one subtle, encouraging hint for the following coding problem based on the user's code. Do not explain your process or philosophy.

                Problem: {problem_description}
                Candidate's Code:
                ```
                {code}
                ```
                
                Your Hint:""",
                
                2: f"""Directly provide a more specific hint pointing towards the solution approach for the following problem. Do not explain your process.

                Problem: {problem_description}
                Candidate's Code:
                ```
                {code}
                ```
                
                Your Hint:""",
                
                3: f"""Directly provide a specific guidance on the data structure or algorithm to use for the following problem. Be direct and educational, but do not give the full code. If the candidate's code is empty, suggest a common approach for this type of problem. Do not explain your process.

                Problem: {problem_description}
                Candidate's Code:
                ```
                {code}
                ```
                
                Your Hint:"""
            }
            
            prompt = hint_prompts.get(hint_level, hint_prompts[1])
            
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: self.model.generate_content(prompt)
            )
            
            return response.text
        except Exception as e:
            print(f"Gemini API error: {e}")
            return self._get_fallback_hint(hint_level)
    
    async def generate_follow_up_question(self, code: str, analysis: Dict[str, Any], problem_description: str, interview_id: str = "") -> str:
        """Generate follow-up questions to probe understanding"""
        if not self.model:
            return "Can you explain your approach and what you think the time complexity is?"
            
        try:
            prompt = f"""You are CodeSage, an AI technical interviewer. Generate a follow-up question based on the candidate's code:
            
            Problem: {problem_description}
            Code: {code}
            Analysis: {analysis}
            
            Ask a thoughtful question that:
            1. Probes the candidate's understanding of their approach
            2. Tests their knowledge of time/space complexity
            3. Explores alternative solutions
            4. Validates their problem-solving methodology
            
            Be conversational and educational. Ask one specific question."""
            
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: self.model.generate_content(prompt)
            )
            
            return response.text
        except Exception as e:
            print(f"Gemini API error: {e}")
            return "Can you explain your approach and what you think the time complexity is?"
    
    async def generate_performance_report(self, interview_data: Dict[str, Any], interview_id: str = "") -> str:
        """Generate comprehensive performance report"""
        if not self.model:
            return "Performance report generation requires Gemini API key. Please configure it in your environment."
            
        try:
            prompt = f"""You are CodeSage, an AI technical interviewer. Generate a comprehensive performance report:
            
            Interview Data: {json.dumps(interview_data, indent=2)}
            
            Create a detailed report that includes:
            1. Overall performance assessment
            2. Strengths and areas for improvement
            3. Technical skills evaluation
            4. Problem-solving approach analysis
            5. Communication and collaboration assessment
            6. Recommendations for development
            
            Be professional, constructive, and specific. Provide actionable feedback."""
            
            loop = asyncio.get_event_loop()
            response = await loop.run_in_executor(
                None, 
                lambda: self.model.generate_content(prompt)
            )
            
            return response.text
        except Exception as e:
            print(f"Gemini API error: {e}")
            return "Performance report generation failed. Please try again."
    
    def _build_interview_prompt(
        self, 
        code: str, 
        analysis: Dict[str, Any], 
        context: List[Dict],
        problem_description: str
    ) -> str:
        """Build context-aware prompt for Gemini"""
        return f"""You are CodeSage, an AI technical interviewer conducting a live coding interview. You are supportive, educational, and adaptive.

        Problem: {problem_description}
        
        Candidate's Code:
        ```{analysis.get('language', 'python')}
        {code}
        ```
        
        Analysis Results:
        - Syntax Valid: {analysis.get('syntax', {}).get('valid', False)}
        - Runtime Success: {analysis.get('runtime', {}).get('success', False)}
        - Overall Score: {analysis.get('overall_score', 0)}/100
        - Time Complexity: {analysis.get('complexity', {}).get('time_complexity', 'Unknown')}
        - Space Complexity: {analysis.get('complexity', {}).get('space_complexity', 'Unknown')}
        - Quality Issues: {analysis.get('quality', {}).get('issues', [])}
        - Execution Time: {analysis.get('runtime', {}).get('execution_time', 0):.3f}s
        
        Recent Conversation: {context[-3:] if context else 'No previous context'}
        
        Provide adaptive feedback:
        1. Acknowledge what's working well (be specific)
        2. Provide constructive suggestions for improvement
        3. Ask follow-up questions to probe understanding
        4. Discuss complexity and optimization opportunities
        5. Offer encouragement and guidance
        
        Be conversational, supportive, and educational. Adapt your response based on performance.
        Keep responses concise but helpful (2-4 sentences max).
        If the code has issues, guide them toward the solution without giving it away.
        If the code is good, challenge them with follow-up questions or optimizations.
        
        Instead of just praising, you could instruct it to ask for clarification or a different perspective.
        If the code is good, praise it briefly, then ask them to explain it in a different way or describe a potential pitfall of their approach. For example: 'That's a great solution. Can you explain it to me as if I were a new developer who has never seen a hash map before?
        
        """
    
    def _get_fallback_response(self, analysis: Dict[str, Any]) -> str:
        """Fallback responses when Gemini API fails"""
        score = analysis.get('overall_score', 0)
        
        if score >= 90:
            return "Excellent work! Your solution is efficient and well-structured. Can you explain your approach and what you think the time complexity is?"
        elif score >= 70:
            return "Good progress! I can see you're on the right track. Let's think about how we can optimize this further. What data structures could help?"
        elif score >= 50:
            return "You're making progress! Let me give you a hint to help you improve. Think about the most efficient way to solve this problem."
        else:
            return "Let's work through this together. I'll help you break it down step by step. What's your initial approach?"
    
    def _get_fallback_hint(self, level: int) -> str:
        """Fallback hints when Gemini API fails"""
        hints = {
            1: "Think about the data structures you could use to solve this efficiently. What would give you the best time complexity?",
            2: "Consider using a hash map or set for O(1) lookups to avoid nested loops. How could you track elements you've seen?",
            3: "Try this approach: Use a set to track seen elements, then iterate once through the array. This will give you O(n) time complexity."
        }
        return hints.get(level, hints[1])
