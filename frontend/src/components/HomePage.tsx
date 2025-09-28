import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Brain, User, Settings, Play } from 'lucide-react';
import { interviewAPI } from '../services/api';
import toast from 'react-hot-toast';

const HomePage: React.FC = () => {
  const [candidateName, setCandidateName] = useState('');
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('medium');
  const [category, setCategory] = useState('all');
  const [isCreating, setIsCreating] = useState(false);
  const navigate = useNavigate();

  const handleCreateInterview = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!candidateName.trim()) {
      toast.error('Please enter your name');
      return;
    }

    setIsCreating(true);
    
    try {
      const response = await interviewAPI.createInterview(candidateName, difficulty, category);
      
      if (response.success) {
        toast.success('Interview created successfully!');
        navigate(`/interview/${response.interview.id}`);
      } else {
        toast.error('Failed to create interview');
      }
    } catch (error) {
      console.error('Error creating interview:', error);
      toast.error('Failed to create interview. Please try again.');
    } finally {
      setIsCreating(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex items-center justify-center p-4">
      <div className="max-w-2xl w-full">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center mb-4">
            <Brain className="w-12 h-12 text-blue-600 mr-3" />
            <h1 className="text-4xl font-bold text-gray-800">CodeSage</h1>
          </div>
          <p className="text-xl text-gray-600 mb-2">AI Technical Interviewer</p>
          <p className="text-gray-500">
            Building Intelligence That Evaluates Intelligence
          </p>
        </div>

        {/* Main Card */}
        <div className="card">
          <div className="card-header">
            <h2 className="card-title flex items-center">
              <User className="w-5 h-5 mr-2" />
              Start Your Interview
            </h2>
            <p className="card-subtitle">
              Enter your details to begin your AI-powered technical interview
            </p>
          </div>

          <form onSubmit={handleCreateInterview} className="space-y-6">
            {/* Candidate Name */}
            <div className="form-group">
              <label htmlFor="candidateName" className="form-label">
                Your Name
              </label>
              <input
                type="text"
                id="candidateName"
                value={candidateName}
                onChange={(e) => setCandidateName(e.target.value)}
                className="form-input"
                placeholder="Enter your full name"
                required
              />
            </div>

            {/* Difficulty Level */}
            <div className="form-group">
              <label htmlFor="difficulty" className="form-label">
                Difficulty Level
              </label>
              <select
                id="difficulty"
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value as 'easy' | 'medium' | 'hard')}
                className="form-input"
              >
                <option value="easy">Easy - Basic algorithms and data structures</option>
                <option value="medium">Medium - Intermediate problem solving</option>
                <option value="hard">Hard - Advanced algorithms and optimization</option>
              </select>
            </div>

            {/* Category */}
            <div className="form-group">
              <label htmlFor="category" className="form-label">
                Category
              </label>
              <select
                id="category"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                className="form-input"
              >
                <option value="all">All Categories</option>
                <option value="arrays">Arrays & Strings</option>
                <option value="trees">Trees & Graphs</option>
                <option value="dynamic">Dynamic Programming</option>
                <option value="sorting">Sorting & Searching</option>
              </select>
            </div>

            {/* Features */}
            <div className="bg-blue-50 p-4 rounded-lg">
              <h3 className="font-semibold text-blue-800 mb-2">What to Expect:</h3>
              <ul className="text-sm text-blue-700 space-y-1">
                <li>• Real-time code analysis and feedback</li>
                <li>• AI-powered adaptive questioning</li>
                <li>• Voice interaction and hints</li>
                <li>• Performance tracking and reporting</li>
                <li>• Multiple programming languages supported</li>
              </ul>
            </div>

            {/* Submit Button */}
            <button
              type="submit"
              disabled={isCreating}
              className="btn btn-primary w-full flex items-center justify-center"
            >
              {isCreating ? (
                <>
                  <div className="spinner mr-2"></div>
                  Creating Interview...
                </>
              ) : (
                <>
                  <Play className="w-4 h-4 mr-2" />
                  Start Interview
                </>
              )}
            </button>
          </form>
        </div>

        {/* Footer */}
        <div className="text-center mt-8 text-gray-500 text-sm">
          <p>Powered by AI • Built for the Eightfold AI × ArIES Hackathon</p>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
