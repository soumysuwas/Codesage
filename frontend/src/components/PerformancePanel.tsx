import React from 'react';
import { TrendingUp, Clock, CheckCircle, XCircle, AlertTriangle, Code2 } from 'lucide-react';
import { CodeAnalysis, PerformanceMetrics } from '../types';

interface PerformancePanelProps {
  analysis?: CodeAnalysis;
  metrics?: PerformanceMetrics;
  isVisible: boolean;
  onToggle: () => void;
}

const PerformancePanel: React.FC<PerformancePanelProps> = ({
  analysis,
  metrics,
  isVisible,
  onToggle
}) => {
  if (!isVisible) {
    return (
      <button
        onClick={onToggle}
        className="fixed bottom-4 right-4 btn btn-primary shadow-lg z-50"
      >
        <TrendingUp className="w-4 h-4 mr-2" />
        Show Performance
      </button>
    );
  }

  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-green-600';
    if (score >= 60) return 'text-yellow-600';
    return 'text-red-600';
  };

  const getScoreBgColor = (score: number) => {
    if (score >= 80) return 'bg-green-100';
    if (score >= 60) return 'bg-yellow-100';
    return 'bg-red-100';
  };

  return (
    <div className="fixed bottom-4 right-4 w-80 bg-white rounded-lg shadow-xl border z-50 max-h-96 overflow-y-auto">
      <div className="p-4 border-b">
        <div className="flex items-center justify-between">
          <h3 className="font-semibold text-gray-800 flex items-center">
            <TrendingUp className="w-4 h-4 mr-2" />
            Performance Analysis
          </h3>
          <button
            onClick={onToggle}
            className="text-gray-400 hover:text-gray-600"
          >
            ×
          </button>
        </div>
      </div>

      <div className="p-4 space-y-4">
        {/* Overall Score */}
        {analysis && (
          <div className="text-center">
            <div className={`inline-flex items-center justify-center w-16 h-16 rounded-full text-2xl font-bold ${getScoreBgColor(analysis.overall_score)} ${getScoreColor(analysis.overall_score)}`}>
              {analysis.overall_score}
            </div>
            <p className="text-sm text-gray-600 mt-2">Overall Score</p>
          </div>
        )}

        {/* Analysis Results */}
        {analysis && (
          <div className="space-y-3">
            {/* Syntax Analysis */}
            <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center">
                {analysis.syntax.valid ? (
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2" />
                ) : (
                  <XCircle className="w-4 h-4 text-red-600 mr-2" />
                )}
                <span className="text-sm font-medium">Syntax</span>
              </div>
              <span className={`text-sm font-semibold ${analysis.syntax.valid ? 'text-green-600' : 'text-red-600'}`}>
                {analysis.syntax.valid ? 'Valid' : 'Invalid'}
              </span>
            </div>

            {/* Runtime Analysis */}
            <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center">
                {analysis.runtime.success ? (
                  <CheckCircle className="w-4 h-4 text-green-600 mr-2" />
                ) : (
                  <XCircle className="w-4 h-4 text-red-600 mr-2" />
                )}
                <span className="text-sm font-medium">Runtime</span>
              </div>
              <span className={`text-sm font-semibold ${analysis.runtime.success ? 'text-green-600' : 'text-red-600'}`}>
                {analysis.runtime.success ? 'Success' : 'Failed'}
              </span>
            </div>

            {/* Execution Time */}
            <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center">
                <Clock className="w-4 h-4 text-blue-600 mr-2" />
                <span className="text-sm font-medium">Execution Time</span>
              </div>
              <span className="text-sm font-semibold text-blue-600">
                {analysis.runtime.execution_time.toFixed(3)}s
              </span>
            </div>

            {/* Complexity Analysis */}
            <div className="p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center mb-2">
                <Code2 className="w-4 h-4 text-purple-600 mr-2" />
                <span className="text-sm font-medium">Complexity</span>
              </div>
              <div className="text-xs text-gray-600">
                <div>Time: <span className="font-mono font-semibold">{analysis.complexity.time_complexity}</span></div>
                <div>Space: <span className="font-mono font-semibold">{analysis.complexity.space_complexity}</span></div>
              </div>
            </div>

            {/* Quality Score */}
            <div className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div className="flex items-center">
                <TrendingUp className="w-4 h-4 text-orange-600 mr-2" />
                <span className="text-sm font-medium">Quality</span>
              </div>
              <div className="text-right">
                <span className={`text-sm font-semibold ${getScoreColor(analysis.quality.score)}`}>
                  {analysis.quality.score}/100
                </span>
                <div className="text-xs text-gray-500">
                  Grade: {analysis.quality.grade}
                </div>
              </div>
            </div>

            {/* Quality Issues */}
            {analysis.quality.issues.length > 0 && (
              <div className="p-3 bg-yellow-50 rounded-lg border-l-4 border-yellow-400">
                <div className="flex items-center mb-2">
                  <AlertTriangle className="w-4 h-4 text-yellow-600 mr-2" />
                  <span className="text-sm font-medium text-yellow-800">Issues Found</span>
                </div>
                <ul className="text-xs text-yellow-700 space-y-1">
                  {analysis.quality.issues.map((issue, index) => (
                    <li key={index}>• {issue}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Runtime Output/Error */}
            {analysis.runtime.output && (
              <div className="p-3 bg-green-50 rounded-lg">
                <div className="text-sm font-medium text-green-800 mb-1">Output:</div>
                <pre className="text-xs text-green-700 bg-white p-2 rounded border overflow-x-auto">
                  {analysis.runtime.output}
                </pre>
              </div>
            )}

            {analysis.runtime.error && (
              <div className="p-3 bg-red-50 rounded-lg">
                <div className="text-sm font-medium text-red-800 mb-1">Error:</div>
                <pre className="text-xs text-red-700 bg-white p-2 rounded border overflow-x-auto">
                  {analysis.runtime.error}
                </pre>
              </div>
            )}
          </div>
        )}

        {/* Performance Metrics */}
        {metrics && (
          <div className="pt-4 border-t">
            <h4 className="text-sm font-semibold text-gray-700 mb-3">Session Metrics</h4>
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="flex justify-between">
                <span>Code Submissions:</span>
                <span className="font-semibold">{metrics.code_submissions}</span>
              </div>
              <div className="flex justify-between">
                <span>Hints Used:</span>
                <span className="font-semibold">{metrics.hints_used}</span>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default PerformancePanel;
