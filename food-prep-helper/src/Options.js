import React, { Component } from 'react';

const NavigationOptions = props => {
    const options = props.navigationOptions.map((option, index) => {
        return (
            <h1>{option}</h1>
        );
    });

    return (
            <div>{options}</div>
    );
}

class Options extends Component {
    render () {
        const { navigationOptions } = this.props;

        return (
            <div>
                <NavigationOptions navigationOptions={navigationOptions} />
            </div>
        );
    }
}

export default Options
