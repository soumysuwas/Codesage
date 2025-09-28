# 📦 CodeSage Installation Guide

## 🖥️ Platform-Specific Instructions

### Windows Installation

#### Prerequisites
1. **Python 3.8+**
   - Download from [python.org](https://www.python.org/downloads/)
   - ✅ Check "Add Python to PATH" during installation
   - Verify: `python --version`

2. **Node.js 16+**
   - Download from [nodejs.org](https://nodejs.org/)
   - Choose LTS version
   - Verify: `node --version` and `npm --version`

3. **Git**
   - Download from [git-scm.com](https://git-scm.com/)
   - Verify: `git --version`

#### Installation Steps
```cmd
# 1. Clone repository
git clone <repository-url>
cd suwas

# 2. Run Windows installer
install.bat

# 3. Configure environment
cd backend
echo GEMINI_API_KEY=your_key_here > .env

# 4. Start system
python start.py
```

#### Manual Windows Setup
```cmd
# Backend setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup
cd ..\frontend
npm install

# Start services
cd ..\backend
venv\Scripts\activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# In new terminal
cd frontend
npm run dev
```

---

### macOS Installation

#### Prerequisites
1. **Homebrew** (if not installed)
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Python 3.8+**
   ```bash
   brew install python
   python3 --version
   ```

3. **Node.js 16+**
   ```bash
   brew install node
   node --version
   npm --version
   ```

4. **Git**
   ```bash
   brew install git
   git --version
   ```

#### Installation Steps
```bash
# 1. Clone repository
git clone <repository-url>
cd suwas

# 2. Run macOS installer
chmod +x install.sh
./install.sh

# 3. Configure environment
cd backend
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Start system
python start.py
```

#### Manual macOS Setup
```bash
# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Start services
cd ../backend
source venv/bin/activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &

# In new terminal
cd frontend
npm run dev
```

---

### Linux (Ubuntu/Debian) Installation

#### Prerequisites
```bash
# Update package list
sudo apt update

# Install Python 3.8+
sudo apt install python3 python3-pip python3-venv

# Install Node.js 16+
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs

# Install Git
sudo apt install git

# Verify installations
python3 --version
node --version
npm --version
git --version
```

#### Installation Steps
```bash
# 1. Clone repository
git clone <repository-url>
cd suwas

# 2. Run Linux installer
chmod +x install.sh
./install.sh

# 3. Configure environment
cd backend
echo "GEMINI_API_KEY=your_key_here" > .env

# 4. Start system
python3 start.py
```

#### Manual Linux Setup
```bash
# Backend setup
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Frontend setup
cd ../frontend
npm install

# Start services
cd ../backend
source venv/bin/activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload &

# In new terminal
cd frontend
npm run dev
```

---

## 🔧 Docker Installation (Alternative)

### Prerequisites
- Docker Desktop installed
- Docker Compose installed

### Docker Setup
```bash
# 1. Clone repository
git clone <repository-url>
cd suwas

# 2. Create docker-compose.yml
cat > docker-compose.yml << EOF
version: '3.8'
services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    environment:
      - GEMINI_API_KEY=your_key_here
    volumes:
      - ./backend:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    volumes:
      - ./frontend:/app
    command: npm run dev
    depends_on:
      - backend
EOF

# 3. Start with Docker
docker-compose up --build
```

---

## 🐳 Container Installation

### Using Dockerfile

#### Backend Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### Frontend Dockerfile
```dockerfile
FROM node:16-alpine

WORKDIR /app
COPY package*.json ./
RUN npm install

COPY . .
EXPOSE 3000

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
```

---

## 🔍 Verification Steps

### 1. Check Prerequisites
```bash
# Python
python --version  # Should be 3.8+

# Node.js
node --version    # Should be 16+

# Git
git --version     # Any recent version
```

### 2. Verify Installation
```bash
# Run verification script
python verify_installation.py
```

### 3. Test Services
```bash
# Test backend
curl http://localhost:8000/health

# Test frontend
curl http://localhost:3000

# Test WebSocket
# Open http://localhost:3000/test_connection.html
```

---

## 🚨 Common Installation Issues

### Python Issues
```bash
# Python not found
export PATH="/usr/local/bin:$PATH"

# Permission denied
sudo chown -R $USER:$USER ~/.local

# Virtual environment issues
python -m venv --clear venv
```

### Node.js Issues
```bash
# npm permission issues
sudo chown -R $USER:$USER ~/.npm

# Clear npm cache
npm cache clean --force

# Node version issues
nvm install 16
nvm use 16
```

### Port Issues
```bash
# Check port usage
netstat -tulpn | grep -E ":(3000|8000)"

# Kill processes
sudo kill -9 $(lsof -ti:3000)
sudo kill -9 $(lsof -ti:8000)
```

### Permission Issues
```bash
# Make scripts executable
chmod +x *.sh
chmod +x *.py

# Fix ownership
sudo chown -R $USER:$USER .
```

---

## 📋 Post-Installation Checklist

- [ ] All prerequisites installed
- [ ] Repository cloned
- [ ] Dependencies installed (backend & frontend)
- [ ] Environment variables configured
- [ ] Gemini API key set
- [ ] Services can start without errors
- [ ] Frontend accessible at http://localhost:3000
- [ ] Backend accessible at http://localhost:8000
- [ ] WebSocket connection working
- [ ] AI responses functioning

---

## 🆘 Getting Help

### Before Asking for Help
1. Check this installation guide
2. Run `python verify_installation.py`
3. Check logs for error messages
4. Verify all prerequisites are met

### Useful Commands for Debugging
```bash
# Check system info
uname -a
python --version
node --version
npm --version

# Check running processes
ps aux | grep -E "(python|node|uvicorn|vite)"

# Check network
netstat -tulpn | grep -E ":(3000|8000)"

# Check logs
tail -f backend/logs/app.log
```

---

*For detailed usage instructions, see COMPREHENSIVE_USER_GUIDE.md*
