import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Add from './Add';
import App from './App';

// make each option it's own component? inside option component pass the onClick
// prop to a DOM's component onClick event

const Index = () => <h2>Home</h2>
const Edit = () => <h2>Edit Recipe</h2>

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

            <Route path="/" exact component={Index} />
            <Route path="/add/" component={Add} />
            <Route path="/edit/" component={Edit} />
        </div>
    </Router>
);

// class NavigationOptions extends Component {
//     // todo: change this to render appropriate pick (ie add recipe when add is clicked)
//     handleClick = () => {
//         console.log(this.props);
//     }

//     render () {
//         const { navigationOptions } = this.props;
//         const options = navigationOptions.map((option, index) => {
//             return (
//                 // add href link to component with the option name?
//                 <th>
//                     <a value={option} onClick={this.handleClick}>{option}</a>
//                 </th>
//             );
//         });

//         return (
//                 <div>{options}</div>
//         );
//     }
// }

// class Options extends Component {
//     render () {
//         const { navigationOptions } = this.props;

//         return (
//             <table>
//                 <NavigationOptions navigationOptions={navigationOptions} />
//             </table>
//         );
//     }
// }

export default AppRouter;
