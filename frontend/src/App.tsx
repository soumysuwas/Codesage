// import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import HomePage from './components/HomePage';
import InterviewPage from './components/InterviewPage';
import './index.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Toaster position="top-right" />
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/interview/:id" element={<InterviewPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
