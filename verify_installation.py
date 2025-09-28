#!/usr/bin/env python3
"""
CodeSage Installation Verification Script
Checks if all prerequisites and dependencies are properly installed
"""

import sys
import subprocess
import os
import json
import requests
from pathlib import Path

def print_status(message, status="INFO"):
    """Print status message with color coding"""
    colors = {
        "INFO": "\033[94m",      # Blue
        "SUCCESS": "\033[92m",   # Green
        "WARNING": "\033[93m",   # Yellow
        "ERROR": "\033[91m",     # Red
        "RESET": "\033[0m"       # Reset
    }
    
    symbols = {
        "INFO": "ℹ️",
        "SUCCESS": "✅",
        "WARNING": "⚠️",
        "ERROR": "❌"
    }
    
    print(f"{colors.get(status, '')}{symbols.get(status, '')} {message}{colors['RESET']}")

def check_python():
    """Check Python installation and version"""
    try:
        version = sys.version_info
        if version.major >= 3 and version.minor >= 8:
            print_status(f"Python {version.major}.{version.minor}.{version.micro} - OK", "SUCCESS")
            return True
        else:
            print_status(f"Python {version.major}.{version.minor}.{version.micro} - Version too old (need 3.8+)", "ERROR")
            return False
    except Exception as e:
        print_status(f"Python check failed: {e}", "ERROR")
        return False

def check_node():
    """Check Node.js installation and version"""
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip().lstrip('v')
            major, minor = map(int, version.split('.')[:2])
            if major >= 16:
                print_status(f"Node.js {version} - OK", "SUCCESS")
                return True
            else:
                print_status(f"Node.js {version} - Version too old (need 16+)", "ERROR")
                return False
        else:
            print_status("Node.js not found", "ERROR")
            return False
    except FileNotFoundError:
        print_status("Node.js not found", "ERROR")
        return False
    except Exception as e:
        print_status(f"Node.js check failed: {e}", "ERROR")
        return False

def check_npm():
    """Check npm installation"""
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print_status(f"npm {version} - OK", "SUCCESS")
            return True
        else:
            print_status("npm not found", "ERROR")
            return False
    except FileNotFoundError:
        print_status("npm not found", "ERROR")
        return False
    except Exception as e:
        print_status(f"npm check failed: {e}", "ERROR")
        return False

def check_git():
    """Check Git installation"""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        if result.returncode == 0:
            version = result.stdout.strip()
            print_status(f"Git {version} - OK", "SUCCESS")
            return True
        else:
            print_status("Git not found", "ERROR")
            return False
    except FileNotFoundError:
        print_status("Git not found", "ERROR")
        return False
    except Exception as e:
        print_status(f"Git check failed: {e}", "ERROR")
        return False

def check_backend_dependencies():
    """Check if backend dependencies are installed"""
    backend_path = Path("backend")
    if not backend_path.exists():
        print_status("Backend directory not found", "ERROR")
        return False
    
    venv_path = backend_path / "venv"
    if not venv_path.exists():
        print_status("Backend virtual environment not found", "ERROR")
        return False
    
    # Check if requirements.txt exists
    requirements_path = backend_path / "requirements.txt"
    if not requirements_path.exists():
        print_status("Backend requirements.txt not found", "ERROR")
        return False
    
    # Try to import key packages
    try:
        if sys.platform == "win32":
            python_exe = venv_path / "Scripts" / "python.exe"
        else:
            python_exe = venv_path / "bin" / "python"
        
        if not python_exe.exists():
            print_status("Backend Python executable not found", "ERROR")
            return False
        
        # Test importing key packages
        test_imports = [
            "fastapi",
            "uvicorn", 
            "websockets",
            "google.generativeai",
            "pydantic"
        ]
        
        for package in test_imports:
            result = subprocess.run([
                str(python_exe), "-c", f"import {package}"
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print_status(f"Backend package {package} not installed", "ERROR")
                return False
        
        print_status("Backend dependencies - OK", "SUCCESS")
        return True
        
    except Exception as e:
        print_status(f"Backend dependency check failed: {e}", "ERROR")
        return False

def check_frontend_dependencies():
    """Check if frontend dependencies are installed"""
    frontend_path = Path("frontend")
    if not frontend_path.exists():
        print_status("Frontend directory not found", "ERROR")
        return False
    
    node_modules_path = frontend_path / "node_modules"
    if not node_modules_path.exists():
        print_status("Frontend node_modules not found", "ERROR")
        return False
    
    package_json_path = frontend_path / "package.json"
    if not package_json_path.exists():
        print_status("Frontend package.json not found", "ERROR")
        return False
    
    # Check if key packages are installed
    try:
        with open(package_json_path, 'r') as f:
            package_data = json.load(f)
        
        dependencies = package_data.get('dependencies', {})
        dev_dependencies = package_data.get('devDependencies', {})
        
        key_packages = ['react', 'react-dom', 'vite', 'typescript']
        
        for package in key_packages:
            if package not in dependencies and package not in dev_dependencies:
                print_status(f"Frontend package {package} not found in package.json", "WARNING")
        
        print_status("Frontend dependencies - OK", "SUCCESS")
        return True
        
    except Exception as e:
        print_status(f"Frontend dependency check failed: {e}", "ERROR")
        return False

def check_environment_config():
    """Check if environment is properly configured"""
    backend_path = Path("backend")
    env_path = backend_path / ".env"
    
    if not env_path.exists():
        print_status("Backend .env file not found", "WARNING")
        return False
    
    try:
        with open(env_path, 'r') as f:
            env_content = f.read()
        
        if "GEMINI_API_KEY" not in env_content:
            print_status("GEMINI_API_KEY not found in .env file", "WARNING")
            return False
        
        if "GEMINI_API_KEY=your_gemini_api_key_here" in env_content:
            print_status("GEMINI_API_KEY not configured (still has placeholder)", "WARNING")
            return False
        
        print_status("Environment configuration - OK", "SUCCESS")
        return True
        
    except Exception as e:
        print_status(f"Environment check failed: {e}", "ERROR")
        return False

def check_ports():
    """Check if required ports are available"""
    import socket
    
    ports_to_check = [3000, 8000]
    available_ports = []
    
    for port in ports_to_check:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
                available_ports.append(port)
        except OSError:
            print_status(f"Port {port} is already in use", "WARNING")
    
    if len(available_ports) == len(ports_to_check):
        print_status("All required ports are available", "SUCCESS")
        return True
    else:
        print_status(f"Only {len(available_ports)}/{len(ports_to_check)} ports are available", "WARNING")
        return False

def check_services():
    """Check if services are currently running"""
    try:
        # Check backend
        backend_running = False
        try:
            response = requests.get("http://localhost:8000/health", timeout=5)
            if response.status_code == 200:
                backend_running = True
                print_status("Backend service is running", "SUCCESS")
        except:
            print_status("Backend service is not running", "INFO")
        
        # Check frontend
        frontend_running = False
        try:
            response = requests.get("http://localhost:3000", timeout=5)
            if response.status_code == 200:
                frontend_running = True
                print_status("Frontend service is running", "SUCCESS")
        except:
            print_status("Frontend service is not running", "INFO")
        
        if backend_running and frontend_running:
            print_status("All services are running", "SUCCESS")
            return True
        else:
            print_status("Some services are not running", "INFO")
            return False
            
    except Exception as e:
        print_status(f"Service check failed: {e}", "ERROR")
        return False

def main():
    """Main verification function"""
    print("🔍 CodeSage Installation Verification")
    print("=" * 50)
    
    checks = [
        ("Python Installation", check_python),
        ("Node.js Installation", check_node),
        ("npm Installation", check_npm),
        ("Git Installation", check_git),
        ("Backend Dependencies", check_backend_dependencies),
        ("Frontend Dependencies", check_frontend_dependencies),
        ("Environment Configuration", check_environment_config),
        ("Port Availability", check_ports),
        ("Service Status", check_services)
    ]
    
    passed = 0
    total = len(checks)
    
    for check_name, check_func in checks:
        print(f"\n📋 {check_name}")
        print("-" * 30)
        if check_func():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 Verification Results: {passed}/{total} checks passed")
    
    if passed == total:
        print_status("🎉 All checks passed! Your CodeSage installation is ready.", "SUCCESS")
        print("\n🚀 To start the system:")
        print("   python start.py")
        print("\n🌐 Then open: http://localhost:3000")
    elif passed >= total - 2:
        print_status("⚠️ Most checks passed. You may have some warnings but the system should work.", "WARNING")
        print("\n🚀 To start the system:")
        print("   python start.py")
    else:
        print_status("❌ Several checks failed. Please review the issues above.", "ERROR")
        print("\n📚 For help, check:")
        print("   - COMPREHENSIVE_USER_GUIDE.md")
        print("   - TROUBLESHOOTING_GUIDE.md")
        print("   - INSTALLATION_GUIDE.md")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)