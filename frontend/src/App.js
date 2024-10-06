import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import RecipesList from './components/RecipesList';
import ChatBot from './components/chatBot';
import CheckBot from './components/CheckBot';
import Items from './components/Items';
import MainLayout from './components/MainLayout';  // Import the layout
import Profile from './components/profile';  // Import the profile component

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
        {/* Wrap all main pages with MainLayout */}
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<MainLayout><ChatBot /></MainLayout>} />
        <Route path="/recipes" element={<MainLayout><RecipesList /></MainLayout>} />
        <Route path="/chatbot" element={<MainLayout><ChatBot /></MainLayout>} />
        <Route path="/chatbot" element={<MainLayout><ChatBot /></MainLayout>} />
        <Route path="/items" element={<MainLayout><Items /></MainLayout>} />
        <Route path="/profile" element={<MainLayout><Profile /></MainLayout>} />
      </Routes>
    </Router>
  );
};

export default App;


// import React from 'react';
// import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
// import Login from './components/Login';
// import Signup from './components/Signup';
// import RecipesList from './components/RecipesList';
// import ChatBot from './components/chatBot';
// import HomePage from './components/HomePage';
// import CheckBot from './components/CheckBot';  // Create a placeholder component for CheckBot
// import Items from './components/Items';  // Create a placeholder component for Items


// const App = () => {
//   return (
//     <Router>
//       <div>
//         <Routes>
//           <Route path="/login" element={<Login />} />
//           <Route path="/signup" element={<Signup />} />
//           <Route path="/recipes" element={<RecipesList />} /> {/* Recipes list page */}
//           <Route path="/" element={<Login />} /> {/* Default route redirects to login */}
//           <Route path="/chat" element={<ChatBot />} /> {/* Recipes list page */}
//           <Route path='/home' element={<HomePage />} /> {/*home page */}
//           <Route path="/checkbot" element={<CheckBot />} />  {/* CheckBot route */ }
//           <Route path="/items" element={<Items />} />  {/* Items route */ }
//         </Routes>
//       </div>
//     </Router>
//   );
// };

// export default App;
