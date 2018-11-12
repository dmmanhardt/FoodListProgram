import React, { Component } from 'react';
import Options from './Options';
import CreateList from './CreateList';

class App extends Component {
    render() {
        // pass navigation options through as props since they don't need to be
        // modified
        const navigationOptions = ['Add', 'Edit', 'Create'];

        return (
            <div className="container">
                <Options navigationOptions={navigationOptions} />
            </div>
        );
    }
}

export default App;
