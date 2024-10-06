// Sidebar.js
import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Sidebar.css';  // Correct path to your CSS file

const Sidebar = () => {
  return (
    <div className="sidebar">
      <ul>
        <li><Link to="/chatbot">ChatBot</Link></li>  {/* Correct path without /home */}
        <li><Link to="/checkbot">CheckBot</Link></li>
        <li><Link to="/recipes">Recipes</Link></li>
        <li><Link to="/items">Items</Link></li>
      </ul>
    </div>
  );
};

export default Sidebar;
