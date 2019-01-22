import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import Options from './Options';
import Create from './Create';
import Selection from './Selection';
import GroceryList from './GroceryList';
import Add from './Add';
import Edit from './Edit';

class App extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            createOptions: [],
            daysToPlanFor: [],
            recipesPicked: [],
        };

        this.state = this.initialState;
    }

    handleSubmit = createOption => {
        this.setState({createOptions: [...this.state.createOptions, createOption]});
        const updatedArray = [...this.state.daysToPlanFor];
        const weekList = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday"
        ];

        // creates array containing name of weekday for each day to plan for
        for (let i = 0; i < createOption.numberDays; i++) {
            var indexOfDayInWeekList = weekList.indexOf(createOption.startDay);
            var dayToAdd = weekList[(indexOfDayInWeekList + i) % 7];
            updatedArray.push(dayToAdd);
        }
        this.setState({daysToPlanFor: updatedArray});
        this.updateSelectionCellIndexes(updatedArray);
    }

    // create array with all selectionCell indexes and declare it in state
    // the call function to create state variable for each selectionCell 
    // index here so that state object can be updated in handleSelectionChange
    updateSelectionCellIndexes(daysToPlanFor) {
        var selectionCellIndexes = [];
        for (let i = 0; i < daysToPlanFor.length; i++) {
            selectionCellIndexes.push(i + 'Breakfast');
            selectionCellIndexes.push(i + 'Lunch');
            selectionCellIndexes.push(i + 'Dinner');    
        }
        this.setState({selectionCellIndexes: selectionCellIndexes});
        this.addSelectionCellIndexToState(selectionCellIndexes);
    }

    addSelectionCellIndexToState(selectionCellIndexes) {
        for (let i = 0; i < selectionCellIndexes.length; i++) {
            this.setState({[selectionCellIndexes[i]]: "none"});
        }
    }

    handleSelectionChange = recipePicked => {
        // copy current state, change value of selectionCell that was just changed
        // go through all selectionCells and update recipesPicked with their values
        // update state with updated recipesPicked
        var currentState = this.state;
        currentState[recipePicked.target.name] = recipePicked.target.value;
        var updatedRecipesPicked = this.state.selectionCellIndexes.map(selectionCell => currentState[selectionCell]);
        this.setState({recipesPicked: updatedRecipesPicked});
    }

// render GroceryList component by going through state and adding any besides createOptions
// and daysToPlanFor to recipesPicked, pass recipes picked to python function that calculates
// ingredient info

    render() {
        const { daysToPlanFor } = this.state;
        const { recipesPicked } = this.state;
        const { recipes } = this.props;

        return (
            <div className="Container">
                <Create handleSubmit={this.handleSubmit} />
                <Selection daysToPlanFor={daysToPlanFor} recipes={recipes} handleSelectionChange={this.handleSelectionChange} />
                <GroceryList recipesPicked={recipesPicked} />
            </div>
        );
    }
}

export default App;
