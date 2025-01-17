// src/App.jsx
import { useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [review, setReview] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const analyzeSentiment = async () => {
    if (!review.trim()) {
      setError('Please enter a review')
      return
    }

    setLoading(true)
    setError(null)
    try {
      const formData = new FormData()
      formData.append('text', review)

      const response = await axios.post('http://localhost:8000/sentiment-analysis', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      setResult(response.data)
    } catch (err) {
      console.error('Error:', err)
      setError('Error analyzing sentiment. Please try again.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white flex flex-col items-center py-8 px-4">
      {/* Title and Subtitle */}
      <div className="w-full max-w-5xl text-center mb-8">
        <h1 className="text-5xl font-bold text-blue-400 mb-4">Sentiment Analyzer</h1>
        <p className="text-gray-400 text-xl">
          Analyze the sentiment of a movie review using AI-powered natural language processing.
        </p>
      </div>

      {/* Input Section */}
      <div className="w-full max-w-5xl bg-gray-800 rounded-md p-8 shadow-lg">
        <h2 className="text-2xl font-semibold mb-4">Enter Your Review</h2>
        <textarea
          className="w-full bg-gray-700 text-white p-4 rounded-md border border-gray-600 focus:outline-none focus:border-blue-500 resize-none"
          style={{ minHeight: '400px' }}
          placeholder="Write your detailed movie review here..."
          value={review}
          onChange={(e) => setReview(e.target.value)}
        />
        <button
          className={`w-full py-3 mt-4 text-lg font-medium rounded-md transition ${
            loading
              ? 'bg-gray-600 cursor-not-allowed'
              : 'bg-blue-600 hover:bg-blue-700'
          }`}
          onClick={analyzeSentiment}
          disabled={loading}
        >
          {loading ? 'Analyzing...' : 'Analyze Sentiment'}
        </button>

        {/* Error Message */}
        {error && <p className="text-red-500 text-center mt-4">{error}</p>}

        {/* Result Section */}
        {result && (
          <div className="bg-gray-700 mt-6 p-6 rounded-md shadow-md">
            <h3 className="text-lg font-medium mb-2 text-blue-400">Analysis Result</h3>
            <p className="text-white text-lg mb-1">
              {result.message}
              <span role="img" aria-label="emoji" className="ml-2">
                {result.sentiment === 'Positive'
                  ? '😊'
                  : result.sentiment === 'Negative'
                  ? '😞'
                  : '😐'}
              </span>
            </p>
            <p className="text-gray-400">
              Confidence Score: {result.confidence.toFixed(1)}% ({result.sentiment})
            </p>
          </div>
        )}
      </div>
    </div>
  )
}

export default App
