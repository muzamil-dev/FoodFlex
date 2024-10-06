// MainLayout.js
import React from 'react';
import Sidebar from './Sidebar';
import '../styles/HomePage.css';  // Import your styles here

const MainLayout = ({ children }) => {
  return (
    <div className="home-container">
      <Sidebar />
      <div className="main-content">
        {children}  {/* This will load the dynamic content */}
      </div>
    </div>
  );
};

export default MainLayout;
