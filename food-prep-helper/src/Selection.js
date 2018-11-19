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

class RecipeOption extends Component {
    render() {
        const { createOptions } = this.props;

        return (
            <select>
                <option value="none"></option>
                <ReturnRecipeOptions createOptions={createOptions} />
            </select>
        );
    }
}

const ReturnRecipeOptions = props => {
    const meals = ["Breakfast", "Lunch", "Dinner"];
    const week = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
    ];

    for (let i = 0; i < props.createOptions[0].numberDays; i++) {
        // todo: get corresponding index of startDay from week
        var daysToPlanFor = [week[(props.createOptions[0].startDay + 1 + i) % 7]];
        console.log(props.createOptions[0].startDay);
        console.log(week["Monday"]);
    }
    return (
        <option>{daysToPlanFor}</option>
    );
}

class SelectionDays extends Component {
    // change this to get days from python file (if starting on monday with 4 Days
    // python should return Monday, Tuesday, Wednesday, Thursday), then this
    // function should return as a row: day, dropdown, dropdown, dropdown with
    // each dropdown containing available recipes
    render () {
        const { createOptions } = this.props;
        const rows = createOptions.map((row, index) => {
            // change the select elements to be their own components
            return (
                <tr key={index}>
                    <td>{row.startDay}</td>
                    <td>
                        <RecipeOption createOptions={createOptions} />
                    </td>
                    <td>
                        <RecipeOption createOptions={createOptions} />
                    </td>
                    <td>
                        <RecipeOption createOptions={createOptions} />
                    </td>
                </tr>
            );
        });

        return (
            <tbody>{rows}</tbody>
        );
    }
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
