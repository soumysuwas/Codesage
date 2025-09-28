@echo off
REM CodeSage AI Technical Interviewer - Windows Installation Script
REM This script automatically installs all dependencies and sets up the system

echo.
echo 🚀 CodeSage AI Technical Interviewer - Installation Script
echo ==========================================================
echo.

REM Check if Python is installed
echo ℹ️  Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found
    echo ℹ️  Please install Python 3.11+ from https://www.python.org/downloads/
    echo ℹ️  Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
) else (
    echo ✅ Python found
)

REM Check if Node.js is installed
echo ℹ️  Checking Node.js installation...
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js not found
    echo ℹ️  Please install Node.js 18+ from https://nodejs.org/
    pause
    exit /b 1
) else (
    echo ✅ Node.js found
)

REM Check if npm is installed
echo ℹ️  Checking npm installation...
npm --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ npm not found
    echo ℹ️  Please install npm (usually comes with Node.js)
    pause
    exit /b 1
) else (
    echo ✅ npm found
)

echo.
echo ℹ️  Setting up Python backend...

REM Navigate to backend directory
cd backend

REM Create virtual environment
echo ℹ️  Creating Python virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment
echo ℹ️  Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ℹ️  Upgrading pip...
python -m pip install --upgrade pip

REM Install Python dependencies
echo ℹ️  Installing Python dependencies...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install Python dependencies
    pause
    exit /b 1
)

REM Create .env file if it doesn't exist
if not exist .env (
    echo ℹ️  Creating environment configuration...
    (
        echo # Gemini API Configuration (REQUIRED^)
        echo GEMINI_API_KEY=your_gemini_api_key_here
        echo.
        echo # Server Configuration
        echo HOST=0.0.0.0
        echo PORT=8000
        echo DEBUG=True
        echo.
        echo # CORS Configuration
        echo CORS_ORIGINS=http://localhost:3000
        echo.
        echo # Security
        echo SECRET_KEY=your-secret-key-change-this
        echo.
        echo # Code Execution
        echo CODE_TIMEOUT=5
        echo MAX_MEMORY_MB=128
        echo.
        echo # Interview Configuration
        echo MAX_QUESTIONS=5
        echo INTERVIEW_DURATION_MINUTES=60
    ) > .env
    echo ✅ Environment file created at backend\.env
) else (
    echo ✅ Environment file already exists
)

REM Go back to root directory
cd ..

echo.
echo ℹ️  Setting up Node.js frontend...

REM Navigate to frontend directory
cd frontend

REM Install Node.js dependencies
echo ℹ️  Installing Node.js dependencies...
npm install
if %errorlevel% neq 0 (
    echo ❌ Failed to install Node.js dependencies
    pause
    exit /b 1
)

REM Go back to root directory
cd ..

echo.
echo ℹ️  Creating start script...

REM Create start.bat file
(
    echo @echo off
    echo REM CodeSage AI Technical Interviewer - Start Script
    echo echo 🚀 Starting CodeSage AI Technical Interviewer...
    echo.
    echo REM Check if .env exists
    echo if not exist backend\.env ^(
    echo     echo ❌ Environment file not found. Please run install.bat first
    echo     pause
    echo     exit /b 1
    echo ^)
    echo.
    echo REM Start backend in background
    echo echo Starting backend server...
    echo cd backend
    echo call venv\Scripts\activate.bat
    echo start /B python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
    echo.
    echo REM Wait for backend to start
    echo timeout /t 3 /nobreak ^>nul
    echo.
    echo REM Start frontend
    echo echo Starting frontend server...
    echo cd ..\frontend
    echo start /B npm run dev
    echo.
    echo echo.
    echo echo 🎉 CodeSage is running!
    echo echo Frontend: http://localhost:3000
    echo echo Backend: http://localhost:8000
    echo echo API Docs: http://localhost:8000/docs
    echo echo.
    echo echo Press any key to stop both servers
    echo pause ^>nul
    echo.
    echo REM Stop all Python and Node processes
    echo taskkill /f /im python.exe ^>nul 2^>^&1
    echo taskkill /f /im node.exe ^>nul 2^>^&1
    echo echo 🛑 Servers stopped
) > start.bat

echo ✅ Start script created

echo.
echo ==========================================================
echo ✅ Installation complete!
echo.
echo ℹ️  Next steps:
echo 1. Add your Gemini API key to backend\.env
echo 2. Run: start.bat
echo 3. Open http://localhost:3000 in your browser
echo.
echo ⚠️  Important: You need a Gemini API key for AI features to work
echo ℹ️  Get your API key from: https://makersuite.google.com/app/apikey
echo.
echo ℹ️  For detailed instructions, see USER_GUIDE.md
echo ==========================================================
echo.
pause
