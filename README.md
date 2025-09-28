# CodeSage: The AI Technical Interviewer

CodeSage is an AI-powered platform that conducts live, adaptive coding interviews. It analyzes code in real-time, provides context-aware hints via an AI agent, and assesses code against a variety of metrics.

This project was developed based on the requirements of the Eightfold AI Hackathon, focusing on creating an intelligent and interactive interview experience.

## ✨ Implemented Features

Based on the problem statement, the following core features have been implemented:

-   **Real-time Code Execution & Analysis**
    -   **How it works**: The backend uses a sandboxed environment to securely execute user-submitted code in Python, JavaScript, Java, and C++. A FastAPI WebSocket connection provides immediate feedback on correctness, execution time, and memory usage to the React frontend.

-   **AI Interviewer Agent**
    -   **How it works**: Leveraging the Google Gemini API, the AI acts as an interactive interviewer. It can process the user's current code and conversation context to provide progressive, helpful hints without giving away the solution. This is managed by the `gemini_service` on the backend.

-   **Interactive Web-Based IDE**
    -   **How it works**: The frontend is built with React and TypeScript, featuring the Monaco Editor to provide a familiar coding environment. The UI is divided into dedicated panels for the problem description, code editor, and live performance feedback, creating a seamless user experience.

-   **Voice Integration**
    -   **How it works**: The frontend utilizes the browser's native Web Speech API for both speech-to-text and text-to-speech. This allows candidates to interact with the AI agent using their voice, and hear its responses spoken aloud.

---

### 🎥 Demo Video

Here's a quick demonstration of CodeSage in action:

[**Watch the CodeSage Demo**](https://youtu.be/IpnebJaxouU?si=iIDgRkcvNyvZ7z0n)

---


## 🏗️ Architecture

-   **Backend**:
    -   **Language**: Python
    -   **Framework**: FastAPI
    -   **Server**: Uvicorn
    -   **Communication**: WebSockets
    -   **AI Integration**: Google Gemini API
-   **Frontend**:
    -   **Language**: TypeScript
    -   **Framework**: React 18
    -   **Build Tool**: Vite
    -   **Code Editor**: Monaco Editor
    -   **Communication**: Socket.io

## 🛠️ Installation & Setup

### Prerequisites

-   Python 3.11+
-   Node.js 18+
-   npm (Node Package Manager)
-   Git
-   A Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))
-   (Optional) Docker for containerized deployment.

### 🚀 Quick Start (Recommended)

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd CodeSage
    ```

2.  **Run the installation script:**
    *   On **macOS/Linux**: `chmod +x install.sh && ./install.sh`
    *   On **Windows**: `install.bat`

3.  **Configure your API Key:**
    *   Open `backend/.env` and add your Gemini API key: `GEMINI_API_KEY=your_key_here`

4.  **Run the application:**
    *   On **macOS/Linux**: `./start.sh`
    *   On **Windows**: `start.bat`

5.  **Open your browser** and navigate to `http://localhost:3000`.

### Manual Installation

If you prefer to set up the project manually, follow these steps.

#### Backend Setup
1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2.  **Create and activate a Python virtual environment:**
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```cmd
        python -m venv venv
        venv\Scripts\activate
        ```
3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

#### Frontend Setup
1.  **Navigate to the frontend directory from the project root:**
    ```bash
    cd frontend
    ```
2.  **Install Node.js dependencies:**
    ```bash
    npm install
    ```

### Environment Configuration

The application requires a Gemini API key. Create a `.env` file in the `backend` directory and add the following:

```env
# Required
GEMINI_API_KEY=your_actual_gemini_api_key_here

# Optional - Default values are shown
HOST=0.0.0.0
PORT=8000
CORS_ORIGINS=http://localhost:3000
CODE_TIMEOUT=5
```
-   `GEMINI_API_KEY`: **(Required)** Your secret API key for the Google Gemini service.
-   `HOST`: The IP address the backend server will listen on.
-   `PORT`: The port for the backend server.
-   `CORS_ORIGINS`: The allowed origin for Cross-Origin Resource Sharing.

## ▶️ Running the Application

After installation, you can run the application using the start scripts (`start.sh` or `start.bat`) or manually.

### Manual Start

Run each command in a separate terminal.

**Terminal 1: Start Backend**
```bash
cd backend
source venv/bin/activate # On Windows: venv\Scripts\activate
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2: Start Frontend**
```bash
cd frontend
npm run dev
```

### Accessing the Application
-   **Frontend**: [http://localhost:3000](http://localhost:3000)
-   **Backend API**: [http://localhost:8000](http://localhost:8000)
-   **API Documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)

## 📖 How to Use

1.  **Start an Interview**: Navigate to the application, enter your name, and select an interview difficulty and category.
2.  **Write Code**: A coding problem will be presented. Write your solution in the Monaco code editor.
3.  **Run and Analyze**: Click the "Run Code" button to execute your solution and see real-time analysis of its performance, style, and correctness.
4.  **Interact with the AI**: Use the chat panel to ask the AI interviewer for hints. You can also use voice commands.
5.  **Monitor Performance**: The performance panel displays key metrics like execution time and memory usage.
6.  **Review Results**: After the interview, a comprehensive report is generated summarizing your performance.

## 🔧 Troubleshooting

-   **Dependency Errors**: If you encounter module errors, try removing the `node_modules` (frontend) and `venv` (backend) directories and re-running the installation script.
-   **Port Already in Use**: The app uses ports `3000` and `8000`. If they are occupied, stop the process using them.
-   **Gemini API Error**: Ensure your API key in `backend/.env` is correct and valid.
-   **Verification Script**: For a detailed diagnosis, run `python verify_installation.py`.
-   **Manual Health Check**: You can check if the backend is running by visiting `http://localhost:8000/health`. You should see a JSON response with `"status": "OK"`.
