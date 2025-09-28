# CodeSage: The AI Technical Interviewer

CodeSage is an AI-powered technical interviewer that conducts live, adaptive coding interviews. It analyzes code in real-time, provides context-aware hints, assesses code quality, and generates detailed performance reports.

## ✨ Features

-   **Real-time Code Analysis**: Continuously tracks and analyzes code as it's written.
-   **Agentic Hint System**: Adjusts problem difficulty and offers progressive hints.
-   **Deep Code Quality Assessment**: Evaluates style, readability, and adherence to standards.
-   **Multi-language Support**: Python, JavaScript, Java, C++.
-   **Voice Integration**: Speech-to-text and text-to-speech capabilities.
-   **Comprehensive Reporting**: Generates a detailed dashboard for hiring managers.

## 🏗️ Architecture

-   **Backend**: Python, FastAPI, WebSockets, Google Gemini API
-   **Frontend**: React 18, TypeScript, Monaco Editor, Vite, Socket.io

## 🛠️ Installation & Setup

### Prerequisites

-   Python 3.11+
-   Node.js 18+
-   npm (comes with Node.js)
-   A Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

### 🚀 Quick Start

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd CodeSage
    ```

2.  **Run the installation script:**
    *   On **macOS/Linux**:
        ```bash
        chmod +x install.sh
        ./install.sh
        ```
    *   On **Windows**:
        ```cmd
        install.bat
        ```
    This will install all dependencies and create a `.env` file in the `backend` directory.

3.  **Configure your API Key:**
    *   Open the `backend/.env` file.
    *   Add your Gemini API key: `GEMINI_API_KEY=your_gemini_api_key_here`

4.  **Run the application:**
    *   On **macOS/Linux**:
        ```bash
        ./start.sh
        ```
    *   On **Windows**:
        ```cmd
        start.bat
        ```

5.  **Open your browser** and navigate to `http://localhost:3000`.

## 🎯 Usage

-   **Frontend Application**: `http://localhost:3000`
-   **Backend API Docs**: `http://localhost:8000/docs`

The application will guide you to start an interview. Write your code in the editor, run it to see real-time analysis, and interact with the AI assistant via chat or voice.

## 🔧 Troubleshooting

-   **"Command not found"**: Ensure Python and Node.js are installed and their paths are configured in your system's environment variables.
-   **Dependency Errors**: If you encounter module errors, try removing the `node_modules` (frontend) and `venv` (backend) directories and re-running the installation script.
-   **Port Already in Use**: The app uses ports `3000` and `8000`. If they are occupied, stop the process using them or configure new ports in `backend/.env` and `frontend/vite.config.ts`.
-   **Gemini API Error**: Double-check that your API key in `backend/.env` is correct and valid.
-   **Verification Script**: For a detailed diagnosis, run the verification script:
    ```bash
    python verify_installation.py
    ```

## 🤝 Contributing

1.  Fork the repository.
2.  Create a feature branch (`git checkout -b feature/YourFeature`).
3.  Commit your changes (`git commit -m 'Add some feature'`).
4.  Push to the branch (`git push origin feature/YourFeature`).
5.  Open a Pull Request.
