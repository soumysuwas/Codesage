#!/bin/bash

# CodeSage AI Technical Interviewer - One-Click Installation Script
# This script automatically installs all dependencies and sets up the system

set -e  # Exit on any error

echo "🚀 CodeSage AI Technical Interviewer - Installation Script"
echo "=========================================================="

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if running on supported OS
check_os() {
    print_info "Checking operating system..."
    
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="linux"
        print_status "Linux detected"
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macos"
        print_status "macOS detected"
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        OS="windows"
        print_status "Windows detected (Git Bash)"
    else
        print_error "Unsupported operating system: $OSTYPE"
        print_info "Supported systems: Linux, macOS, Windows (with Git Bash)"
        exit 1
    fi
}

# Check if required tools are installed
check_dependencies() {
    print_info "Checking system dependencies..."
    
    # Check Python
    if command -v python3 &> /dev/null; then
        PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
        if [[ $(echo "$PYTHON_VERSION >= 3.11" | bc -l) -eq 1 ]]; then
            print_status "Python $PYTHON_VERSION found"
        else
            print_error "Python 3.11+ required, found $PYTHON_VERSION"
            print_info "Please install Python 3.11+ from https://www.python.org/downloads/"
            exit 1
        fi
    else
        print_error "Python not found"
        print_info "Please install Python 3.11+ from https://www.python.org/downloads/"
        exit 1
    fi
    
    # Check Node.js
    if command -v node &> /dev/null; then
        NODE_VERSION=$(node --version | cut -d'v' -f2 | cut -d'.' -f1)
        if [[ $NODE_VERSION -ge 18 ]]; then
            print_status "Node.js $(node --version) found"
        else
            print_error "Node.js 18+ required, found $(node --version)"
            print_info "Please install Node.js 18+ from https://nodejs.org/"
            exit 1
        fi
    else
        print_error "Node.js not found"
        print_info "Please install Node.js 18+ from https://nodejs.org/"
        exit 1
    fi
    
    # Check npm
    if command -v npm &> /dev/null; then
        print_status "npm $(npm --version) found"
    else
        print_error "npm not found"
        print_info "Please install npm (usually comes with Node.js)"
        exit 1
    fi
    
    # Check Git
    if command -v git &> /dev/null; then
        print_status "Git $(git --version | cut -d' ' -f3) found"
    else
        print_warning "Git not found (optional but recommended)"
    fi
}

# Install system dependencies based on OS
install_system_dependencies() {
    print_info "Installing system dependencies..."
    
    if [[ "$OS" == "linux" ]]; then
        # Detect Linux distribution
        if command -v apt &> /dev/null; then
            print_info "Installing dependencies via apt..."
            sudo apt update
            sudo apt install -y python3-venv python3-pip nodejs npm git curl
        elif command -v yum &> /dev/null; then
            print_info "Installing dependencies via yum..."
            sudo yum install -y python3 python3-pip nodejs npm git curl
        elif command -v dnf &> /dev/null; then
            print_info "Installing dependencies via dnf..."
            sudo dnf install -y python3 python3-pip nodejs npm git curl
        else
            print_warning "Package manager not detected. Please install dependencies manually."
        fi
    elif [[ "$OS" == "macos" ]]; then
        if command -v brew &> /dev/null; then
            print_info "Installing dependencies via Homebrew..."
            brew install python@3.11 node git
        else
            print_warning "Homebrew not found. Please install dependencies manually."
            print_info "Install Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        fi
    fi
}

# Setup Python backend
setup_backend() {
    print_info "Setting up Python backend..."
    
    cd backend
    
    # Create virtual environment
    print_info "Creating Python virtual environment..."
    python3 -m venv venv
    
    # Activate virtual environment
    print_info "Activating virtual environment..."
    source venv/bin/activate
    
    # Upgrade pip
    print_info "Upgrading pip..."
    pip install --upgrade pip
    
    # Install Python dependencies
    print_info "Installing Python dependencies..."
    pip install -r requirements.txt
    
    # Create .env file if it doesn't exist
    if [[ ! -f .env ]]; then
        print_info "Creating environment configuration..."
        cat > .env << EOF
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
EOF
        print_status "Environment file created at backend/.env"
    else
        print_status "Environment file already exists"
    fi
    
    cd ..
    print_status "Backend setup complete"
}

# Setup Node.js frontend
setup_frontend() {
    print_info "Setting up Node.js frontend..."
    
    cd frontend
    
    # Install Node.js dependencies
    print_info "Installing Node.js dependencies..."
    npm install
    
    cd ..
    print_status "Frontend setup complete"
}

# Create start script
create_start_script() {
    print_info "Creating start script..."
    
    cat > start.sh << 'EOF'
#!/bin/bash

# CodeSage AI Technical Interviewer - Start Script
echo "🚀 Starting CodeSage AI Technical Interviewer..."

# Check if .env exists
if [[ ! -f backend/.env ]]; then
    echo "❌ Environment file not found. Please run install.sh first"
    exit 1
fi

# Start backend in background
echo "Starting backend server..."
cd backend
source venv/bin/activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!

# Wait for backend to start
sleep 3

# Start frontend
echo "Starting frontend server..."
cd ../frontend
npm run dev &
FRONTEND_PID=$!

echo ""
echo "🎉 CodeSage is running!"
echo "Frontend: http://localhost:3000"
echo "Backend: http://localhost:8000"
echo "API Docs: http://localhost:8000/docs"
echo ""
echo "Press Ctrl+C to stop both servers"

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Stopping servers..."
    kill $BACKEND_PID 2>/dev/null
    kill $FRONTEND_PID 2>/dev/null
    exit 0
}

# Set trap to cleanup on script exit
trap cleanup SIGINT SIGTERM

# Wait for user to stop
wait
EOF

    chmod +x start.sh
    print_status "Start script created"
}

# Main installation function
main() {
    echo ""
    print_info "Starting installation process..."
    echo ""
    
    # Check OS
    check_os
    
    # Check dependencies
    check_dependencies
    
    # Install system dependencies
    install_system_dependencies
    
    # Setup backend
    setup_backend
    
    # Setup frontend
    setup_frontend
    
    # Create start script
    create_start_script
    
    echo ""
    echo "=========================================================="
    print_status "Installation complete!"
    echo ""
    print_info "Next steps:"
    echo "1. Add your Gemini API key to backend/.env"
    echo "2. Run: ./start.sh"
    echo "3. Open http://localhost:3000 in your browser"
    echo ""
    print_warning "Important: You need a Gemini API key for AI features to work"
    print_info "Get your API key from: https://makersuite.google.com/app/apikey"
    echo ""
    print_info "For detailed instructions, see USER_GUIDE.md"
    echo "=========================================================="
}

# Run main function
main "$@"
