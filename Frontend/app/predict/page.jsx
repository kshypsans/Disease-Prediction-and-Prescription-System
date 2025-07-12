'use client';

import { useState } from 'react';
import axios from 'axios';
import ResultCard from '../components/ResultCard/ResultCard';

export default function PredictPage() {
  const [input, setInput] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    setLoading(true);
    setResults([]);

    try {
      const res = await axios.post('http://localhost:5000/predict', {
        text: input,
      });
      setResults(res.data.predictions);
    } catch (error) {
      alert("Failed to fetch predictions. Is the backend running?");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h2>Disease Predictor</h2>
      <form onSubmit={handleSubmit}>
        <textarea
          rows={5}
          placeholder="Describe your symptoms..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
        />
        <button type="submit">{loading ? 'Predicting...' : 'Predict Disease'}</button>
      </form>

      {results.map((res, i) => (
        <ResultCard key={i} data={res} />
      ))}
    </div>
  );
}
