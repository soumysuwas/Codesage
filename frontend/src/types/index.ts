export interface Interview {
  id: string;
  candidate_name: string;
  difficulty: 'easy' | 'medium' | 'hard';
  category: string;
  questions: Question[];
  status: 'created' | 'in_progress' | 'completed' | 'cancelled';
  created_at: string;
  started_at?: string;
  completed_at?: string;
  current_question: number;
}

export interface Question {
  id: string;
  title: string;
  description: string;
  difficulty: 'easy' | 'medium' | 'hard';
  category: string;
  test_cases: TestCase[];
  constraints: string;
  hints: string[];
  expected_complexity?: string;
}

export interface TestCase {
  input: Record<string, any>;
  expected: any;
}

export interface CodeAnalysis {
  syntax: {
    valid: boolean;
    errors: string[];
  };
  runtime: {
    execution_time: number;
    output: string;
    error: string;
    success: boolean;
    return_code: number;
  };
  complexity: {
    time_complexity: string;
    space_complexity: string;
  };
  quality: {
    score: number;
    issues: string[];
    grade: string;
  };
  performance: {
    execution_time: number;
    memory_usage: string;
    efficiency: string;
  };
  overall_score: number;
  language: string;
}

export interface ConversationMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: string;
  message_type?: string;
}

export interface PerformanceMetrics {
  overall_score: number;
  syntax_score: number;
  runtime_score: number;
  quality_score: number;
  complexity_score: number;
  execution_time: number;
  hints_used: number;
  code_submissions: number;
}

export interface WebSocketMessage {
  type: string;
  data?: any;
  analysis?: CodeAnalysis;
  ai_response?: string;
  hint?: string;
  hint_level?: number;
  question?: string;
  report?: string;
}
