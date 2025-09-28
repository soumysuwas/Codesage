#!/usr/bin/env python3
"""
CodeSage AI Technical Interviewer Setup Script
Automatically sets up the development environment for both backend and frontend
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, cwd=None, check=True):
    """Run a command and return success status"""
    try:
        print(f"Running: {command}")
        result = subprocess.run(command, shell=True, cwd=cwd, check=check, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        if e.stderr:
            print(f"Error output: {e.stderr}")
        return False

def check_requirements():
    """Check if required tools are installed"""
    print("🔍 Checking system requirements...")
    
    # Check Python
    if not run_command("python --version", check=False):
        print("❌ Python not found. Please install Python 3.11+")
        return False
    else:
        print("✅ Python found")
    
    # Check Node.js
    if not run_command("node --version", check=False):
        print("❌ Node.js not found. Please install Node.js 18+")
        return False
    else:
        print("✅ Node.js found")
    
    # Check npm
    if not run_command("npm --version", check=False):
        print("❌ npm not found. Please install npm")
        return False
    else:
        print("✅ npm found")
    
    return True

def setup_backend():
    """Setup Python backend"""
    print("\n🐍 Setting up Python backend...")
    
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found")
        return False
    
    # Create virtual environment
    print("Creating virtual environment...")
    if not run_command("python -m venv venv", cwd=backend_dir):
        print("❌ Failed to create virtual environment")
        return False
    
    # Determine activation script based on OS
    if os.name == 'nt':  # Windows
        activate_script = "venv\\Scripts\\activate"
        pip_command = "venv\\Scripts\\pip"
    else:  # Unix/Linux/macOS
        activate_script = "venv/bin/activate"
        pip_command = "venv/bin/pip"
    
    # Install dependencies
    print("Installing Python dependencies...")
    if not run_command(f"{pip_command} install --upgrade pip", cwd=backend_dir):
        print("❌ Failed to upgrade pip")
        return False
    
    if not run_command(f"{pip_command} install -r requirements.txt", cwd=backend_dir):
        print("❌ Failed to install Python dependencies")
        return False
    
    print("✅ Backend setup complete")
    return True

def setup_frontend():
    """Setup React frontend"""
    print("\n⚛️ Setting up React frontend...")
    
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found")
        return False
    
    # Install dependencies
    print("Installing Node.js dependencies...")
    if not run_command("npm install", cwd=frontend_dir):
        print("❌ Failed to install Node.js dependencies")
        return False
    
    print("✅ Frontend setup complete")
    return True

def create_env_file():
    """Create environment file"""
    print("\n📝 Creating environment file...")
    
    env_content = """# Gemini API Configuration (REQUIRED)
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
"""
    
    env_file = Path("backend/.env")
    try:
        with open(env_file, "w") as f:
            f.write(env_content)
        print(f"✅ Environment file created at {env_file}")
        print("🔑 Please add your Gemini API key to backend/.env")
    except Exception as e:
        print(f"❌ Failed to create environment file: {e}")
        return False
    
    return True

def create_start_script():
    """Create start script"""
    print("\n📜 Creating start script...")
    
    start_script_content = """#!/usr/bin/env python3
import subprocess
import sys
import os
import time
import threading
from pathlib import Path

def run_backend():
    \"\"\"Run backend server\"\"\"
    os.chdir("backend")
    if os.name == 'nt':  # Windows
        subprocess.run(["venv\\\\Scripts\\\\python", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])
    else:  # Unix/Linux/macOS
        subprocess.run(["venv/bin/python", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

def run_frontend():
    \"\"\"Run frontend server\"\"\"
    os.chdir("frontend")
    subprocess.run(["npm", "run", "dev"])

def main():
    \"\"\"Start both servers\"\"\"
    print("🚀 Starting CodeSage AI Technical Interviewer...")
    print("Backend: http://localhost:8000")
    print("Frontend: http://localhost:3000")
    print("Press Ctrl+C to stop both servers")
    
    # Check if .env exists
    if not Path("backend/.env").exists():
        print("❌ Environment file not found. Please run setup.py first")
        return
    
    # Start backend in separate thread
    backend_thread = threading.Thread(target=run_backend)
    backend_thread.daemon = True
    backend_thread.start()
    
    # Wait a bit for backend to start
    time.sleep(3)
    
    # Start frontend
    try:
        run_frontend()
    except KeyboardInterrupt:
        print("\\n🛑 Stopping servers...")
        sys.exit(0)

if __name__ == "__main__":
    main()
"""
    
    try:
        with open("start.py", "w") as f:
            f.write(start_script_content)
        
        # Make it executable on Unix systems
        if os.name != 'nt':
            os.chmod("start.py", 0o755)
        
        print("✅ Start script created")
    except Exception as e:
        print(f"❌ Failed to create start script: {e}")
        return False
    
    return True

def main():
    """Main setup function"""
    print("🚀 Setting up CodeSage AI Technical Interviewer...")
    print("=" * 60)
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Setup failed. Please install required tools and try again.")
        return False
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed")
        return False
    
    # Setup frontend
    if not setup_frontend():
        print("\n❌ Frontend setup failed")
        return False
    
    # Create environment file
    if not create_env_file():
        print("\n❌ Environment file creation failed")
        return False
    
    # Create start script
    if not create_start_script():
        print("\n❌ Start script creation failed")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("1. Add your Gemini API key to backend/.env")
    print("2. Run: python start.py")
    print("3. Open http://localhost:3000 in your browser")
    print("\n🔧 Manual setup if needed:")
    print("- Backend: cd backend && venv/bin/python -m uvicorn app.main:app --reload")
    print("- Frontend: cd frontend && npm run dev")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
