import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import RecipesList from './components/RecipesList';
import ChatBot from './components/chatBot';
import HomePage from './components/HomePage';
import CheckBot from './components/CheckBot';  // Create a placeholder component for CheckBot
import Items from './components/Items';  // Create a placeholder component for Items


const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/recipes" element={<RecipesList />} /> {/* Recipes list page */}
          <Route path="/" element={<Login />} /> {/* Default route redirects to login */}
          <Route path="/chat" element={<ChatBot />} /> {/* Recipes list page */}
          <Route path='/home' element={<HomePage />} /> {/*home page */}
          <Route path="/checkbot" element={<CheckBot />} />  {/* CheckBot route */ }
          <Route path="/items" element={<Items />} />  {/* Items route */ }
        </Routes>
      </div>
    </Router>
  );
};

export default App;
