# Future Work & Unimplemented Features

This document outlines features from the original problem statement that are planned for future development.

### 1. Advanced Algorithmic Complexity Analysis

-   **Goal**: Automatically determine the time and space complexity (Big O notation) of the user's code.
-   **Current Status**: The backend service includes a placeholder for this feature (`_analyze_complexity`), but it currently returns "N/A". The frontend UI is ready to display this data once available.
-   **Implementation Plan**: Integrate a static analysis library that can parse the code into an Abstract Syntax Tree (AST). By analyzing loops, recursion, and data structures within the AST, the algorithmic complexity can be calculated.

### 2. Comprehensive Hiring Manager Dashboard

-   **Goal**: Provide a persistent, shareable performance report for hiring managers to review after an interview is complete.
-   **Current Status**: The application provides excellent real-time feedback to the candidate during the interview via the Performance Panel. However, this data is not saved or aggregated into a post-interview report.
-   **Implementation Plan**:
    1.  Develop a database schema to store interview session data, including code submissions, performance metrics, and AI chat logs.
    2.  Create a new set of API endpoints to retrieve and aggregate this data for a specific interview session.
    3.  Build a new route and set of components in the React frontend for a "Hiring Manager Dashboard" that visualizes this data, providing a comprehensive overview of the candidate's performance.

### 3. Dynamic Difficulty Adaptation

-   **Goal**: The AI should dynamically select the next question based on the candidate's performance in the current stage.
-   **Current Status**: The system has a pre-defined list of questions categorized by difficulty. The user selects the difficulty at the start of the interview.
-   **Implementation Plan**: Enhance the interview session logic. After a candidate successfully solves a problem, the backend could analyze their performance (e.g., time taken, hints used, code efficiency) to decide whether to present a slightly harder or easier question next from the existing question bank.