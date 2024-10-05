import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import '../Auth.css';  // Import the Auth styling

const Login = () => {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/users/login/', formData)
      .then((response) => {
        localStorage.setItem('token', response.data.token);
        navigate('/recipes');
      })
      .catch((error) => {
        console.error('Error logging in:', error);
      });
  };

  return (
    <div className="auth-container">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          name="email" 
          placeholder="email" 
          onChange={handleChange} 
          value={formData.email} 
        />
        <input 
          type="password" 
          name="password" 
          placeholder="Password" 
          onChange={handleChange} 
          value={formData.password} 
        />
        <button type="submit">Login</button>
      </form>
      <div className="auth-link">
        <p>Don't have an account? <a href="/signup">Sign Up</a></p>
      </div>
    </div>
  );
};

export default Login;
