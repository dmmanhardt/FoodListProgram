import React, { Component } from 'react';
import Options from './Options';
import Create from './Create';
import Selection from './Selection';

class App extends Component {
    state = {
        createOptions: []
    };

    handleSubmit = createOption => {
        this.setState({createOptions: [...this.state.createOptions, createOption]});
    }

    render() {
        // pass navigation options through as props since they don't need to be
        // modified
        const navigationOptions = ['Add', 'Edit', 'Create'];
        const { createOptions } = this.state;

        return (
            <div className="container">
                <Options navigationOptions={navigationOptions} />
                <Create handleSubmit={this.handleSubmit} />
                <Selection createOptions={createOptions}/>
            </div>
        );
    }
}

export default App;
