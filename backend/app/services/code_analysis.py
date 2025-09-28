import ast
import re
import time
import subprocess
import tempfile
import os
from typing import Dict, Any
from ..config import Config

class CodeAnalysisService:
    def __init__(self):
        self.timeout = Config.CODE_TIMEOUT
        self.max_memory = Config.MAX_MEMORY_MB * 1024 * 1024
    
    async def analyze_code(self, code: str, language: str) -> Dict[str, Any]:
        """Comprehensive code analysis"""
        analysis = {
            "syntax": await self._analyze_syntax(code, language),
            "runtime": await self._analyze_runtime(code, language),
            "complexity": await self._analyze_complexity(code, language),
            "quality": await self._analyze_quality(code, language),
            "performance": await self._analyze_performance(code, language),
            "language": language
        }
        
        # Calculate overall score
        analysis["overall_score"] = self._calculate_overall_score(analysis)
        
        return analysis
    
    async def _analyze_syntax(self, code: str, language: str) -> Dict[str, Any]:
        """Analyze syntax"""
        if language == "python":
            try:
                ast.parse(code)
                return {"valid": True, "errors": []}
            except SyntaxError as e:
                return {"valid": False, "errors": [f"Line {e.lineno}: {e.msg}"]}
            except Exception as e:
                return {"valid": False, "errors": [str(e)]}
        else:
            return {"valid": True, "errors": []}
    
    async def _analyze_runtime(self, code: str, language: str) -> Dict[str, Any]:
        """Analyze runtime behavior"""
        start_time = time.time()
        result = await self._execute_code(code, language)
        execution_time = time.time() - start_time
        
        return {
            "execution_time": execution_time,
            "output": result.get("output", ""),
            "error": result.get("error", ""),
            "success": result.get("return_code", 1) == 0,
            "return_code": result.get("return_code", 1)
        }
    
    async def _execute_code(self, code: str, language: str) -> Dict[str, Any]:
        """Execute code safely"""
        try:
            if language == "python":
                return await self._execute_python(code)
            elif language == "javascript":
                return await self._execute_javascript(code)
            elif language == "java":
                return await self._execute_java(code)
            elif language == "cpp":
                return await self._execute_cpp(code)
            else:
                return {"error": "Unsupported language", "output": "", "return_code": 1}
        except Exception as e:
            return {"error": str(e), "output": "", "return_code": 1}
    
    async def _execute_python(self, code: str) -> Dict[str, Any]:
        """Execute Python code safely"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            result = subprocess.run(
                ['python', temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=tempfile.gettempdir()
            )
            
            return {
                "output": result.stdout,
                "error": result.stderr,
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"error": "Execution timeout", "output": "", "return_code": 1}
        finally:
            os.unlink(temp_file)
    
    async def _execute_javascript(self, code: str) -> Dict[str, Any]:
        """Execute JavaScript code using Node.js"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            result = subprocess.run(
                ['node', temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=tempfile.gettempdir()
            )
            
            return {
                "output": result.stdout,
                "error": result.stderr,
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"error": "Execution timeout", "output": "", "return_code": 1}
        finally:
            os.unlink(temp_file)
    
    async def _execute_java(self, code: str) -> Dict[str, Any]:
        """Execute Java code"""
        class_name = "Solution"
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.java', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            # Compile Java code
            compile_result = subprocess.run(
                ['javac', temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=tempfile.gettempdir()
            )
            
            if compile_result.returncode != 0:
                return {"error": f"Compilation error: {compile_result.stderr}", "output": "", "return_code": 1}
            
            # Execute compiled class
            class_file = temp_file.replace('.java', '.class')
            result = subprocess.run(
                ['java', '-cp', tempfile.gettempdir(), class_name],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=tempfile.gettempdir()
            )
            
            return {
                "output": result.stdout,
                "error": result.stderr,
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"error": "Execution timeout", "output": "", "return_code": 1}
        finally:
            # Clean up files
            for ext in ['.java', '.class']:
                try:
                    os.unlink(temp_file.replace('.java', ext))
                except:
                    pass
    
    async def _execute_cpp(self, code: str) -> Dict[str, Any]:
        """Execute C++ code"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False) as f:
            f.write(code)
            temp_file = f.name
        
        try:
            # Compile C++ code
            compile_result = subprocess.run(
                ['g++', '-o', temp_file.replace('.cpp', ''), temp_file],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=tempfile.gettempdir()
            )
            
            if compile_result.returncode != 0:
                return {"error": f"Compilation error: {compile_result.stderr}", "output": "", "return_code": 1}
            
            # Execute compiled binary
            result = subprocess.run(
                [temp_file.replace('.cpp', '')],
                capture_output=True,
                text=True,
                timeout=self.timeout,
                cwd=tempfile.gettempdir()
            )
            
            return {
                "output": result.stdout,
                "error": result.stderr,
                "return_code": result.returncode
            }
        except subprocess.TimeoutExpired:
            return {"error": "Execution timeout", "output": "", "return_code": 1}
        finally:
            # Clean up files
            for ext in ['.cpp', '']:
                try:
                    os.unlink(temp_file.replace('.cpp', ext))
                except:
                    pass
    
    async def _analyze_complexity(self, code: str, language: str) -> Dict[str, Any]:
        """Analyze algorithmic complexity"""
        if language == "python":
            return self._analyze_python_complexity(code)
        elif language == "javascript":
            return self._analyze_javascript_complexity(code)
        else:
            return {"time_complexity": "Unknown", "space_complexity": "Unknown"}
    
    def _analyze_python_complexity(self, code: str) -> Dict[str, Any]:
        """Analyze Python code complexity"""
        # Count nested loops
        nested_loops = code.count("for ") + code.count("while ")
        
        # Check for common patterns
        if "for i in range" in code and "for j in range" in code:
            return {"time_complexity": "O(n²)", "space_complexity": "O(1)"}
        elif "for " in code:
            return {"time_complexity": "O(n)", "space_complexity": "O(1)"}
        else:
            return {"time_complexity": "O(1)", "space_complexity": "O(1)"}
    
    def _analyze_javascript_complexity(self, code: str) -> Dict[str, Any]:
        """Analyze JavaScript code complexity"""
        if "for (let i" in code and "for (let j" in code:
            return {"time_complexity": "O(n²)", "space_complexity": "O(1)"}
        elif "for (" in code or "forEach" in code:
            return {"time_complexity": "O(n)", "space_complexity": "O(1)"}
        else:
            return {"time_complexity": "O(1)", "space_complexity": "O(1)"}
    
    async def _analyze_quality(self, code: str, language: str) -> Dict[str, Any]:
        """Analyze code quality"""
        quality_score = 0
        issues = []
        
        # Check for comments
        if "//" in code or "#" in code or "/*" in code:
            quality_score += 20
        else:
            issues.append("No comments found")
        
        # Check for proper naming
        if re.search(r'[a-z][a-zA-Z0-9]*', code):
            quality_score += 20
        else:
            issues.append("Poor variable naming")
        
        # Check for proper formatting
        if len(code.split('\n')) > 1:
            quality_score += 20
        else:
            issues.append("Poor formatting")
        
        # Check for error handling
        if "try" in code or "catch" in code or "if" in code:
            quality_score += 20
        else:
            issues.append("No error handling")
        
        # Check for efficiency
        if "for" in code and "in" in code:
            quality_score += 20
        else:
            issues.append("Could be more efficient")
        
        return {
            "score": quality_score,
            "issues": issues,
            "grade": "A" if quality_score >= 80 else "B" if quality_score >= 60 else "C"
        }
    
    async def _analyze_performance(self, code: str, language: str) -> Dict[str, Any]:
        """Analyze performance characteristics"""
        # This would run the code multiple times to measure performance
        # For now, return basic metrics
        return {
            "execution_time": 0.001,  # Placeholder
            "memory_usage": "Low",    # Placeholder
            "efficiency": "Good"      # Placeholder
        }
    
    def _calculate_overall_score(self, analysis: Dict[str, Any]) -> int:
        """Calculate overall score from all analysis components"""
        score = 0
        
        # Syntax score (25%)
        if analysis["syntax"]["valid"]:
            score += 25
        
        # Runtime score (25%)
        if analysis["runtime"]["success"]:
            score += 25
        
        # Quality score (25%)
        score += analysis["quality"]["score"] * 0.25
        
        # Performance score (25%)
        score += 25  # Placeholder
        
        return min(int(score), 100)
