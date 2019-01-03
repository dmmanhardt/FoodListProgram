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

class SelectionCell extends Component {
    constructor(props) {
        super(props);
        const { day, meal, mealIndex } = this.props;

        this.initialState = {
            dayCell: {day},
            mealCell: {meal},
            recipePicked: "none",
        };

        this.state = this.initialState;
    }

    handleChange = event => {
        const {value} = event.target;

        this.setState({
            recipePicked: value,
        });
    }

    render() {
        const { dayCell, mealCell, recipePicked } = this.state;
        const { day, meal, mealIndex } = this.props;

        return (
            <td name="dayCell" value={day}>
                <select name={meal} onChange={this.handleChange}>
                    <option name="recipePicked" value="none"></option>
                    <option
                        name="recipePicked"
                        value="{recipe}">
                        "recipe"
                    </option>
                </select>
            </td>
        );
    }
}

class SelectionRow extends Component {
    constructor(props) {
        super(props);
        this.initialState = {
            recipesPicked: []
        };

        this.state = this.initialState;
    }
    // if meal/day in recipesPicked, replace recipePicked
    // else, concat
    // MOVE THIS TO MAIN SELECTION COMPONENT (highest component) or main app
    // which will then render GroceryList component
    handleChange = event => {
        this.setState({recipesPicked: this.state.recipesPicked.concat([[event.target.name, event.target.value]])
        });
    }

    render() {
        const meals = ["Breakfast", "Lunch", "Dinner"];
        const { day, dayIndex } = this.props;

        const selectionCells = meals.map((meal, mealIndex) => {
            return (
                <SelectionCell onChange={this.handleChange} key={mealIndex} day={day} meal={meal} index={mealIndex} />
            );
        });

        return (
            <tr onChange={this.handleChange}>
                <td name="day" value={day}>{day}</td>
                {selectionCells}
            </tr>
        );
    }
}

class SelectionBody extends Component {
    render () {
        // TODO add options to list recipes with same meal from Python scripts
        // TODO add key:value (day+meal:recipe) to state variable and pass to
        // GroceryList component
        // const { recipesPicked } = this.state;
        const { daysToPlanFor } = this.props;

        const selectionRows = daysToPlanFor.map((day, dayIndex) => {
            return (
                <SelectionRow key={dayIndex} day={day} index={dayIndex} />
            );
        });

        return (
            <tbody>{selectionRows}</tbody>
        );
    }
}
// add day:meal as state and update that for each child?
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
