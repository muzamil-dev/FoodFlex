import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/HomePage.css';  // We'll add some styling here

const HomePage = () => {
  return (
    <div className="home-container">
      {/* Sidebar */}
      <div className="sidebar">
        <div className="profile-icon">
          <img src="/path-to-icon" alt="Profile" className="profile-img" />
        </div>
        <nav>
          <ul>
            <li>
              <Link to="/chat">RecipeBot</Link>
            </li>
            <li>
              <Link to="/chat">CheckBot</Link>
            </li>
            <li>
              <Link to="/recipes">Recipes</Link>
            </li>
            <li>
              <Link to="/items">Items</Link>
            </li>
          </ul>
        </nav>
      </div>

      {/* Main Content Area */}
      <div className="main-content">
        <h1>Welcome to the Home Page</h1>
        <div className="cards">
          {/* Example Cards */}
          <div className="card">Card 1</div>
          <div className="card">Card 2</div>
          <div className="card">Card 3</div>
          <div className="card">Card 4</div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
