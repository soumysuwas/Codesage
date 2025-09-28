import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Play, 
  Pause, 
  RotateCcw, 
  Lightbulb, 
  Send, 
  Mic, 
  MicOff,
  Code2,
  Brain,
  Clock,
  CheckCircle,
  XCircle,
  AlertCircle,
  ArrowLeft,
  ArrowRight
} from 'lucide-react';
import { interviewAPI } from '../services/api';
import { websocketService } from '../services/websocket';
import { Interview, Question, ConversationMessage, CodeAnalysis, WebSocketMessage } from '../types';
import CodeEditor from './CodeEditor';
import ChatInterface from './ChatInterface';
import PerformancePanel from './PerformancePanel';
import QuestionPanel from './QuestionPanel';
import toast from 'react-hot-toast';

const InterviewPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  
  const [interview, setInterview] = useState<Interview | null>(null);
  const [currentQuestion, setCurrentQuestion] = useState<Question | null>(null);
  const [code, setCode] = useState('');
  const [language, setLanguage] = useState('python');
  const [isRunning, setIsRunning] = useState(false);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [showPerformance, setShowPerformance] = useState(false);
  const [chatMessages, setChatMessages] = useState<ConversationMessage[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [timeElapsed, setTimeElapsed] = useState(0);
  const [startTime, setStartTime] = useState<Date | null>(null);
  const [isVoiceEnabled, setIsVoiceEnabled] = useState(true);
  const [currentHintLevel, setCurrentHintLevel] = useState(0);
  const [analysis, setAnalysis] = useState<CodeAnalysis | null>(null);
  const [isConnected, setIsConnected] = useState(false);

  const intervalRef = useRef<number | null>(null);

  // Load interview data
  useEffect(() => {
    const loadInterview = async () => {
      if (!id) return;
      
      try {
        const response = await interviewAPI.getInterview(id);
        if (response.success) {
          setInterview(response.interview);
          setCurrentQuestion(response.interview.questions[0]);
          setIsLoading(false);
        } else {
          toast.error('Interview not found');
          navigate('/');
        }
      } catch (error) {
        console.error('Error loading interview:', error);
        toast.error('Failed to load interview');
        navigate('/');
      }
    };

    loadInterview();
  }, [id, navigate]);

  // Start interview
  useEffect(() => {
    const startInterview = async () => {
      if (!id || !interview) return;
      
      try {
        await interviewAPI.startInterview(id);
        setStartTime(new Date());
        startTimer();
        connectWebSocket();
      } catch (error) {
        console.error('Error starting interview:', error);
        toast.error('Failed to start interview');
      }
    };

    if (interview && interview.status === 'created') {
      startInterview();
    }
  }, [interview, id]);

  // WebSocket connection
  const connectWebSocket = () => {
    if (!id) return;

    websocketService.connect(id);
    setIsConnected(true);

    // Set up message handlers
    websocketService.onMessage('code_analysis', (data) => {
      setAnalysis(data.analysis);
      setIsAnalyzing(false);
      
      // Add AI response to chat
      const aiMessage: ConversationMessage = {
        id: Date.now().toString(),
        role: 'assistant',
        content: data.ai_response,
        timestamp: new Date().toISOString()
      };
      setChatMessages(prev => [...prev, aiMessage]);
    });

    websocketService.onMessage('chat_message', (data) => {
      const aiMessage: ConversationMessage = {
        id: Date.now().toString(),
        role: 'assistant',
        content: data.ai_response,
        timestamp: new Date().toISOString()
      };
      setChatMessages(prev => [...prev, aiMessage]);
    });

    websocketService.onMessage('hint_response', (data) => {
      const hintMessage: ConversationMessage = {
        id: Date.now().toString(),
        role: 'assistant',
        content: `Hint ${data.hint_level}: ${data.hint}`,
        timestamp: new Date().toISOString()
      };
      setChatMessages(prev => [...prev, hintMessage]);
      setCurrentHintLevel(data.hint_level);
    });

    websocketService.onMessage('follow_up_question', (data) => {
      const questionMessage: ConversationMessage = {
        id: Date.now().toString(),
        role: 'assistant',
        content: data.question,
        timestamp: new Date().toISOString()
      };
      setChatMessages(prev => [...prev, questionMessage]);
    });
  };

  // Timer
  const startTimer = () => {
    intervalRef.current = setInterval(() => {
      setTimeElapsed(prev => prev + 1);
    }, 1000);
  };

  const stopTimer = () => {
    if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }
  };

  useEffect(() => {
    return () => {
      stopTimer();
      websocketService.disconnect();
    };
  }, []);

  // Format time
  const formatTime = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Handle code changes
  const handleCodeChange = (newCode: string) => {
    setCode(newCode);
  };

  const handleLanguageChange = (newLanguage: string) => {
    setLanguage(newLanguage);
  };

  // Handle code execution
  const handleRunCode = () => {
    if (!code.trim()) {
      toast.error('Please write some code first');
      return;
    }

    setIsRunning(true);
    setIsAnalyzing(true);

    // Send code for analysis via WebSocket
    websocketService.sendCodeAnalysis(
      code,
      language,
      currentQuestion?.description || ''
    );

    // Simulate running state
    setTimeout(() => {
      setIsRunning(false);
    }, 2000);
  };

  // Handle code reset
  const handleResetCode = () => {
    setCode('');
    setAnalysis(null);
    setCurrentHintLevel(0);
  };

  // Handle chat messages
  const handleSendMessage = (message: string) => {
    const userMessage: ConversationMessage = {
      id: Date.now().toString(),
      role: 'user',
      content: message,
      timestamp: new Date().toISOString()
    };
    setChatMessages(prev => [...prev, userMessage]);

    // Send message via WebSocket
    websocketService.sendMessage(message);
  };

  // Handle hint requests
  const handleRequestHint = (hintLevel: number) => {
    if (!currentQuestion) return;

    websocketService.requestHint(
      currentQuestion.id,
      hintLevel,
      code
    );
  };

  // Handle next question
  const handleNextQuestion = () => {
    if (!interview || !currentQuestion) return;

    const currentIndex = interview.questions.findIndex(q => q.id === currentQuestion.id);
    if (currentIndex < interview.questions.length - 1) {
      const nextQuestion = interview.questions[currentIndex + 1];
      setCurrentQuestion(nextQuestion);
      setCode('');
      setAnalysis(null);
      setCurrentHintLevel(0);
    }
  };

  // Handle previous question
  const handlePreviousQuestion = () => {
    if (!interview || !currentQuestion) return;

    const currentIndex = interview.questions.findIndex(q => q.id === currentQuestion.id);
    if (currentIndex > 0) {
      const prevQuestion = interview.questions[currentIndex - 1];
      setCurrentQuestion(prevQuestion);
      setCode('');
      setAnalysis(null);
      setCurrentHintLevel(0);
    }
  };

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <div className="spinner mx-auto mb-4"></div>
          <p className="text-white">Loading interview...</p>
        </div>
      </div>
    );
  }

  if (!interview || !currentQuestion) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <XCircle className="w-16 h-16 text-red-500 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-white mb-2">Interview Not Found</h2>
          <p className="text-blue-200 mb-4">The interview you're looking for doesn't exist.</p>
          <button onClick={() => navigate('/')} className="btn btn-primary">
            Go Home
          </button>
        </div>
      </div>
    );
  }

  const currentQuestionIndex = interview.questions.findIndex(q => q.id === currentQuestion.id);

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Header */}
      <header className="bg-white shadow-sm border-b">
        <div className="container mx-auto px-6 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center space-x-4">
              <button
                onClick={() => navigate('/')}
                className="btn btn-secondary"
              >
                <ArrowLeft className="w-4 h-4 mr-2" />
                Back
              </button>
              <div className="flex items-center space-x-2">
                <Brain className="w-8 h-8 text-blue-600" />
                <h1 className="text-2xl font-bold text-gray-800">CodeSage</h1>
              </div>
              <div className="text-sm text-gray-600">
                Interviewing: <span className="font-semibold">{interview.candidate_name}</span>
              </div>
            </div>
            
            <div className="flex items-center space-x-4">
              <div className="flex items-center space-x-2 text-sm text-gray-600">
                <Clock className="w-4 h-4" />
                <span>{formatTime(timeElapsed)}</span>
              </div>
              
              <div className="flex items-center space-x-2">
                <span className="text-sm text-gray-600">Question</span>
                <span className="bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-sm font-semibold">
                  {currentQuestionIndex + 1} of {interview.questions.length}
                </span>
              </div>

              <div className="flex items-center space-x-2">
                <button
                  onClick={() => setIsVoiceEnabled(!isVoiceEnabled)}
                  className={`btn ${isVoiceEnabled ? 'btn-primary' : 'btn-secondary'}`}
                  title={isVoiceEnabled ? 'Disable voice feedback' : 'Enable voice feedback'}
                >
                  {isVoiceEnabled ? <Mic className="w-4 h-4" /> : <MicOff className="w-4 h-4" />}
                  Voice
                </button>
                
                <button
                  onClick={() => setShowPerformance(!showPerformance)}
                  className="btn btn-secondary"
                >
                  <Code2 className="w-4 h-4" />
                  Performance
                </button>
              </div>
            </div>
          </div>
        </div>
      </header>

      <div className="container mx-auto px-6 py-6">
        <div className="grid lg:grid-cols-3 gap-6">
          {/* Left Panel - Question */}
          <div className="lg:col-span-1">
            <QuestionPanel 
              question={currentQuestion}
              questionNumber={currentQuestionIndex + 1}
              onRequestHint={handleRequestHint}
              currentHintLevel={currentHintLevel}
            />
          </div>

          {/* Center Panel - Code Editor */}
          <div className="lg:col-span-1">
            <CodeEditor
              code={code}
              language={language}
              onChange={handleCodeChange}
              onLanguageChange={handleLanguageChange}
              onRun={handleRunCode}
              onReset={handleResetCode}
              isRunning={isRunning}
            />
          </div>

          {/* Right Panel - Chat */}
          <div className="lg:col-span-1">
            <ChatInterface
              messages={chatMessages}
              onSendMessage={handleSendMessage}
              isAnalyzing={isAnalyzing}
            />
          </div>
        </div>

        {/* Navigation */}
        <div className="mt-6 flex justify-between">
          <button
            onClick={handlePreviousQuestion}
            disabled={currentQuestionIndex === 0}
            className="btn btn-secondary"
          >
            <ArrowLeft className="w-4 h-4 mr-2" />
            Previous
          </button>

          <div className="flex space-x-2">
            <button
              onClick={() => websocketService.generateReport()}
              className="btn btn-primary"
            >
              Generate Report
            </button>
          </div>

          <button
            onClick={handleNextQuestion}
            disabled={currentQuestionIndex === interview.questions.length - 1}
            className="btn btn-primary"
          >
            Next
            <ArrowRight className="w-4 h-4 ml-2" />
          </button>
        </div>
      </div>

      {/* Performance Panel */}
      <PerformancePanel
        analysis={analysis}
        isVisible={showPerformance}
        onToggle={() => setShowPerformance(!showPerformance)}
      />
    </div>
  );
};

export default InterviewPage;
