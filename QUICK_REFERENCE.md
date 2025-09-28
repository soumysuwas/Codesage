# 🚀 CodeSage Quick Reference Card

## ⚡ Quick Start (3 Steps)
```bash
# 1. Clone and setup
git clone <repo-url> && cd suwas
python setup.py

# 2. Configure API key
echo "GEMINI_API_KEY=your_key_here" > backend/.env

# 3. Start system
python start.py
```

## 🌐 Access URLs
- **Main App**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

## 🔧 Essential Commands

### Start Services
```bash
# Universal start
python start.py

# Manual start
cd backend && venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &
cd frontend && npm run dev &
```

### Stop Services
```bash
pkill -f uvicorn && pkill -f vite
```

### Check Status
```bash
ps aux | grep -E "(uvicorn|vite)"
curl http://localhost:8000/health
```

## 🛠️ Troubleshooting

### Port Issues
```bash
# Kill processes on ports 3000/8000
lsof -ti:3000 | xargs kill -9
lsof -ti:8000 | xargs kill -9
```

### Dependencies Issues
```bash
# Backend
cd backend && pip install -r requirements.txt --force-reinstall

# Frontend
cd frontend && rm -rf node_modules && npm install
```

### WebSocket Issues
- Ensure both services are running
- Check firewall settings
- Verify CORS configuration

## 📋 Prerequisites Checklist
- [ ] Python 3.8+
- [ ] Node.js 16+
- [ ] Git
- [ ] Gemini API Key
- [ ] 4GB+ RAM
- [ ] Internet connection

## 🔑 Environment Variables
```bash
# Required in backend/.env
GEMINI_API_KEY=your_gemini_api_key_here
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:3000
```

## 🎯 Key Features
- ✅ Real-time code analysis
- ✅ AI-powered interviewing
- ✅ Multi-language support (Python, JS, Java, C++)
- ✅ Voice input/output
- ✅ Progressive hints system
- ✅ Performance tracking
- ✅ Session management

## 📞 Quick Help
1. Check logs: `tail -f backend/logs/app.log`
2. Verify installation: `python verify_installation.py`
3. Test connection: Open http://localhost:3000/test_connection.html
4. Check API: `curl http://localhost:8000/health`

---
*For detailed information, see COMPREHENSIVE_USER_GUIDE.md*
