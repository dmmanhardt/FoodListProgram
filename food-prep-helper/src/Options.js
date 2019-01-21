import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Add from './Add';
import Edit from './Edit';
import App from './App';

// make each option it's own component? inside option component pass the onClick
// prop to a DOM's component onClick event

const AppRouter = () => (
    <Router>
        <div>
            <nav>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/add/">Add Recipe</Link>
                    </li>
                    <li>
                        <Link to="/edit/">Edit Recipe</Link>
                    </li>
                </ul>
            </nav>

            <Route path="/" exact component={App} />
            <Route path="/add/" component={Add} />
            <Route path="/edit/" render={(props) => <Edit {...props} />} />
        </div>
    </Router>
);

export default AppRouter;
