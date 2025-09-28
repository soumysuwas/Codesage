# CodeSage: The AI Technical Interviewer

Building Intelligence That Evaluates Intelligence

## 🚀 Overview

CodeSage is an AI-powered technical interviewer that conducts live, adaptive coding interviews with human-like insight. It analyzes code in real-time, provides context-aware hints, assesses code quality beyond correctness, and generates detailed performance reports.

## ✨ Features

### Core Requirements
- **Real-time Code Analysis Engine**: Continuously tracks code as it's written and runs it safely in a sandboxed environment
- **Agentic Interviewer Hint System**: Adjusts problem difficulty dynamically and offers progressive hints
- **Deep Code Quality Assessment**: Evaluates style, readability, and adherence to standards
- **Comprehensive Reporting System**: Presents metrics in a clean, visual dashboard for hiring managers
- **User Interface & Audio Interaction**: Intuitive UI with voice input/output capabilities

### Technical Features
- **Multi-language Support**: Python, JavaScript, Java, C++
- **Real-time WebSocket Communication**: Live code analysis and AI responses
- **Voice Integration**: Speech-to-text and text-to-speech using Web Speech APIs
- **Performance Tracking**: Execution time, memory usage, complexity analysis
- **Session Playback**: Review code evolution and candidate thought process
- **Responsive Design**: Works on desktop and mobile devices

## 🏗️ Architecture

### Backend (Python/FastAPI)
- **FastAPI**: High-performance web framework
- **WebSockets**: Real-time communication
- **Google Gemini API**: AI-powered interviewer responses
- **Subprocess Execution**: Safe code execution in sandboxed environment
- **In-memory Storage**: No database required for development

### Frontend (React/TypeScript)
- **React 18**: Modern UI framework
- **Monaco Editor**: Professional code editor
- **Framer Motion**: Smooth animations
- **Web Speech APIs**: Voice interaction
- **Socket.io**: Real-time communication

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.11+
- Node.js 18+
- npm
- Gemini API Key

### 🚀 Quick Start (3 Minutes)

**Windows:**
```cmd
install.bat
start.bat
```

**macOS/Linux:**
```bash
chmod +x install.sh start.sh
./install.sh
./start.sh
```

**Manual Setup:**
```bash
python setup.py
python start.py
```

### 📖 Detailed Installation Guide

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd codesage-ai-interviewer
   ```

2. **Run the setup script**
   ```bash
   python setup.py
   ```

3. **Add your Gemini API key**
   ```bash
   # Edit backend/.env
   GEMINI_API_KEY=your_actual_gemini_api_key_here
   ```

4. **Start the application**
   ```bash
   python start.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:3000`

### Manual Setup

If the automated setup doesn't work, you can set up manually:

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env
# Edit .env with your Gemini API key
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🎯 Usage

### Starting an Interview
1. Enter your name and select difficulty level
2. Choose a category (or select "All Categories")
3. Click "Start Interview"

### During the Interview
- **Code Editor**: Write your solution in your preferred language
- **Run Code**: Execute your code and see real-time analysis
- **AI Chat**: Ask questions or get help from the AI interviewer
- **Voice Input**: Use voice commands for hands-free interaction
- **Hints**: Request progressive hints when stuck
- **Performance Panel**: Monitor your code quality and execution metrics

### Interview Features
- **Real-time Analysis**: Code is analyzed as you type
- **Adaptive Feedback**: AI responses adjust based on your performance
- **Progressive Hints**: Three levels of hints to guide you
- **Follow-up Questions**: AI asks probing questions about your approach
- **Performance Tracking**: Comprehensive metrics and scoring

## 🔧 Configuration

### Environment Variables
```bash
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
HOST=0.0.0.0
PORT=8000
DEBUG=True
CORS_ORIGINS=http://localhost:3000
CODE_TIMEOUT=5
MAX_MEMORY_MB=128
MAX_QUESTIONS=5
INTERVIEW_DURATION_MINUTES=60
```

### Supported Languages
- **Python**: Full support with syntax highlighting
- **JavaScript**: Node.js execution
- **Java**: Compilation and execution
- **C++**: GCC compilation and execution

## 📊 Evaluation Metrics

The system evaluates candidates on multiple dimensions:

- **Conversational Intelligence & Adaptivity** (30%)
- **Quality of Analysis & Feedback** (25%)
- **Performance & System Reliability** (20%)
- **User Experience** (15%)
- **Innovation & Creativity** (10%)

## 🎥 Demo Script

1. **Introduction** (30 seconds)
   - Show the home page
   - Explain the AI interviewer concept
   - Start a new interview

2. **Interview Experience** (2 minutes)
   - Demonstrate real-time code analysis
   - Show AI responses and hints
   - Use voice input/output
   - Display performance metrics

3. **Advanced Features** (30 seconds)
   - Show session playback
   - Generate performance report
   - Demonstrate multi-language support

## 🚀 Deployment

### Production Deployment
1. Set up a production server
2. Install Python 3.11+ and Node.js 18+
3. Clone the repository
4. Run setup script
5. Configure environment variables
6. Use a process manager like PM2 or systemd
7. Set up reverse proxy (nginx)

### Docker Deployment (Optional)
```bash
# Build and run with Docker Compose
docker-compose up --build
```

## 📚 User Guides

### 📖 Complete Documentation
- **[Comprehensive User Guide](COMPREHENSIVE_USER_GUIDE.md)** - Complete installation and usage guide
- **[Quick Reference Card](QUICK_REFERENCE.md)** - Essential commands and troubleshooting
- **[Installation Guide](INSTALLATION_GUIDE.md)** - Platform-specific installation instructions
- **[Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md)** - Common issues and solutions
- **[API Documentation](http://localhost:8000/docs)** - Interactive API documentation

### 🚀 Quick Start Options
1. **Universal Setup**: `python setup.py` (works on all platforms)
2. **Platform Scripts**: `install.sh` (macOS/Linux) or `install.bat` (Windows)
3. **Manual Setup**: Follow the detailed guide in COMPREHENSIVE_USER_GUIDE.md

### 🆘 Getting Help
- **Quick Issues**: Check [Quick Reference Card](QUICK_REFERENCE.md)
- **Installation Problems**: See [Installation Guide](INSTALLATION_GUIDE.md)
- **System Issues**: Consult [Troubleshooting Guide](TROUBLESHOOTING_GUIDE.md)
- **Health Check**: Visit http://localhost:8000/health
- **API Reference**: http://localhost:8000/docs

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is built for the Eightfold AI × ArIES Hackathon.

## 🏆 Hackathon Submission

### Submission Package
1. **Web Application URL**: Working interface for manual testing
2. **API Documentation**: OpenAPI spec with example calls
3. **Demo Video**: 3-minute recording following the demo script
4. **Source Code**: Complete GitHub repository

### Key Features Demonstrated
- Real-time code analysis and feedback
- AI-powered adaptive questioning
- Voice interaction capabilities
- Comprehensive performance reporting
- Multi-language support
- Professional UI/UX

## 🆘 Troubleshooting

### Common Issues
1. **Gemini API Key Error**: Ensure the API key is correctly set in `backend/.env`
2. **Port Already in Use**: Change ports in configuration
3. **Voice Not Working**: Ensure HTTPS or localhost for Web Speech APIs
4. **Code Execution Fails**: Check if required compilers are installed

### Support
For issues and questions, please check the troubleshooting section or create an issue in the repository.

---

**Built with ❤️ for the Eightfold AI × ArIES Hackathon**
