import { WebSocketMessage } from '../types';

class WebSocketService {
  private socket: WebSocket | null = null;
  private callbacks: Map<string, (data: any) => void> = new Map();
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;

  connect(interviewId: string) {
    try {
      this.socket = new WebSocket(`ws://localhost:8000/ws/${interviewId}`);

      this.socket.onopen = () => {
        console.log('Connected to interview session');
        this.reconnectAttempts = 0;
      };

      this.socket.onclose = () => {
        console.log('Disconnected from interview session');
        this.attemptReconnect(interviewId);
      };

      this.socket.onerror = (error) => {
        console.error('WebSocket error:', error);
      };

      this.socket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          this.handleMessage(data);
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };
    } catch (error) {
      console.error('Error connecting to WebSocket:', error);
    }
  }

  private attemptReconnect(interviewId: string) {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      console.log(`Attempting to reconnect... (${this.reconnectAttempts}/${this.maxReconnectAttempts})`);
      setTimeout(() => this.connect(interviewId), 2000 * this.reconnectAttempts);
    }
  }

  private handleMessage(data: any) {
    const { type, ...messageData } = data;
    
    switch (type) {
      case 'code_analysis':
        this.triggerCallback('code_analysis', messageData);
        break;
      case 'chat_message':
        this.triggerCallback('chat_message', messageData);
        break;
      case 'hint_response':
        this.triggerCallback('hint_response', messageData);
        break;
      case 'follow_up_question':
        this.triggerCallback('follow_up_question', messageData);
        break;
      case 'performance_report':
        this.triggerCallback('performance_report', messageData);
        break;
      default:
        console.log('Unknown message type:', type);
    }
  }

  disconnect() {
    if (this.socket) {
      this.socket.close();
      this.socket = null;
    }
  }

  private send(data: any) {
    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.send(JSON.stringify(data));
    } else {
      console.warn('WebSocket not connected, cannot send message');
    }
  }

  sendCodeAnalysis(code: string, language: string, problemDescription: string = '') {
    this.send({
      type: 'analyze_code',
      code,
      language,
      problem_description: problemDescription,
      timestamp: new Date().toISOString()
    });
  }

  sendMessage(message: string) {
    this.send({
      type: 'send_message',
      message,
      timestamp: new Date().toISOString()
    });
  }

  requestHint(questionId: string, hintLevel: number = 1, currentCode: string = '') {
    this.send({
      type: 'request_hint',
      question_id: questionId,
      hint_level: hintLevel,
      current_code: currentCode,
      timestamp: new Date().toISOString()
    });
  }

  requestFollowUp(code: string, analysis: any, problemDescription: string) {
    this.send({
      type: 'request_follow_up',
      code,
      analysis,
      problem_description: problemDescription,
      timestamp: new Date().toISOString()
    });
  }

  generateReport() {
    this.send({
      type: 'generate_report',
      timestamp: new Date().toISOString()
    });
  }

  onMessage(type: string, callback: (data: any) => void) {
    this.callbacks.set(type, callback);
  }

  offMessage(type: string) {
    this.callbacks.delete(type);
  }

  private triggerCallback(type: string, data: any) {
    const callback = this.callbacks.get(type);
    if (callback) {
      callback(data);
    }
  }
}

export const websocketService = new WebSocketService();
