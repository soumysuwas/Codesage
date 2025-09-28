# CodeSage: The AI Technical Interviewer

CodeSage is an AI-powered platform that conducts live, adaptive coding interviews. It analyzes code in real-time, provides context-aware hints via an AI agent, and assesses code against a variety of metrics.

This project was developed based on the requirements of the Eightfold AI Hackathon, focusing on creating an intelligent and interactive interview experience.

## ✨ Implemented Features

Based on the problem statement, the following core features have been implemented:

-   **Real-time Code Execution & Analysis**
    -   **How it works**: The backend uses a sandboxed environment to securely execute user-submitted code in Python, JavaScript, Java, and C++. A FastAPI WebSocket connection provides immediate feedback on correctness, execution time, and memory usage to the React frontend.

-   **AI Interviewer Agent**
    -   **How it works**: Leveraging the Google Gemini API, the AI acts as an interactive interviewer. It can process the user's current code and conversation context to provide progressive, helpful hints without giving away the solution. This is managed by the `gemini_service` on the backend.

-   **Interactive Web-Based IDE**
    -   **How it works**: The frontend is built with React and TypeScript, featuring the Monaco Editor to provide a familiar coding environment. The UI is divided into dedicated panels for the problem description, code editor, and live performance feedback, creating a seamless user experience.

-   **Voice Integration**
    -   **How it works**: The frontend utilizes the browser's native Web Speech API for both speech-to-text and text-to-speech. This allows candidates to interact with the AI agent using their voice, and hear its responses spoken aloud.

## 🏗️ Architecture

-   **Backend**: Python, FastAPI, WebSockets, Google Gemini API
-   **Frontend**: React 18, TypeScript, Monaco Editor, Vite, Socket.io

## 🛠️ Installation & Setup

### Prerequisites

-   Python 3.11+
-   Node.js 18+
-   A Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### 🚀 Quick Start

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd CodeSage
    ```

2.  **Run the installation script:**
    *   On **macOS/Linux**: `chmod +x install.sh && ./install.sh`
    *   On **Windows**: `install.bat`

3.  **Configure your API Key:**
    *   Open `backend/.env` and add your Gemini API key: `GEMINI_API_KEY=your_key_here`

4.  **Run the application:**
    *   On **macOS/Linux**: `./start.sh`
    *   On **Windows**: `start.bat`

5.  **Open your browser** and navigate to `http://localhost:3000`.

## 🔧 Troubleshooting

-   **Dependency Errors**: If you encounter module errors, try removing the `node_modules` (frontend) and `venv` (backend) directories and re-running the installation script.
-   **Port Already in Use**: The app uses ports `3000` and `8000`. If they are occupied, stop the process using them.
-   **Gemini API Error**: Ensure your API key in `backend/.env` is correct and valid.
-   **Verification Script**: For a detailed diagnosis, run `python verify_installation.py`.
