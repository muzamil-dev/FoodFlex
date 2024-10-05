import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import RecipeList from './components/RecipeList';
import './App.css';

function App() {
    return (
        <Router>
            <div className="App">
                <Switch>
                    <Route path="/login">
                        <Login />
                    </Route>
                    <Route path="/">
                        <RecipeList />
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}

export default App;
