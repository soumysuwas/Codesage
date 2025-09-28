import React, { useState, useRef, useEffect } from 'react';
import { Send, Bot, User, Loader } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { VoiceInput } from './VoiceInput';
import { ConversationMessage } from '../types';

interface ChatInterfaceProps {
  messages: ConversationMessage[];
  onSendMessage: (message: string) => void;
  isAnalyzing?: boolean;
}

const ChatInterface: React.FC<ChatInterfaceProps> = ({ 
  messages, 
  onSendMessage, 
  isAnalyzing = false 
}) => {
  const [inputMessage, setInputMessage] = useState('');
  const [isListening, setIsListening] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputMessage.trim() && onSendMessage) {
      onSendMessage(inputMessage.trim());
      setInputMessage('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  const handleVoiceTranscript = (transcript: string) => {
    setInputMessage(transcript);
    if (onSendMessage) {
      onSendMessage(transcript);
      setInputMessage('');
    }
  };

  const handleVoiceError = (error: string) => {
    console.error('Voice input error:', error);
    setIsListening(false);
  };

  const handleStartListening = () => {
    setIsListening(true);
  };

  const handleStopListening = () => {
    setIsListening(false);
  };

  // Auto-speak AI responses
  useEffect(() => {
    const lastMessage = messages[messages.length - 1];
    if (lastMessage && lastMessage.role === 'assistant' && (window as any).voiceInputSpeak) {
      // Small delay to ensure the message is rendered
      setTimeout(() => {
        (window as any).voiceInputSpeak(lastMessage.content);
      }, 500);
    }
  }, [messages]);

  const formatTime = (timestamp: string) => {
    return new Date(timestamp).toLocaleTimeString([], { 
      hour: '2-digit', 
      minute: '2-digit' 
    });
  };

  return (
    <div className="card h-full flex flex-col">
      <div className="card-header">
        <h3 className="card-title flex items-center">
          <Bot className="w-5 h-5 mr-2 text-blue-600" />
          AI Interviewer
        </h3>
        <p className="card-subtitle">
          Ask questions or get help with your code
        </p>
      </div>

      <div className="chat-container flex-1">
        <AnimatePresence>
          {messages.map((message) => (
            <motion.div
              key={message.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className={`chat-message ${message.role}`}
            >
              <div className="flex items-start space-x-2">
                <div className="flex-shrink-0">
                  {message.role === 'user' ? (
                    <User className="w-4 h-4 text-gray-600" />
                  ) : (
                    <Bot className="w-4 h-4 text-blue-600" />
                  )}
                </div>
                <div className="flex-1">
                  <p className="text-sm whitespace-pre-wrap">{message.content}</p>
                  <p className="text-xs text-gray-500 mt-1">
                    {formatTime(message.timestamp)}
                  </p>
                </div>
              </div>
            </motion.div>
          ))}
        </AnimatePresence>

        {isAnalyzing && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="chat-message assistant"
          >
            <div className="flex items-start space-x-2">
              <div className="flex-shrink-0">
                <Bot className="w-4 h-4 text-blue-600" />
              </div>
              <div className="flex-1">
                <div className="flex items-center space-x-2">
                  <Loader className="w-4 h-4 animate-spin text-blue-600" />
                  <p className="text-sm text-gray-600">Analyzing your code...</p>
                </div>
              </div>
            </div>
          </motion.div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="mt-4">
        <div className="space-y-3">
          {/* Voice Input Controls */}
          <VoiceInput
            onTranscript={handleVoiceTranscript}
            onError={handleVoiceError}
            isListening={isListening}
            onStartListening={handleStartListening}
            onStopListening={handleStopListening}
            className="mb-2"
          />
          
          {/* Text Input */}
          <div className="flex space-x-2">
            <input
              ref={inputRef}
              type="text"
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your message or use voice input..."
              className="form-input flex-1"
              disabled={isAnalyzing || isListening}
            />
            <button
              type="submit"
              disabled={!inputMessage.trim() || isAnalyzing || isListening}
              className="btn btn-primary"
            >
              <Send className="w-4 h-4" />
            </button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default ChatInterface;
