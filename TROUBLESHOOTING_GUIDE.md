# 🔧 CodeSage Troubleshooting Guide

## 🚨 Quick Diagnosis

### System Status Check
```bash
# Check if services are running
ps aux | grep -E "(uvicorn|vite|node.*vite)"

# Check port usage
netstat -tulpn | grep -E ":(3000|8000)"

# Test backend health
curl -s http://localhost:8000/health

# Test frontend
curl -s http://localhost:3000 | head -5
```

---

## 🔍 Common Issues and Solutions

### 1. Port Already in Use

#### Symptoms
- `Address already in use` error
- Services fail to start
- Connection refused errors

#### Solutions
```bash
# Find processes using ports
lsof -i :3000
lsof -i :8000

# Kill processes (replace PID with actual process ID)
kill -9 <PID>

# Or kill all processes on specific ports
lsof -ti:3000 | xargs kill -9
lsof -ti:8000 | xargs kill -9

# On Windows
netstat -ano | findstr :3000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### 2. Python Dependencies Issues

#### Symptoms
- `ModuleNotFoundError`
- `ImportError`
- Package installation failures

#### Solutions
```bash
# Clear pip cache
pip cache purge

# Upgrade pip
pip install --upgrade pip

# Reinstall dependencies
cd backend
rm -rf venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt --force-reinstall

# If specific package fails
pip install <package_name> --no-cache-dir
```

### 3. Node.js Dependencies Issues

#### Symptoms
- `npm ERR!` messages
- Module not found errors
- Build failures

#### Solutions
```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and reinstall
cd frontend
rm -rf node_modules package-lock.json
npm install

# If specific package fails
npm install <package_name> --no-optional

# Check Node.js version
node --version  # Should be 16+
```

### 4. WebSocket Connection Issues

#### Symptoms
- `WebSocket connection failed`
- `403 Forbidden` errors
- AI not responding

#### Solutions
```bash
# Check if both services are running
ps aux | grep -E "(uvicorn|vite)"

# Test WebSocket manually
curl -i -N -H "Connection: Upgrade" -H "Upgrade: websocket" -H "Sec-WebSocket-Version: 13" -H "Sec-WebSocket-Key: x3JJHMbDL1EzLkh9GBhXDw==" http://localhost:8000/ws/test-connection

# Check CORS configuration
grep -r "CORS_ORIGINS" backend/

# Restart both services
pkill -f uvicorn && pkill -f vite
python start.py
```

### 5. Gemini API Issues

#### Symptoms
- `Gemini API error: 404`
- `API key not found`
- AI responses not working

#### Solutions
```bash
# Check API key configuration
cat backend/.env | grep GEMINI_API_KEY

# Verify API key format
echo $GEMINI_API_KEY

# Test API key
curl -H "Authorization: Bearer $GEMINI_API_KEY" https://generativelanguage.googleapis.com/v1beta/models

# Check API quota
# Visit: https://makersuite.google.com/app/apikey
```

### 6. Frontend Build Issues

#### Symptoms
- `TypeScript errors`
- `Build failed`
- `Module not found`

#### Solutions
```bash
# Check TypeScript configuration
cd frontend
npx tsc --noEmit

# Fix TypeScript errors
npm run build

# Clear Vite cache
rm -rf node_modules/.vite
npm run dev

# Check for missing types
npm install @types/node @types/react @types/react-dom
```

### 7. Memory Issues

#### Symptoms
- `Out of memory` errors
- Slow performance
- System crashes

#### Solutions
```bash
# Check memory usage
free -h  # Linux
vm_stat  # macOS
wmic OS get TotalVisibleMemorySize,FreePhysicalMemory /format:table  # Windows

# Increase Node.js memory limit
export NODE_OPTIONS="--max-old-space-size=4096"

# Reduce backend memory usage
# Edit backend/.env
echo "MAX_MEMORY_MB=64" >> backend/.env
```

---

## 🔧 Advanced Troubleshooting

### 1. Log Analysis

#### Backend Logs
```bash
# Enable debug logging
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --log-level debug

# Check specific log files
tail -f logs/app.log
tail -f logs/error.log
```

#### Frontend Logs
```bash
# Enable verbose logging
cd frontend
npm run dev -- --debug

# Check browser console
# Open Developer Tools (F12) and check Console tab
```

### 2. Network Troubleshooting

#### Check Network Connectivity
```bash
# Test localhost connectivity
ping localhost

# Test port accessibility
telnet localhost 3000
telnet localhost 8000

# Check firewall settings
sudo ufw status  # Ubuntu
sudo firewall-cmd --list-all  # CentOS/RHEL
```

#### Proxy Issues
```bash
# Check proxy configuration
echo $HTTP_PROXY
echo $HTTPS_PROXY

# Disable proxy for localhost
export NO_PROXY=localhost,127.0.0.1
```

### 3. System Resource Issues

#### Check System Resources
```bash
# CPU usage
top -p $(pgrep -f "uvicorn|vite")

# Memory usage
ps aux --sort=-%mem | head -10

# Disk space
df -h

# Check for zombie processes
ps aux | grep -v grep | grep -E "(uvicorn|vite)" | awk '{print $2}' | xargs ps -o pid,ppid,state
```

### 4. Configuration Issues

#### Environment Variables
```bash
# Check all environment variables
env | grep -E "(GEMINI|HOST|PORT|CORS)"

# Validate .env file
cd backend
python -c "from dotenv import load_dotenv; load_dotenv(); print('Environment loaded successfully')"
```

#### File Permissions
```bash
# Check file permissions
ls -la backend/.env
ls -la frontend/package.json

# Fix permissions
chmod 644 backend/.env
chmod 755 start.py
chmod +x *.sh
```

---

## 🚨 Emergency Recovery

### Complete System Reset
```bash
# Stop all services
pkill -f uvicorn && pkill -f vite && pkill -f node

# Clean everything
rm -rf backend/venv
rm -rf frontend/node_modules
rm -rf frontend/dist
rm -rf frontend/.vite

# Reinstall everything
python setup.py

# Restart
python start.py
```

### Backup and Restore
```bash
# Create backup
tar -czf codesage-backup-$(date +%Y%m%d).tar.gz backend/ frontend/ *.py *.sh *.md

# Restore from backup
tar -xzf codesage-backup-YYYYMMDD.tar.gz
```

---

## 📊 Diagnostic Scripts

### System Health Check
```bash
#!/bin/bash
echo "=== CodeSage System Health Check ==="

echo "1. Checking Python..."
python --version || echo "❌ Python not found"

echo "2. Checking Node.js..."
node --version || echo "❌ Node.js not found"

echo "3. Checking services..."
ps aux | grep -E "(uvicorn|vite)" | grep -v grep || echo "❌ Services not running"

echo "4. Checking ports..."
netstat -tulpn | grep -E ":(3000|8000)" || echo "❌ Ports not listening"

echo "5. Testing backend..."
curl -s http://localhost:8000/health || echo "❌ Backend not responding"

echo "6. Testing frontend..."
curl -s http://localhost:3000 | head -1 || echo "❌ Frontend not responding"

echo "=== Health Check Complete ==="
```

### Performance Monitor
```bash
#!/bin/bash
echo "=== CodeSage Performance Monitor ==="

while true; do
    echo "$(date): CPU: $(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)%, Memory: $(free | grep Mem | awk '{printf "%.1f%%", $3/$2 * 100.0}')"
    sleep 5
done
```

---

## 🆘 Getting Help

### Before Contacting Support
1. ✅ Check this troubleshooting guide
2. ✅ Run the diagnostic scripts
3. ✅ Check logs for error messages
4. ✅ Verify all prerequisites are met
5. ✅ Try the emergency recovery steps

### Information to Provide
- Operating system and version
- Python and Node.js versions
- Error messages (full text)
- Steps to reproduce the issue
- System logs
- Screenshots if applicable

### Useful Commands for Support
```bash
# System information
uname -a
python --version
node --version
npm --version

# Service status
ps aux | grep -E "(uvicorn|vite|node.*vite)"
netstat -tulpn | grep -E ":(3000|8000)"

# Error logs
tail -50 backend/logs/app.log
tail -50 frontend/logs/vite.log

# Configuration
cat backend/.env
cat frontend/package.json
```

---

## 📚 Additional Resources

- [COMPREHENSIVE_USER_GUIDE.md](COMPREHENSIVE_USER_GUIDE.md) - Complete user guide
- [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Quick reference card
- [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md) - Installation instructions
- [API Documentation](http://localhost:8000/docs) - When system is running

---

*Last updated: September 2024*
