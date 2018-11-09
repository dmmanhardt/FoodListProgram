import React, { Component } from 'react';

class App extends Component {
    state = {
        options: ['add', 'edit', 'create']
    };

    pickOption = index => {
        const { options } = this.state;
    };

    render() {
        const { options } = this.state;

        return (
            <div className="container">
                <h1>{ options }</h1>
            </div>
        );
    }
}

export default App;
