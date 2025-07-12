"use client";
import React, { useState } from "react";
import ResultCard from "./components/ResultCard/ResultCard";
import "./globals.css";

export default function App() {
  const [symptomText, setSymptomText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleCheck = async () => {
    if (!symptomText.trim()) return;

    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text: symptomText }),
      });

      const data = await res.json();
      setResult(data);
    } catch (error) {
      console.error(error);
      alert("Couldn't connect to backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      {/* 🌟 Logo and Header Text */}
      <header className="app-header">
        <img src="/logo.png" alt="Disease Predictor Logo" className="logo" />
        <h2 className="app-subtitle">
          Welcome to the AI-Powered Disease Predictor
        </h2>
      </header>

      {/* 🔥 Hero Section */}
      <div className="hero">
        <div className="hero-content">
          <h1>Describe Your Symptoms</h1>
          <p>
            Our intelligent system will suggest a possible disease along with
            useful advice.
          </p>

          <textarea
            placeholder="e.g., I feel tired, have sore throat and headache..."
            value={symptomText}
            onChange={(e) => setSymptomText(e.target.value)}
          ></textarea>

          {loading ? (
            <button disabled>
              <span className="loader"></span> Checking...
            </button>
          ) : (
            <button onClick={handleCheck}>Check Disease</button>
          )}
        </div>
      </div>

      {/* ✅ Result Cards */}
      {result?.predictions?.map((prediction, index) => (
        <ResultCard key={index} data={prediction} />
      ))}
    </div>
  );
}
