import React, { Component } from 'react';

// make each option it's own component? inside option component pass the onClick
// prop to a DOM's component onClick event

class NavigationOptions extends Component {
    handleClick = () => {
        console.log(this.props);
    }

    render () {
        const { navigationOptions } = this.props;
        const options = navigationOptions.map((option, index) => {
            return (
                // add href link to component with the option name?
                <th>
                    <a value={option} onClick={this.handleClick}>{option}</a>
                </th>
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
            <table>
                <NavigationOptions navigationOptions={navigationOptions} />
            </table>
        );
    }
}

export default Options;
