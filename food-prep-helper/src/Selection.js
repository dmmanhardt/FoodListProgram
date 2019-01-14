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
        const { day, meal, dayIndex } = this.props;
        this.selectionIndex = dayIndex + meal;

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
        const { recipes } = this.props;

        return (
            <td name="dayCell" value={day}>
                <select name={this.selectionIndex} onChange={this.props.handleSelectionChange}>
                    <option name="recipePicked" value="none"></option>
                    { recipes.map(recipe => {
                        if(recipe["meal_served"] === meal)
                            return <option name="recipePicked" value={recipe["recipe_name"]}>
                                        {recipe["recipe_name"]}                                    
                                    </option>
                    })}
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

    handleChange = event => {
        this.setState({recipesPicked: this.state.recipesPicked.concat([[event.target.name, event.target.value]])
        });
    }

    render() {
        const meals = ["Breakfast", "Lunch", "Dinner"];
        const { day, dayIndex } = this.props;
        const { recipes } = this.props;

        const selectionCells = meals.map((meal) => {
            return (
                <SelectionCell onChange={this.handleChange} recipes={recipes} key={meal} day={day} meal={meal} dayIndex={dayIndex} handleSelectionChange={this.props.handleSelectionChange} />
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

// change the fetch location, probably need to reorganize the file
// structure first
class SelectionBody extends Component {     
    render () {
        const { daysToPlanFor } = this.props;
        const { recipes } = this.props;

        const selectionRows = daysToPlanFor.map((day, dayIndex) => {
            return (
                <SelectionRow day={day} dayIndex={dayIndex} recipes={recipes} handleSelectionChange={this.props.handleSelectionChange} />
            );
        });

        return (
            <tbody>{selectionRows}</tbody>
        );
    }
}

class Selection extends Component {
    render () {
        const { daysToPlanFor } = this.props;
        const { recipes } = this.props;

        return (
            <table>
                <SelectionHeader />
                <SelectionBody daysToPlanFor={daysToPlanFor} recipes={recipes} handleSelectionChange={this.props.handleSelectionChange} />
            </table>
        );
    }
}

export default Selection;
