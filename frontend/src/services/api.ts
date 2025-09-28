import axios from 'axios';

const API_BASE_URL = window.location.origin.replace(":3000", ":8000") || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const interviewAPI = {
  createInterview: async (candidateName: string, difficulty: string, category: string = 'all') => {
    const response = await api.post('/api/interviews', {
      candidate_name: candidateName,
      difficulty,
      category,
    });
    return response.data;
  },

  getInterview: async (interviewId: string) => {
    const response = await api.get(`/api/interviews/${interviewId}`);
    return response.data;
  },

  startInterview: async (interviewId: string) => {
    const response = await api.post(`/api/interviews/${interviewId}/start`);
    return response.data;
  },

  listInterviews: async () => {
    const response = await api.get('/api/interviews');
    return response.data;
  },
};

export const analysisAPI = {
  analyzeCode: async (code: string, language: string) => {
    const response = await api.post('/api/analysis/analyze', {
      code,
      language,
    });
    return response.data;
  },
};

export default api;
