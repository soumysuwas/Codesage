import React, { useState } from 'react';
import { Lightbulb, Clock, Target, AlertCircle } from 'lucide-react';
import { Question } from '../types';

interface QuestionPanelProps {
  question: Question;
  questionNumber: number;
  onRequestHint: (hintLevel: number) => void;
  currentHintLevel: number;
}

const QuestionPanel: React.FC<QuestionPanelProps> = ({
  question,
  questionNumber,
  onRequestHint,
  currentHintLevel
}) => {
  const [showTestCases, setShowTestCases] = useState(false);
  const [showHints, setShowHints] = useState(false);

  const getDifficultyColor = (difficulty: string) => {
    switch (difficulty) {
      case 'easy':
        return 'bg-green-100 text-green-800';
      case 'medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'hard':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  const getHintButtonText = (level: number) => {
    switch (level) {
      case 1:
        return 'Get Hint';
      case 2:
        return 'More Help';
      case 3:
        return 'Detailed Guidance';
      default:
        return 'Get Hint';
    }
  };

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center justify-between mb-2">
          <h3 className="card-title">Question {questionNumber}</h3>
          <span className={`px-2 py-1 rounded-full text-xs font-semibold ${getDifficultyColor(question.difficulty)}`}>
            {question.difficulty.toUpperCase()}
          </span>
        </div>
        <h4 className="text-lg font-semibold text-gray-800">{question.title}</h4>
        <p className="text-sm text-gray-600">{question.category}</p>
      </div>

      <div className="space-y-4">
        {/* Problem Description */}
        <div>
          <h5 className="font-medium text-gray-700 mb-2">Problem Description</h5>
          <div className="bg-gray-50 p-4 rounded-lg">
            <p className="text-sm leading-relaxed whitespace-pre-wrap">
              {question.description}
            </p>
          </div>
        </div>

        {/* Constraints */}
        <div>
          <h5 className="font-medium text-gray-700 mb-2 flex items-center">
            <AlertCircle className="w-4 h-4 mr-1" />
            Constraints
          </h5>
          <div className="bg-yellow-50 p-3 rounded-lg border-l-4 border-yellow-400">
            <p className="text-sm text-yellow-800">{question.constraints}</p>
          </div>
        </div>

        {/* Expected Complexity */}
        {question.expected_complexity && (
          <div>
            <h5 className="font-medium text-gray-700 mb-2 flex items-center">
              <Target className="w-4 h-4 mr-1" />
              Expected Complexity
            </h5>
            <div className="bg-blue-50 p-3 rounded-lg">
              <p className="text-sm text-blue-800 font-mono">
                {question.expected_complexity}
              </p>
            </div>
          </div>
        )}

        {/* Test Cases */}
        <div>
          <button
            onClick={() => setShowTestCases(!showTestCases)}
            className="flex items-center justify-between w-full p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
          >
            <h5 className="font-medium text-gray-700">Test Cases</h5>
            <span className="text-sm text-gray-500">
              {showTestCases ? 'Hide' : 'Show'} ({question.test_cases.length})
            </span>
          </button>
          
          {showTestCases && (
            <div className="mt-2 space-y-2">
              {question.test_cases.map((testCase, index) => (
                <div key={index} className="bg-gray-50 p-3 rounded-lg">
                  <div className="text-sm">
                    <div className="mb-2">
                      <span className="font-medium text-gray-600">Input:</span>
                      <pre className="mt-1 text-xs bg-white p-2 rounded border">
                        {JSON.stringify(testCase.input, null, 2)}
                      </pre>
                    </div>
                    <div>
                      <span className="font-medium text-gray-600">Expected Output:</span>
                      <pre className="mt-1 text-xs bg-white p-2 rounded border">
                        {JSON.stringify(testCase.expected, null, 2)}
                      </pre>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Hints */}
        <div>
          <button
            onClick={() => setShowHints(!showHints)}
            className="flex items-center justify-between w-full p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
          >
            <h5 className="font-medium text-gray-700 flex items-center">
              <Lightbulb className="w-4 h-4 mr-1" />
              Hints
            </h5>
            <span className="text-sm text-gray-500">
              {showHints ? 'Hide' : 'Show'} ({question.hints.length})
            </span>
          </button>
          
          {showHints && (
            <div className="mt-2 space-y-2">
              {question.hints.map((hint, index) => (
                <div key={index} className="bg-yellow-50 p-3 rounded-lg border-l-4 border-yellow-400">
                  <div className="flex items-start">
                    <span className="flex-shrink-0 w-6 h-6 bg-yellow-400 text-white rounded-full flex items-center justify-center text-xs font-bold mr-2">
                      {index + 1}
                    </span>
                    <p className="text-sm text-yellow-800">{hint}</p>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>

        {/* Hint Request Button */}
        <div className="pt-4 border-t">
          <button
            onClick={() => onRequestHint(currentHintLevel + 1)}
            disabled={currentHintLevel >= 3}
            className="btn btn-secondary w-full flex items-center justify-center"
          >
            <Lightbulb className="w-4 h-4 mr-2" />
            {getHintButtonText(currentHintLevel + 1)}
            {currentHintLevel >= 3 && ' (Max reached)'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default QuestionPanel;
