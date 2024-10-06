// src/components/Login.jsx
import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import '../styles/Auth.css';  // Import the enhanced Auth styling

const Login = () => {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [error, setError] = useState(''); // State for error messages
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
    setError(''); // Clear error message on input change
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(''); // Reset error message

    try {
      const response = await axios.post('http://localhost:8000/users/login/', formData);
      localStorage.setItem('userId', response.data.userId);
      console.log('userId saved to localStorage:', response.data.userId);  // Debug log

      navigate('/recipes');
    } catch (error) {
      console.error('Error logging in:', error);
      if (error.response && error.response.data && error.response.data.error) {
        setError(error.response.data.error); // Display backend error message
      } else {
        setError('An unexpected error occurred. Please try again.');
      }
    }
  };

  return (
    <div className="auth-container">
      <div className="logo">FoodFlix</div> {/* FoodFlix Title/Logo */}
      <h2>Login</h2>
      {error && <div className="error-message">{error}</div>} {/* Display error message */}
      <form onSubmit={handleSubmit}>
        <input 
          type="email" 
          name="email" 
          placeholder="Email" 
          onChange={handleChange} 
          value={formData.email} 
          required
        />
        <input 
          type="password" 
          name="password" 
          placeholder="Password" 
          onChange={handleChange} 
          value={formData.password} 
          required
        />
        <button type="submit">Login</button>
      </form>
      <div className="auth-link">
        <p>Don't have an account? <Link to="/signup">Sign Up</Link></p>
      </div>
    </div>
  );
};

export default Login;
