import React, { Component } from 'react';
import Options from './Options';
import Create from './Create';
import Selection from './Selection';
import GroceryList from './GroceryList';
import Add from './Add';

class App extends Component {
    state = {
        createOptions: [],
        daysToPlanFor: [],
        recipesPicked: [],
        recipes: []
    };

    componentDidMount() {
        const url = "http://localhost:5000/select";

        fetch(url)
            .then(result => result.json())
            .then(result => {
                this.setState({
                    recipes: result
                })
            });
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
        // pass navigation options through as props since they don't need to be
        // modified. NOT IMPLEMENTED CURRENTLY
        const navigationOptions = ['Add', 'Edit', 'Create'];
        const { createOptions } = this.state;
        const { daysToPlanFor } = this.state;
        const { recipesPicked } = this.state;
        const { recipes } = this.state;

        return (
            <div className="container">
                <Options navigationOptions={navigationOptions} />
                <Create handleSubmit={this.handleSubmit} />
                <Selection daysToPlanFor={daysToPlanFor} recipes={recipes} handleSelectionChange={this.handleSelectionChange} />
                <GroceryList recipesPicked={recipesPicked} />
                {/* <Add /> */}
            </div>
        );
    }
}

export default App;
