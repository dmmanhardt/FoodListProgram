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

// set state of each select element to be meal and recipe picked
// add this to recipesPicked array of SelectionBody. (ie will be able to map
// and do row.meal, row.day, row.recipe)

//render SelectionRow from SelectionBody, SelectionRow maps over meals and
//renders 3 SelectionCell for each

class SelectionRow extends Component {
    render() {
        const meals = ["Breakfast", "Lunch", "Dinner"];

        const selectionCells = meals.map((meal, index) => {
            return (
                <SelectionCell />
            );
        });

        return (
            <tr>{selectionCells}</tr>
        );
    }
}

class SelectionCell extends Component {
    constructor(props) {
        super(props);
        this.initialState = {
            day: '',
            meal: '',
            recipePicked: ''
        };

        this.state = this.initialState;
    }

    handleChange = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
    }

    render() {
        const { day, meal, recipePicked } = this.state;

        return (
            <td name="day" value="{day}" onChange={this.handleChange}>
                <select name="meal" value="{meal}" onChange={this.handleChange}>
                    <option value="none"></option>
                    <option
                        name="recipePicked"
                        value="recipe">
                        Recipe for meal
                    </option>
                </select>
            </td>
        );
    }
}

// TODO for each day,meal pair, there should be one recipe selection. Push that
// to recipesPicked array onChange, or handle by onSubmit. If not, would need
// to be able to change recipe for day, meal in array
class SelectionBody extends Component {
    constructor(props) {
        super(props);
        this.initialState = {
            recipesPicked: []
        };

        this.state = this.initialState;
    }

    handleChange = event => {
        const { recipe, value } = event.target;

        console.log("handle change");

        this.setState({
            [recipe] : value
        });
    }

    render () {
        // TODO add options to list recipes with same meal from Python scripts
        // TODO add key:value (day+meal:recipe) to state variable and pass to
        // GroceryList component
        const { recipesPicked } = this.state;
        const { daysToPlanFor } = this.props;

        const selectionRows = daysToPlanFor.map((day, index) => {
            return (
                <SelectionRow />
            );
        });

        return (
            <tbody onChange={this.handleChange}>{selectionRows}</tbody>
        );
    }
}

class Selection extends Component {
    render () {
        const { daysToPlanFor } = this.props;

        return (
            <table>
                <SelectionHeader />
                <SelectionBody daysToPlanFor={daysToPlanFor} />
            </table>
        );
    }
}

export default Selection;
