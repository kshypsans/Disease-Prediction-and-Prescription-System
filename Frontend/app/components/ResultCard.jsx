import React from 'react';

export default function ResultCard({ data }) {
  return (
    <div className="result-card">
      <h3>{data.disease} <span className="confidence">({data.confidence}%)</span></h3>
      <p className="description">{data.description}</p>

      <div className="section">
        <h4>🛡 Precautions</h4>
        {data.precautions.length > 0 ? (
          <ul>
            {data.precautions.map((p, i) => <li key={i}>{p}</li>)}
          </ul>
        ) : (
          <p>No precautions provided.</p>
        )}
      </div>

      <div className="section">
        <h4>🥗 Diet</h4>
        {data.diet.length > 0 ? (
          <ul>
            {data.diet.map((d, i) => <li key={i}>{d}</li>)}
          </ul>
        ) : (
          <p>No diet advice provided.</p>
        )}
      </div>

      <div className="section">
        <h4>🛌 Rest Advice</h4>
        <p>{data.rest || 'No rest advice provided.'}</p>
      </div>
    </div>
  );
}
