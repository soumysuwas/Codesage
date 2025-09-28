from fastapi import APIRouter, HTTPException
from typing import Dict, Any, List
import uuid
import random
from datetime import datetime
from ..models.interview import (
    Interview, CreateInterviewRequest, StartInterviewRequest, 
    SubmitCodeRequest, SendMessageRequest, RequestHintRequest,
    Question, DifficultyLevel, InterviewStatus
)
from ..config import Config

router = APIRouter()

# In-memory storage (replace with database in production)
interviews_db: Dict[str, Interview] = {}

@router.post("/")
async def create_interview(interview_data: CreateInterviewRequest):
    """Create a new interview"""
    interview_id = str(uuid.uuid4())
    
    # Get all questions for the selected difficulty
    all_questions = get_questions_by_difficulty(interview_data.difficulty)
    
    # Filter by category if specified
    if interview_data.category != "all":
        filtered_questions = [q for q in all_questions if q.category == interview_data.category]
    else:
        filtered_questions = all_questions
        
    # Shuffle the filtered questions
    random.shuffle(filtered_questions)
    
    # Select a subset of questions up to MAX_QUESTIONS
    selected_questions = filtered_questions[:Config.MAX_QUESTIONS]
    
    interview = Interview(
        id=interview_id,
        candidate_name=interview_data.candidate_name,
        difficulty=interview_data.difficulty,
        category=interview_data.category,
        questions=selected_questions,
        status=InterviewStatus.CREATED,
        created_at=datetime.now()
    )
    
    interviews_db[interview_id] = interview
    
    return {"success": True, "interview": interview.dict()}

@router.get("/{interview_id}")
async def get_interview(interview_id: str):
    """Get interview details"""
    if interview_id not in interviews_db:
        raise HTTPException(status_code=404, detail="Interview not found")
    
    return {"success": True, "interview": interviews_db[interview_id].dict()}

@router.post("/{interview_id}/start")
async def start_interview(interview_id: str):
    """Start an interview"""
    if interview_id not in interviews_db:
        raise HTTPException(status_code=404, detail="Interview not found")
    
    interview = interviews_db[interview_id]
    interview.status = InterviewStatus.IN_PROGRESS
    interview.started_at = datetime.now()
    
    return {"success": True, "message": "Interview started"}

@router.post("/{interview_id}/submit-code")
async def submit_code(interview_id: str, request: SubmitCodeRequest):
    """Submit code for analysis"""
    if interview_id not in interviews_db:
        raise HTTPException(status_code=404, detail="Interview not found")
    
    # This would typically trigger code analysis via WebSocket
    # For now, return success
    return {"success": True, "message": "Code submitted for analysis"}

@router.get("/")
async def list_interviews():
    """List all interviews"""
    return {"success": True, "interviews": [interview.dict() for interview in interviews_db.values()]}

def get_questions_by_difficulty(difficulty: DifficultyLevel) -> List[Question]:
    """Get questions based on difficulty level"""
    questions = {
        DifficultyLevel.EASY: [
            Question(
                id="e1",
                title="Two Sum",
                description="Given an array of integers and a target sum, find two numbers that add up to the target. Return their indices.",
                difficulty=DifficultyLevel.EASY,
                category="arrays",
                test_cases=[{"input": {"nums": [2, 7, 11, 15], "target": 9}, "expected": [0, 1]}, {"input": {"nums": [3, 2, 4], "target": 6}, "expected": [1, 2]}],
                constraints="Array length <= 10^4",
                hints=["Brute force is O(n^2).", "Can you use a hash map?"],
                expected_complexity="O(n) time, O(n) space"
            ),
            Question(
                id="e2",
                title="Valid Parentheses",
                description="Given a string containing just '(', ')', '{', '}', '[' and ']', determine if the input string is valid.",
                difficulty=DifficultyLevel.EASY,
                category="strings",
                test_cases=[{"input": {"s": "()[]{}"}, "expected": True}, {"input": {"s": "(]"}, "expected": False}],
                constraints="String length is between 1 and 10^4.",
                hints=["Use a stack data structure.", "Push opening brackets onto the stack and pop when a matching closing bracket is found."],
                expected_complexity="O(n) time, O(n) space"
            ),
            Question(
                id="e3",
                title="Merge Two Sorted Lists",
                description="Merge two sorted linked lists and return it as a new sorted list.",
                difficulty=DifficultyLevel.EASY,
                category="linked_lists",
                test_cases=[{"input": {"l1": [1,2,4], "l2": [1,3,4]}, "expected": [1,1,2,3,4,4]}],
                constraints="The number of nodes in both lists is in the range [0, 50].",
                hints=["Use a dummy head to simplify the code.", "Iteratively compare the heads of the two lists and append the smaller one."],
                expected_complexity="O(n+m) time, O(1) space"
            ),
            Question(
                id="e4",
                title="Best Time to Buy and Sell Stock",
                description="Find the maximum profit you can achieve. You may complete at most one transaction.",
                difficulty=DifficultyLevel.EASY,
                category="arrays",
                test_cases=[{"input": {"prices": [7,1,5,3,6,4]}, "expected": 5}, {"input": {"prices": [7,6,4,3,1]}, "expected": 0}],
                constraints="1 <= prices.length <= 10^5",
                hints=["Keep track of the minimum price found so far.", "Iterate through the array once, calculating the potential profit at each step."],
                expected_complexity="O(n) time, O(1) space"
            ),
            Question(
                id="e5",
                title="Invert Binary Tree",
                description="Given the root of a binary tree, invert the tree, and return its root.",
                difficulty=DifficultyLevel.EASY,
                category="trees",
                test_cases=[{"input": {"root": [4,2,7,1,3,6,9]}, "expected": [4,7,2,9,6,3,1]}],
                constraints="The number of nodes in the tree is in the range [0, 100].",
                hints=["This can be solved recursively.", "For each node, swap its left and right children, then recurse on the children."],
                expected_complexity="O(n) time, O(h) space where h is the height of the tree"
            )
        ],
        DifficultyLevel.MEDIUM: [
            Question(
                id="m1",
                title="Longest Substring Without Repeating Characters",
                description="Given a string, find the length of the longest substring without repeating characters.",
                difficulty=DifficultyLevel.MEDIUM,
                category="strings",
                test_cases=[{"input": {"s": "abcabcbb"}, "expected": 3}, {"input": {"s": "pwwkew"}, "expected": 3}],
                constraints="0 <= s.length <= 5 * 10^4",
                hints=["Use a sliding window approach.", "A set or map can track characters in the current window."],
                expected_complexity="O(n) time, O(min(m,n)) space"
            ),
            Question(
                id="m2",
                title="Product of Array Except Self",
                description="Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].",
                difficulty=DifficultyLevel.MEDIUM,
                category="arrays",
                test_cases=[{"input": {"nums": [1,2,3,4]}, "expected": [24,12,8,6]}, {"input": {"nums": [-1,1,0,-3,3]}, "expected": [0,0,9,0,0]}],
                constraints="You must write an algorithm that runs in O(n) time and without using the division operation.",
                hints=["Calculate prefix products in one pass.", "Calculate suffix products in a second pass and multiply them with the prefixes."],
                expected_complexity="O(n) time, O(1) extra space (output array doesn't count)"
            ),
            Question(
                id="m3",
                title="Validate Binary Search Tree",
                description="Given the root of a binary tree, determine if it is a valid binary search tree (BST).",
                difficulty=DifficultyLevel.MEDIUM,
                category="trees",
                test_cases=[{"input": {"root": [2,1,3]}, "expected": True}, {"input": {"root": [5,1,4,None,None,3,6]}, "expected": False}],
                constraints="The number of nodes in the tree is in the range [1, 10^4].",
                hints=["A simple recursive check of root.left.val < root.val is not enough.", "Pass down the valid range (min, max) for each node as you recurse."],
                expected_complexity="O(n) time, O(h) space"
            ),
            Question(
                id="m4",
                title="Number of Islands",
                description="Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.",
                difficulty=DifficultyLevel.MEDIUM,
                category="graphs",
                test_cases=[{"input": {"grid": [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]}, "expected": 3}],
                constraints="m and n are between 1 and 300.",
                hints=["Iterate through each cell of the grid.", "If you find a '1', start a traversal (DFS or BFS) to find all connected land parts and mark them as visited."],
                expected_complexity="O(m*n) time, O(m*n) space in worst case for recursion stack"
            ),
            Question(
                id="m5",
                title="Container With Most Water",
                description="Find two lines that together with the x-axis form a container, such that the container contains the most water.",
                difficulty=DifficultyLevel.MEDIUM,
                category="arrays",
                test_cases=[{"input": {"height": [1,8,6,2,5,4,8,3,7]}, "expected": 49}],
                constraints="n == height.length, 2 <= n <= 10^5",
                hints=["Use a two-pointer approach, one at each end.", "Move the pointer pointing to the shorter line inward. Why?"],
                expected_complexity="O(n) time, O(1) space"
            )
        ],
        DifficultyLevel.HARD: [
            Question(
                id="h1",
                title="Median of Two Sorted Arrays",
                description="Given two sorted arrays, find the median of the two sorted arrays.",
                difficulty=DifficultyLevel.HARD,
                category="arrays",
                test_cases=[{"input": {"nums1": [1, 3], "nums2": [2]}, "expected": 2.0}, {"input": {"nums1": [1, 2], "nums2": [3, 4]}, "expected": 2.5}],
                constraints="The overall run time complexity should be O(log (m+n)).",
                hints=["This suggests a binary search approach.", "Partition both arrays to find the median."],
                expected_complexity="O(log(min(m,n))) time, O(1) space"
            ),
            Question(
                id="h2",
                title="Trapping Rain Water",
                description="Given n non-negative integers representing an elevation map, compute how much water it can trap after raining.",
                difficulty=DifficultyLevel.HARD,
                category="arrays",
                test_cases=[{"input": {"height": [0,1,0,2,1,0,1,3,2,1,2,1]}, "expected": 6}],
                constraints="n == height.length, 1 <= n <= 2 * 10^4",
                hints=["Water trapped at an index is min(max_left, max_right) - height[i].", "A two-pointer approach can solve this in O(n) time and O(1) space."],
                expected_complexity="O(n) time, O(1) space"
            ),
            Question(
                id="h3",
                title="Merge k Sorted Lists",
                description="You are given an array of k linked-lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.",
                difficulty=DifficultyLevel.HARD,
                category="linked_lists",
                test_cases=[{"input": {"lists": [[1,4,5],[1,3,4],[2,6]]}, "expected": [1,1,2,3,4,4,5,6]}],
                constraints="k == lists.length, 0 <= k <= 10^4",
                hints=["A min-heap (priority queue) is a great data structure for this.", "Insert the head of each list into the min-heap, then repeatedly extract the minimum and add its next node."],
                expected_complexity="O(N log k) time, O(k) space where N is total nodes"
            ),
            Question(
                id="h4",
                title="Largest Rectangle in Histogram",
                description="Given an array of integers heights representing the histogram's bar height, return the area of the largest rectangle.",
                difficulty=DifficultyLevel.HARD,
                category="arrays",
                test_cases=[{"input": {"heights": [2,1,5,6,2,3]}, "expected": 10}],
                constraints="1 <= heights.length <= 10^5",
                hints=["For each bar, the challenge is finding the nearest smaller bars to its left and right.", "A monotonic stack can solve this efficiently in one pass."],
                expected_complexity="O(n) time, O(n) space"
            ),
            Question(
                id="h5",
                title="Serialize and Deserialize Binary Tree",
                description="Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work.",
                difficulty=DifficultyLevel.HARD,
                category="trees",
                test_cases=[{"input": {"root": [1,2,3,None,None,4,5]}, "expected": [1,2,3,None,None,4,5]}],
                constraints="The number of nodes in the tree is in the range [0, 10^4].",
                hints=["A pre-order traversal (DFS) is a good choice for serialization.", "Use a special marker (like 'null') for null nodes to preserve the tree structure."],
                expected_complexity="O(n) time, O(n) space"
            )
        ]
    }
    
    return questions.get(difficulty, questions[DifficultyLevel.MEDIUM])
