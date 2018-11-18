import React, { Component } from 'react';

const SelectionHeader = () => {
    return (
        <thead>
            <tr>
                <th>Day</th>
                <th>Breakfast</th>
                <th>Lunch</th>
                <th>Dinner</th>
            </tr>
        </thead>
    );
}

const SelectionDays = props => {
    const rows = props.createOptions.map((row, index) => {
        return (
            <tr key={index}>
                <td>{row.startDay}</td>
                <td>{row.numberDays}</td>
                <td>{index}</td>
            </tr>
        );
    });

    return (
        <tbody>{rows}</tbody>
    );
}

class Selection extends Component {
    render () {
        const { createOptions } = this.props;

        return (
            <table>
                <SelectionHeader />
                <SelectionDays createOptions={createOptions} />
            </table>
        );
    }
}

export default Selection;
