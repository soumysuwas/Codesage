import React, { useState } from 'react';
import { Editor } from '@monaco-editor/react';
import { Play, RotateCcw, Settings } from 'lucide-react';

interface CodeEditorProps {
  code: string;
  language: string;
  onChange: (code: string) => void;
  onLanguageChange: (language: string) => void;
  onRun: () => void;
  onReset: () => void;
  isRunning?: boolean;
}

const CodeEditor: React.FC<CodeEditorProps> = ({
  code,
  language,
  onChange,
  onLanguageChange,
  onRun,
  onReset,
  isRunning = false
}) => {
  const [showSettings, setShowSettings] = useState(false);

  const languages = [
    { value: 'python', label: 'Python' },
    { value: 'javascript', label: 'JavaScript' },
    { value: 'java', label: 'Java' },
    { value: 'cpp', label: 'C++' }
  ];

  const defaultCode = {
    python: `def solution():
    # Write your solution here
    pass`,
    javascript: `function solution() {
    // Write your solution here
}`,
    java: `public class Solution {
    public static void main(String[] args) {
        // Write your solution here
    }
}`,
    cpp: `#include <iostream>
using namespace std;

int main() {
    // Write your solution here
    return 0;
}`
  };

  const handleLanguageChange = (newLanguage: string) => {
    onLanguageChange(newLanguage);
    if (code.trim() === '' || code === defaultCode[language as keyof typeof defaultCode]) {
      onChange(defaultCode[newLanguage as keyof typeof defaultCode]);
    }
  };

  return (
    <div className="card">
      <div className="card-header">
        <div className="flex items-center justify-between">
          <h3 className="card-title">Code Editor</h3>
          <div className="flex items-center space-x-2">
            <button
              onClick={() => setShowSettings(!showSettings)}
              className="btn btn-secondary"
              title="Settings"
            >
              <Settings className="w-4 h-4" />
            </button>
            <button
              onClick={onReset}
              className="btn btn-secondary"
              title="Reset Code"
            >
              <RotateCcw className="w-4 h-4" />
            </button>
            <button
              onClick={onRun}
              disabled={isRunning}
              className="btn btn-primary"
              title="Run Code"
            >
              <Play className="w-4 h-4" />
              {isRunning ? 'Running...' : 'Run'}
            </button>
          </div>
        </div>
        
        {showSettings && (
          <div className="mt-4 p-4 bg-gray-50 rounded-lg">
            <div className="form-group">
              <label className="form-label">Programming Language</label>
              <select
                value={language}
                onChange={(e) => handleLanguageChange(e.target.value)}
                className="form-input"
              >
                {languages.map((lang) => (
                  <option key={lang.value} value={lang.value}>
                    {lang.label}
                  </option>
                ))}
              </select>
            </div>
          </div>
        )}
      </div>

      <div className="code-editor-container">
        <Editor
          height="100%"
          language={language}
          value={code}
          onChange={(value) => onChange(value || '')}
          theme="vs-dark"
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            lineNumbers: 'on',
            roundedSelection: false,
            scrollBeyondLastLine: false,
            automaticLayout: true,
            wordWrap: 'on',
            wrappingIndent: 'indent',
            selectOnLineNumbers: true,
            renderLineHighlight: 'all',
            cursorStyle: 'line',
            cursorBlinking: 'blink',
            cursorSmoothCaretAnimation: true,
            smoothScrolling: true,
            contextmenu: true,
            mouseWheelZoom: true,
            multiCursorModifier: 'ctrlCmd',
            formatOnPaste: true,
            formatOnType: true,
            suggestOnTriggerCharacters: true,
            acceptSuggestionOnEnter: 'on',
            tabCompletion: 'on',
            wordBasedSuggestions: 'matchingDocuments',
            parameterHints: { enabled: true },
            hover: { enabled: true },
            folding: true,
            foldingStrategy: 'indentation',
            showFoldingControls: 'always',
            unfoldOnClickAfterEnd: false,
            bracketPairColorization: { enabled: true },
            guides: {
              bracketPairs: true,
              indentation: true,
              highlightActiveIndentation: true
            }
          }}
        />
      </div>
    </div>
  );
};

export default CodeEditor;
