# CodeSage AI Technical Interviewer - Installation Guides

## 📚 Complete Guide Collection

This document provides an overview of all available installation and user guides for the CodeSage AI Technical Interviewer system.

---
 
## 🚀 Quick Start (3 Minutes)

### For Impatient Users
- **[QUICK_START.md](QUICK_START.md)** - Get up and running in 3 minutes
- **One-Click Install**: `install.sh` (macOS/Linux) or `install.bat` (Windows)
- **One-Click Start**: `start.sh` (macOS/Linux) or `start.bat` (Windows)

---

## 📖 Comprehensive Guides

### 1. Complete User Guide
- **[USER_GUIDE.md](USER_GUIDE.md)** - Comprehensive installation and usage guide
- **Includes**: Detailed installation steps, troubleshooting, feature explanations
- **For**: Users who want complete understanding of the system

### 2. Quick Start Guide
- **[QUICK_START.md](QUICK_START.md)** - Minimal steps to get started
- **Includes**: Essential installation steps, basic usage
- **For**: Users who want to get started quickly

---

## 🛠️ Installation Methods

### Method 1: One-Click Installation (Recommended)
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

### Method 2: Automated Python Setup
```bash
python setup.py
python start.py
```

### Method 3: Manual Installation
Follow the detailed steps in [USER_GUIDE.md](USER_GUIDE.md)

---

## 🔍 Verification & Troubleshooting

### Installation Verification
```bash
python verify_installation.py
```
This script checks:
- Python 3.11+ installation
- Node.js 18+ installation
- Backend dependencies
- Frontend dependencies
- Environment configuration
- Server startup capability

### Health Checks
- **System Health**: http://localhost:8000/health
- **API Documentation**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000

---

## 📋 System Requirements

### Minimum Requirements
- **OS**: Windows 10+, macOS 10.15+, Ubuntu 18.04+
- **Python**: 3.11+
- **Node.js**: 18+
- **RAM**: 4GB (8GB recommended)
- **Storage**: 2GB free space
- **Internet**: Required for AI features

### Required Tools
- **Python**: [Download](https://www.python.org/downloads/)
- **Node.js**: [Download](https://nodejs.org/)
- **Git**: [Download](https://git-scm.com/downloads)
- **Gemini API Key**: [Get API Key](https://makersuite.google.com/app/apikey)

---

## 🎯 Usage Guides

### Basic Usage
1. **Create Interview**: Enter candidate name, select difficulty
2. **Code**: Write code in Python, JavaScript, Java, or C++
3. **Get Feedback**: Receive real-time AI analysis and hints
4. **Voice Interaction**: Use voice input/output features
5. **View Reports**: See comprehensive performance analysis

### Advanced Features
- **Multi-language Support**: Python, JavaScript, Java, C++
- **Real-time Analysis**: Syntax, runtime, complexity, quality
- **AI Interviewer**: Adaptive responses and progressive hints
- **Voice Features**: Speech-to-text and text-to-speech
- **Performance Tracking**: Live metrics and reporting

---

## 🆘 Support & Help

### Getting Help
1. **Check Health**: http://localhost:8000/health
2. **Read Guides**: Start with QUICK_START.md
3. **Verify Installation**: Run `python verify_installation.py`
4. **Check Logs**: Review terminal output for errors
5. **API Docs**: Visit http://localhost:8000/docs

### Common Issues
- **Python not found**: Install Python 3.11+ and add to PATH
- **Node.js not found**: Install Node.js 18+ from nodejs.org
- **Port in use**: Close other applications using ports 3000/8000
- **API errors**: Check Gemini API key in backend/.env
- **Build failures**: Run `python setup.py` to reinstall dependencies

---

## 📁 File Structure

```
CodeSage/
├── install.sh              # macOS/Linux installation script
├── install.bat             # Windows installation script
├── start.sh                # macOS/Linux start script
├── start.bat               # Windows start script
├── setup.py                # Python setup script
├── verify_installation.py  # Installation verification
├── USER_GUIDE.md           # Comprehensive user guide
├── QUICK_START.md          # Quick start guide
├── INSTALLATION_GUIDES.md  # This file
├── README.md               # Main project documentation
├── backend/                # Python backend
└── frontend/               # React frontend
```

---

## 🎉 Success Indicators

### Installation Complete When:
- ✅ All dependencies installed
- ✅ Environment file configured
- ✅ Backend server starts without errors
- ✅ Frontend builds successfully
- ✅ Health check returns OK
- ✅ Can access http://localhost:3000

### Ready to Use When:
- ✅ Can create an interview
- ✅ Code editor loads properly
- ✅ AI responses work (with valid API key)
- ✅ Voice features work (on localhost/HTTPS)
- ✅ Real-time analysis functions

---

## 🚀 Next Steps After Installation

1. **Get Gemini API Key**: https://makersuite.google.com/app/apikey
2. **Configure API Key**: Edit `backend/.env`
3. **Start Application**: Run start script
4. **Open Browser**: Go to http://localhost:3000
5. **Create Interview**: Test the system
6. **Explore Features**: Try voice, different languages, hints

---

**Happy Interviewing!** 🎯
