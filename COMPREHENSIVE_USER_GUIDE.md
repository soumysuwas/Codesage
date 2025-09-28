# 🚀 CodeSage AI Technical Interviewer - Complete User Guide

## 📋 Table of Contents
1. [System Overview](#system-overview)
2. [Prerequisites](#prerequisites)
3. [Installation Guide](#installation-guide)
4. [Environment Setup](#environment-setup)
5. [Running the System](#running-the-system)
6. [Troubleshooting](#troubleshooting)
7. [Features Guide](#features-guide)
8. [API Documentation](#api-documentation)
9. [Support](#support)

---

## 🎯 System Overview

CodeSage is an AI-powered technical interviewer that conducts live, adaptive coding interviews with human-like insight. It provides:

- **Real-time Code Analysis** - Instant feedback on code quality and performance
- **AI-Powered Interviewing** - Intelligent conversation and adaptive questioning
- **Multi-Language Support** - Python, JavaScript, Java, C++
- **Voice Integration** - Speech-to-text and text-to-speech capabilities
- **Performance Tracking** - Comprehensive metrics and reporting
- **Live Hints System** - Progressive guidance for candidates

### Architecture
- **Backend**: Python FastAPI with WebSocket support
- **Frontend**: React with TypeScript and Vite
- **AI Service**: Google Gemini API
- **Database**: In-memory (no external database required)

---

## 🔧 Prerequisites

### System Requirements
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 18.04+)
- **RAM**: Minimum 4GB, Recommended 8GB+
- **Storage**: 2GB free space
- **Internet**: Required for AI API calls

### Required Software
1. **Python 3.8+** (with pip)
2. **Node.js 16+** (with npm)
3. **Git** (for cloning the repository)
4. **Google Gemini API Key** (free tier available)

---

## 📦 Installation Guide

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd CodeSage
```

### Step 2: Backend Setup

#### Option A: Automated Setup (Recommended)
```bash
# Run the universal setup script
python setup.py
```

#### Option B: Manual Setup
```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install
```

### Step 4: Environment Configuration
```bash
# Navigate to backend directory
cd backend

# Create .env file
touch .env  # On Windows: type nul > .env

# Edit .env file with your configuration
```

---

## ⚙️ Environment Setup

### Backend Environment Variables (.env file)
Create a `.env` file in the `backend` directory with the following content:

```bash
# Gemini API Configuration (REQUIRED)
GEMINI_API_KEY=your_gemini_api_key_here

# Server Configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True

# CORS Configuration
CORS_ORIGINS=http://localhost:3000

# Security
SECRET_KEY=your-secret-key-change-this

# Code Execution Settings
CODE_TIMEOUT=5
MAX_MEMORY_MB=128

# Interview Configuration
MAX_QUESTIONS=5
INTERVIEW_DURATION_MINUTES=60
```

### Getting Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Paste it in your `.env` file

### Frontend Configuration
The frontend automatically connects to the backend via proxy configuration in `vite.config.ts`. No additional configuration needed.

---

## 🚀 Running the System

### Method 1: Universal Python Script (Recommended)
```bash
# From the root directory
python start.py
```

### Method 2: Platform-Specific Scripts

#### Windows
```bash
# Run the Windows batch script
install.bat
```

#### macOS/Linux
```bash
# Make the script executable
chmod +x install.sh

# Run the installation script
./install.sh
```

### Method 3: Manual Start

#### Terminal 1: Start Backend
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

#### Terminal 2: Start Frontend
```bash
cd frontend
npm run dev
```

### Method 4: Using Start Script
```bash
# Make executable (Linux/macOS)
chmod +x start.sh

# Run the start script
./start.sh
```

---

## 🌐 Accessing the Application

Once both services are running:

- **Main Application**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

---

## 🔍 Troubleshooting

### Common Issues and Solutions

#### 1. Port Already in Use
```bash
# Kill processes using ports 3000 and 8000
# On Windows:
netstat -ano | findstr :3000
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -ti:3000 | xargs kill -9
lsof -ti:8000 | xargs kill -9
```

#### 2. Python Dependencies Issues
```bash
# Clear pip cache and reinstall
pip cache purge
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

#### 3. Node.js Dependencies Issues
```bash
# Clear npm cache and reinstall
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

#### 4. WebSocket Connection Issues
- Ensure both backend and frontend are running
- Check firewall settings
- Verify CORS configuration in backend

#### 5. Gemini API Issues
- Verify API key is correct
- Check API quota limits
- Ensure internet connection is stable

### Logs and Debugging

#### Backend Logs
```bash
# Run backend with verbose logging
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --log-level debug
```

#### Frontend Logs
```bash
# Run frontend with verbose logging
cd frontend
npm run dev -- --debug
```

### Verification Script
```bash
# Run the verification script to check installation
python verify_installation.py
```

---

## 🎮 Features Guide

### 1. Creating an Interview
1. Open http://localhost:3000
2. Enter candidate name
3. Select difficulty level (Easy, Medium, Hard)
4. Choose category (All, Algorithms, Data Structures, etc.)
5. Click "Start Interview"

### 2. Coding Interface
- **Code Editor**: Monaco Editor with syntax highlighting
- **Language Selection**: Python, JavaScript, Java, C++
- **Run Code**: Execute code in sandboxed environment
- **Real-time Analysis**: Instant feedback on code quality

### 3. AI Interviewer Features
- **Chat Interface**: Talk with the AI interviewer
- **Voice Input**: Use microphone for speech-to-text
- **Voice Output**: AI responses with text-to-speech
- **Progressive Hints**: Request hints at different levels
- **Follow-up Questions**: AI asks intelligent follow-ups

### 4. Performance Tracking
- **Live Metrics**: Real-time performance indicators
- **Code Quality**: Syntax, runtime, and complexity analysis
- **Time Tracking**: Monitor interview duration
- **Progress Visualization**: Charts and graphs

### 5. Session Management
- **Save Progress**: Automatic session saving
- **Resume Interview**: Continue where you left off
- **Export Results**: Download performance reports

---

## 📚 API Documentation

### REST API Endpoints

#### Health Check
```http
GET /health
```

#### Create Interview
```http
POST /api/interviews/
Content-Type: application/json

{
  "candidate_name": "John Doe",
  "difficulty": "medium",
  "category": "algorithms"
}
```

#### Get Interview
```http
GET /api/interviews/{interview_id}
```

#### Start Interview
```http
POST /api/interviews/{interview_id}/start
```

#### Submit Code
```http
POST /api/interviews/{interview_id}/submit
Content-Type: application/json

{
  "code": "def solution():\n    return 'Hello World'",
  "language": "python",
  "problem_description": "Print Hello World"
}
```

### WebSocket Events

#### Client to Server
- `analyze_code`: Send code for analysis
- `send_message`: Send chat message
- `request_hint`: Request hint at specific level
- `request_follow_up`: Request follow-up question
- `generate_report`: Generate performance report

#### Server to Client
- `code_analysis`: Code analysis results
- `chat_message`: AI response message
- `hint_response`: Hint response
- `follow_up_question`: Follow-up question
- `performance_report`: Performance report

---

## 🛠️ Development Guide

### Project Structure
```
CodeSage/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── services/
│   │   └── routes/
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   └── types/
│   ├── package.json
│   └── vite.config.ts
├── setup.py
├── start.py
└── README.md
```

### Adding New Features
1. Backend: Add routes in `backend/app/routes/`
2. Frontend: Add components in `frontend/src/components/`
3. WebSocket: Add handlers in `backend/app/main.py`
4. Types: Update `frontend/src/types/index.ts`

### Testing
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests
cd frontend
npm test
```

---

## 🔒 Security Considerations

### API Key Security
- Never commit API keys to version control
- Use environment variables for sensitive data
- Rotate API keys regularly

### Code Execution Security
- Code runs in sandboxed environment
- Limited memory and execution time
- No file system access

### Network Security
- CORS properly configured
- Rate limiting implemented
- Input validation and sanitization

---

## 📞 Support

### Getting Help
1. Check this guide first
2. Review troubleshooting section
3. Check logs for error messages
4. Verify all prerequisites are met

### Common Commands Reference
```bash
# Check if services are running
ps aux | grep -E "(uvicorn|vite)"

# Check port usage
netstat -tulpn | grep -E ":(3000|8000)"

# View backend logs
tail -f backend/logs/app.log

# Restart services
pkill -f uvicorn && pkill -f vite
```

### System Requirements Check
```bash
# Check Python version
python --version

# Check Node.js version
node --version

# Check npm version
npm --version

# Check if ports are available
lsof -i :3000
lsof -i :8000
```

---

## 🎉 Quick Start Summary

1. **Clone repository**: `git clone <repo-url> && cd CodeSage`
2. **Run setup**: `python setup.py`
3. **Configure API key**: Edit `backend/.env` with your Gemini API key
4. **Start system**: `python start.py`
5. **Open browser**: Navigate to http://localhost:3000
6. **Start interviewing**: Create an interview and begin!

---

## 📝 License

This project is licensed under the MIT License. See LICENSE file for details.

---

## 🤝 Contributing

We welcome contributions! Please see CONTRIBUTING.md for guidelines.

---

*Last updated: September 2024*
*Version: 1.0.0*
