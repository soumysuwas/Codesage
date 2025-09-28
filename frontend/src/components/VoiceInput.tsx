import React, { useState, useEffect, useRef } from 'react';
import { Mic, MicOff, Volume2, VolumeX } from 'lucide-react';

interface VoiceInputProps {
  onTranscript: (text: string) => void;
  isListening: boolean;
  onStartListening: () => void;
  onStopListening: () => void;
  className?: string;
}

export const VoiceInput: React.FC<VoiceInputProps> = ({
  onTranscript,
  isListening,
  onStartListening,
  onStopListening,
  className = ''
}) => {
  const [isSupported, setIsSupported] = useState(false);
  const [isMuted, setIsMuted] = useState(false);
  const [interimTranscript, setInterimTranscript] = useState('');
  const [finalTranscript, setFinalTranscript] = useState('');
  const timeoutRef = useRef<number | null>(null);

  useEffect(() => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      setIsSupported(true);
    }
  }, []);

  const startListening = () => {
    if (!isSupported) return;
    
    const SpeechRecognition = (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US';

    recognition.onstart = () => {
      setInterimTranscript('');
      setFinalTranscript('');
    };

    recognition.onresult = (event: any) => {
      let interim = '';
      let final = '';

      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript;
        if (event.results[i].isFinal) {
          final += transcript;
        } else {
          interim += transcript;
        }
      }

      setInterimTranscript(interim);
      setFinalTranscript(final);

      if (final && !isListening) {
        if (timeoutRef.current) clearTimeout(timeoutRef.current);
        timeoutRef.current = setTimeout(() => {
          if (onTranscript && final.trim()) {
            onTranscript(final.trim());
            setFinalTranscript('');
            setInterimTranscript('');
          }
        }, 2000);
      }
    };

    recognition.onerror = (event: any) => {
      console.error('Speech recognition error:', event.error);
      if (isListening) {
        onStopListening();
      }
    };

    recognition.onend = () => {
      if (isListening) {
        setTimeout(() => {
          if (isListening) {
            try {
              recognition.start();
            } catch (e) {
              console.warn('Could not restart recognition:', e);
            }
          }
        }, 100);
      }
    };

    try {
      recognition.start();
      onStartListening();
    } catch (e) {
      console.error('Error starting recognition:', e);
    }
  };

  const stopListening = () => {
    if (timeoutRef.current) {
      clearTimeout(timeoutRef.current);
    }
    onStopListening();
  };

  const toggleMute = () => {
    setIsMuted(!isMuted);
  };

  const speak = (text: string) => {
    if ('speechSynthesis' in window && !isMuted) {
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.rate = 0.9;
      utterance.pitch = 1;
      utterance.volume = 0.8;
      
      const voices = speechSynthesis.getVoices();
      const preferredVoice = voices.find(voice => 
        voice.lang.includes('en') && voice.name.includes('Google')
      ) || voices.find(voice => voice.lang.includes('en'));
      
      if (preferredVoice) {
        utterance.voice = preferredVoice;
      }
      
      speechSynthesis.speak(utterance);
    }
  };

  useEffect(() => {
    (window as any).voiceInputSpeak = speak;
  }, [isMuted]);

  if (!isSupported) {
    return (
      <div className={`text-sm text-gray-500 ${className}`}>
        Voice input not supported in this browser
      </div>
    );
  }

  return (
    <div className={`flex items-center space-x-2 ${className}`}>
      <button
        onClick={isListening ? stopListening : startListening}
        className={`voice-button ${isListening ? 'listening' : 'ready'}`}
        title={isListening ? 'Stop listening' : 'Start voice input'}
      >
        {isListening ? <MicOff size={20} /> : <Mic size={20} />}
      </button>

      <button
        onClick={toggleMute}
        className={`voice-button ${isMuted ? 'ready' : 'ready'}`}
        style={{ backgroundColor: isMuted ? '#718096' : '#38a169' }}
        title={isMuted ? 'Unmute voice output' : 'Mute voice output'}
      >
        {isMuted ? <VolumeX size={20} /> : <Volume2 size={20} />}
      </button>

      {(interimTranscript || finalTranscript) && (
        <div className="flex-1 min-w-0">
          <div className="text-sm text-gray-600 bg-gray-100 p-2 rounded border">
            {finalTranscript && (
              <div className="text-gray-800 font-medium">{finalTranscript}</div>
            )}
            {interimTranscript && (
              <div className="text-gray-500 italic">{interimTranscript}</div>
            )}
          </div>
        </div>
      )}

      {isListening && (
        <div className="flex items-center space-x-1 text-sm text-red-500">
          <div className="w-2 h-2 bg-red-500 rounded-full animate-pulse"></div>
          <span>Listening...</span>
        </div>
      )}
    </div>
  );
};
