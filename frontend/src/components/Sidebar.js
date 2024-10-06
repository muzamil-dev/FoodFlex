import React from 'react';
import { NavLink } from 'react-router-dom';
import '../styles/Sidebar.css';  // Correct path to your CSS file

const Sidebar = () => {
  return (
    <div className="sidebar">
      <ul>
        <li>
        <li>
          <NavLink to="/profile" activeClassName="active">
            Profile
          </NavLink>
        </li>
          <NavLink to="/chatbot" activeClassName="active">
            ChatBot
          </NavLink>
        </li>
        <li>
          <NavLink to="/checkbot" activeClassName="active">
            CheckBot
          </NavLink>
        </li>
        <li>
          <NavLink to="/recipes" activeClassName="active">
            Recipes
          </NavLink>
        </li>
        <li>
          <NavLink to="/items" activeClassName="active">
            Items
          </NavLink>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;
