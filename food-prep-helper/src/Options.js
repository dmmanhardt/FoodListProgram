import React, { Component } from 'react';

// make each option it's own component? inside option component pass the onClick
// prop to a DOM's component onClick event

class NavigationOptions extends Component {
    render () {
        const { navigationOptions } = this.props;

        const options = navigationOptions.map((option, index) => {
            return (
                <h1 className={index} onClick={this.props.onClick}>{option}</h1>
            );
        });

        return (
                <div>{options}</div>
        );
    }
}

class Options extends Component {
    render () {
        const { navigationOptions } = this.props;

        return (
            <div className="container">
                <NavigationOptions navigationOptions={navigationOptions} />
            </div>
        );
    }
}

export default Options;
