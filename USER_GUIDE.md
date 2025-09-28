# CodeSage AI Technical Interviewer - User Guide

## 🎯 Overview

CodeSage is an AI-powered technical interviewer that conducts live, adaptive coding interviews with human-like insight. It analyzes code in real-time, provides context-aware hints, assesses code quality beyond correctness, and generates detailed performance reports.

## 🚀 Quick Start (5 Minutes)

### Step 1: Download the Code
```bash
# Clone or download the repository
git clone <repository-url>
cd suwas
```

### Step 2: Run Automated Setup
```bash
# Run the automated setup script
python setup.py
```

### Step 3: Add Your Gemini API Key
```bash
# Edit the environment file
nano backend/.env
# Add your Gemini API key:
# GEMINI_API_KEY=your_actual_api_key_here
```

### Step 4: Start the Application
```bash
# Start both backend and frontend
python start.py
```

### Step 5: Open in Browser
- Open your browser and go to: `http://localhost:3000`
- Start conducting AI-powered technical interviews!

---

## 📋 System Requirements

### Minimum Requirements
- **Operating System**: Windows 10+, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Python**: 3.11 or higher
- **Node.js**: 18.0 or higher
- **RAM**: 4GB minimum, 8GB recommended
- **Storage**: 2GB free space
- **Internet**: Required for AI features

### Required Tools
- **Python 3.11+**: [Download Python](https://www.python.org/downloads/)
- **Node.js 18+**: [Download Node.js](https://nodejs.org/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Gemini API Key**: [Get API Key](https://makersuite.google.com/app/apikey)

---

## 🛠️ Detailed Installation Guide

### For Windows Users

#### 1. Install Python
1. Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation:
   ```cmd
   python --version
   pip --version
   ```

#### 2. Install Node.js
1. Download Node.js 18+ from [nodejs.org](https://nodejs.org/)
2. Run the installer
3. Verify installation:
   ```cmd
   node --version
   npm --version
   ```

#### 3. Install Git
1. Download Git from [git-scm.com](https://git-scm.com/downloads)
2. Run the installer with default settings
3. Verify installation:
   ```cmd
   git --version
   ```

### For macOS Users

#### 1. Install Homebrew (if not already installed)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 2. Install Python
```bash
brew install python@3.11
```

#### 3. Install Node.js
```bash
brew install node
```

#### 4. Install Git
```bash
brew install git
```

### For Linux Users (Ubuntu/Debian)

#### 1. Update system packages
```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Install Python 3.11
```bash
sudo apt install python3.11 python3.11-venv python3.11-pip -y
```

#### 3. Install Node.js 18
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

#### 4. Install Git
```bash
sudo apt install git -y
```

---

## 🔧 Manual Installation (If Automated Setup Fails)

### Backend Setup

#### 1. Navigate to backend directory
```bash
cd backend
```

#### 2. Create virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Python dependencies
```bash
# Windows
venv\Scripts\pip install -r requirements.txt

# macOS/Linux
venv/bin/pip install -r requirements.txt
```

#### 4. Create environment file
```bash
# Create .env file
nano .env
```

Add the following content:
```env
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

# Code Execution
CODE_TIMEOUT=5
MAX_MEMORY_MB=128

# Interview Configuration
MAX_QUESTIONS=5
INTERVIEW_DURATION_MINUTES=60
```

### Frontend Setup

#### 1. Navigate to frontend directory
```bash
cd frontend
```

#### 2. Install Node.js dependencies
```bash
npm install
```

---

## 🚀 Running the Application

### Method 1: Automated Start (Recommended)
```bash
# From the root directory
python start.py
```

### Method 2: Manual Start

#### Terminal 1 - Backend
```bash
cd backend
# Windows
venv\Scripts\python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# macOS/Linux
venv/bin/python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Terminal 2 - Frontend
```bash
cd frontend
npm run dev
```

### Method 3: Individual Services
```bash
# Backend only
cd backend && venv/bin/python -m uvicorn app.main:app --reload

# Frontend only
cd frontend && npm run dev
```

---

## 🌐 Accessing the Application

### URLs
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

### Browser Compatibility
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

---

## 📖 How to Use CodeSage

### 1. Starting an Interview

#### Step 1: Create Interview
1. Open http://localhost:3000 in your browser
2. Enter candidate name
3. Select difficulty level (Easy/Medium/Hard)
4. Choose category (All/Algorithms/Data Structures/System Design)
5. Click "Start Interview"

#### Step 2: Interview Interface
- **Code Editor**: Write your code in the Monaco editor
- **Question Panel**: View the current problem and constraints
- **Chat Interface**: Interact with the AI interviewer
- **Performance Panel**: Monitor real-time analysis

### 2. AI Interviewer Features

#### Real-time Code Analysis
- **Syntax Checking**: Instant syntax error detection
- **Runtime Analysis**: Code execution with output capture
- **Complexity Analysis**: Time and space complexity estimation
- **Quality Assessment**: Code style and best practices evaluation

#### AI Responses
- **Adaptive Feedback**: AI responds based on your code quality
- **Progressive Hints**: Three levels of hints (Nudge → Guide → Direction)
- **Follow-up Questions**: AI asks intelligent follow-up questions
- **Performance Reports**: Comprehensive assessment at the end

#### Voice Features
- **Voice Input**: Click the microphone to speak
- **Voice Output**: AI responses can be read aloud
- **Voice Commands**: Navigate using voice commands

### 3. Supported Programming Languages

#### Python
```python
def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates
```

#### JavaScript
```javascript
function findDuplicates(arr) {
    const seen = new Set();
    const duplicates = [];
    for (const item of arr) {
        if (seen.has(item)) {
            duplicates.push(item);
        } else {
            seen.add(item);
        }
    }
    return duplicates;
}
```

#### Java
```java
public class Solution {
    public List<Integer> findDuplicates(int[] arr) {
        Set<Integer> seen = new HashSet<>();
        List<Integer> duplicates = new ArrayList<>();
        for (int item : arr) {
            if (seen.contains(item)) {
                duplicates.add(item);
            } else {
                seen.add(item);
            }
        }
        return duplicates;
    }
}
```

#### C++
```cpp
#include <vector>
#include <unordered_set>
using namespace std;

vector<int> findDuplicates(vector<int>& arr) {
    unordered_set<int> seen;
    vector<int> duplicates;
    for (int item : arr) {
        if (seen.find(item) != seen.end()) {
            duplicates.push_back(item);
        } else {
            seen.insert(item);
        }
    }
    return duplicates;
}
```

### 4. Interview Navigation

#### Controls
- **Run Code**: Execute your code and see results
- **Submit Code**: Submit your solution for analysis
- **Request Hint**: Ask the AI for hints
- **Next Question**: Move to the next problem
- **Voice Input**: Toggle voice input on/off

#### Keyboard Shortcuts
- **Ctrl+Enter**: Run code
- **Ctrl+S**: Submit code
- **Ctrl+H**: Request hint
- **Ctrl+N**: Next question
- **Ctrl+M**: Toggle voice input

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "Python not found" Error
**Solution**: Ensure Python is installed and added to PATH
```bash
# Check Python installation
python --version
# If not found, reinstall Python with "Add to PATH" checked
```

#### 2. "Node.js not found" Error
**Solution**: Install Node.js from [nodejs.org](https://nodejs.org/)
```bash
# Check Node.js installation
node --version
npm --version
```

#### 3. "Module not found" Errors
**Solution**: Reinstall dependencies
```bash
# Backend
cd backend
venv/bin/pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

#### 4. "Port already in use" Error
**Solution**: Kill processes using the ports
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :8000
kill -9 <PID>
```

#### 5. "Gemini API Error" Error
**Solution**: Check your API key
1. Verify API key is correct in `backend/.env`
2. Ensure you have credits in your Google AI Studio account
3. Check internet connection

#### 6. "CORS Error" Error
**Solution**: Check CORS configuration
1. Ensure frontend is running on port 3000
2. Check `CORS_ORIGINS` in `backend/.env`
3. Restart both servers

### Performance Issues

#### Slow Code Execution
- Reduce `CODE_TIMEOUT` in `backend/.env`
- Check system resources (CPU, RAM)
- Close other applications

#### Slow AI Responses
- Check internet connection
- Verify Gemini API key is valid
- Check API quota limits

#### Frontend Loading Issues
- Clear browser cache
- Check browser console for errors
- Restart frontend server

---

## 📊 System Monitoring

### Health Check
Visit http://localhost:8000/health to check system status:
```json
{
  "status": "OK",
  "service": "CodeSage AI Interviewer",
  "version": "1.0.0",
  "gemini_configured": true,
  "features": {
    "real_time_analysis": true,
    "voice_interaction": true,
    "code_execution": true,
    "ai_interviewer": true
  }
}
```

### Logs
- **Backend logs**: Check terminal running backend
- **Frontend logs**: Check browser console (F12)
- **Error logs**: Check terminal output for error messages

---

## 🔒 Security Considerations

### API Key Security
- Never commit your Gemini API key to version control
- Use environment variables for sensitive data
- Rotate API keys regularly

### Code Execution Safety
- Code runs in sandboxed environment
- Timeout and memory limits are enforced
- No network access from executed code

### Data Privacy
- All data is stored in memory (not persistent)
- No data is sent to external services except Gemini API
- Interview data is not logged or stored

---

## 🆘 Getting Help

### Documentation
- **API Documentation**: http://localhost:8000/docs
- **README**: Check README.md in the project root
- **Code Comments**: Check source code for detailed comments

### Common Commands
```bash
# Check system status
python -c "import sys; print(sys.version)"
node --version
npm --version

# Check if ports are free
netstat -an | grep :8000
netstat -an | grep :3000

# Check Python packages
pip list

# Check Node.js packages
npm list
```

### Support
If you encounter issues not covered in this guide:
1. Check the troubleshooting section above
2. Verify all requirements are met
3. Check the logs for error messages
4. Ensure all dependencies are properly installed

---

## 🎉 Congratulations!

You now have a fully functional AI Technical Interviewer system running on your machine! 

**Next Steps:**
1. Try creating your first interview
2. Test the voice features
3. Experiment with different programming languages
4. Explore the AI interviewer's adaptive responses

**Happy Interviewing!** 🚀
