#!/usr/bin/env python3
"""
CodeSage AI Technical Interviewer Start Script
Concurrently starts both backend and frontend servers
"""

import subprocess
import sys
import os
import time
import threading
from pathlib import Path

def run_backend():
    """Run backend server"""
    os.chdir("backend")
    if os.name == 'nt':  # Windows
        subprocess.run(["venv\\Scripts\\python", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])
    else:  # Unix/Linux/macOS
        subprocess.run(["venv/bin/python", "-m", "uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"])

def run_frontend():
    """Run frontend server"""
    os.chdir("frontend")
    subprocess.run(["npm", "run", "dev"])

def main():
    """Start both servers"""
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
        print("\n🛑 Stopping servers...")
        sys.exit(0)

if __name__ == "__main__":
    main()
