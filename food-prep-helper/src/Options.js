import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Add from './Add';
import Edit from './Edit';
import App from './App';

// make each option it's own component? inside option component pass the onClick
// prop to a DOM's component onClick event

class AppRouter extends Component {
    state = {
        recipes: []
    };

    componentDidMount() {
        const url = "http://localhost:5000/select";

        fetch(url)
            .then(result => result.json())
            .then(result => {
                this.setState({
                    recipes: result
                })
            });
    }

    render() {
        const { recipes } = this.state;

        return (
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

                    <Route path="/" exact component={(props) => <App recipes={recipes} {...props} />} />
                    <Route path="/add/" component={Add} />
                    <Route path="/edit/" render={(props) => <Edit recipes={recipes} {...props} />} />
                </div>
            </Router>
        );
    }
}

export default AppRouter;
