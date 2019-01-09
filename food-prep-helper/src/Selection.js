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

        return (
            <td name="dayCell" value={day}>
                <select name={this.selectionIndex} onChange={this.props.handleSelectionChange}>
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

    handleChange = event => {
        this.setState({recipesPicked: this.state.recipesPicked.concat([[event.target.name, event.target.value]])
        });
    }

    render() {
        const meals = ["Breakfast", "Lunch", "Dinner"];
        const { day, dayIndex } = this.props;

        const selectionCells = meals.map((meal) => {
            return (
                <SelectionCell onChange={this.handleChange} key={meal} day={day} meal={meal} dayIndex={dayIndex} handleSelectionChange={this.props.handleSelectionChange} />
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
    getRecipesFromServer() {
        return fetch('/select', {
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        })
            .then((response) => response.json())
            .then((responseJson) => {
                return responseJson;
            })
            .catch((error) => {
                console.error(error);
            });
    }
    
    render () {
        // TODO add options to list recipes with same meal from Python scripts
        // TODO add key:value (day+meal:recipe) to state variable and pass to
        // GroceryList component
        const { daysToPlanFor } = this.props;
        // make HTTP request here to fetch recipes from create.py fetch_recipes()
        const recipes = this.getRecipesFromServer();
        console.log(recipes);

        const selectionRows = daysToPlanFor.map((day, dayIndex) => {
            return (
                <SelectionRow recipes={recipes} day={day} dayIndex={dayIndex} handleSelectionChange={this.props.handleSelectionChange} />
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

        return (
            <table>
                <SelectionHeader />
                <SelectionBody daysToPlanFor={daysToPlanFor} handleSelectionChange={this.props.handleSelectionChange} />
            </table>
        );
    }
}

export default Selection;
