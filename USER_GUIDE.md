# CodeSage AI Technical Interviewer - User Guide

## 🎯 Overview

CodeSage is an AI-powered technical interviewer that conducts live, adaptive coding interviews. It analyzes code in real-time, provides context-aware hints, assesses code quality, and generates detailed performance reports.

## 🚀 Quick Start

1.  **Download the Code**
    ```bash
    git clone <repository-url>
    cd CodeSage
    ```

2.  **Run Automated Setup**
    ```bash
    python setup.py
    ```

3.  **Add Your Gemini API Key**
    *   Edit the `backend/.env` file.
    *   Set your key: `GEMINI_API_KEY=your_actual_api_key_here`

4.  **Start the Application**
    ```bash
    python start.py
    ```

5.  **Open in Browser**
    *   Navigate to `http://localhost:3000` to begin.

---

## 📋 Prerequisites

Ensure the following tools are installed on your system:

-   **Python**: 3.11 or higher ([Download](https://www.python.org/downloads/))
-   **Node.js**: 18.0 or higher ([Download](https://nodejs.org/))
-   **Git**: ([Download](https://git-scm.com/downloads))
-   **Gemini API Key**: ([Get API Key](https://makersuite.google.com/app/apikey))

---

## 🔧 Manual Installation

If the automated setup (`python setup.py`) fails, follow these steps.

### Backend Setup
```bash
# From the project root
cd backend

# Create and activate virtual environment (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create and configure environment file
cp env.example .env
nano .env  # Add your GEMINI_API_KEY
```

### Frontend Setup
```bash
# From the project root
cd frontend
npm install
```

---

## 🚀 Running the Application

### Recommended Method
This command starts both the backend and frontend servers.
```bash
# From the project root
python start.py
```

### Manual Start
Run each command in a separate terminal.

**Terminal 1: Backend**
```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --port 8000
```

**Terminal 2: Frontend**
```bash
cd frontend
npm run dev
```

---

## 🌐 Accessing the Application

-   **Frontend**: http://localhost:3000
-   **API Docs**: http://localhost:8000/docs
-   **Health Check**: http://localhost:8000/health

---

## 📖 How to Use CodeSage

1.  **Start an Interview**: Open the application, enter your name, and select the interview difficulty and category.
2.  **Code Editor**: Write your solution in the Monaco editor.
3.  **AI Interaction**: Use the chat interface to ask questions or request hints from the AI.
4.  **Real-time Analysis**: Run your code to see instant feedback on syntax, performance, complexity, and quality in the performance panel.
5.  **Voice Features**: Use the microphone for voice input and to hear AI responses read aloud.

---

## 🔧 Troubleshooting

-   **"Python/Node not found"**: Ensure Python and Node.js are installed and their paths are configured correctly in your system's environment variables.
-   **Module Not Found**: Re-run dependency installation.
    -   Backend: `pip install -r backend/requirements.txt`
    -   Frontend: `npm install --prefix frontend`
-   **Port Already in Use**: Identify and stop the process using port 3000 or 8000, or configure a different port in `backend/.env` and `frontend/vite.config.ts`.
-   **Gemini API Error**: Double-check that your API key in `backend/.env` is correct and has active credits.
-   **CORS Error**: Ensure `CORS_ORIGINS` in `backend/.env` matches the frontend URL (default is `http://localhost:3000`).

---

## 🔒 Security

-   **API Keys**: Your `GEMINI_API_KEY` is stored locally in `backend/.env` and is not committed to version control.
-   **Code Execution**: User-submitted code is executed in a sandboxed environment with strict timeout and memory limits.

Happy Interviewing! 🚀
