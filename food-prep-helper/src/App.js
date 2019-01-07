import React, { Component } from 'react';
import Options from './Options';
import Create from './Create';
import Selection from './Selection';

class App extends Component {
    state = {
        createOptions: [],
        daysToPlanFor: [],
        recipesPicked: {}
    };

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
        for (let i = 0; i < createOption.numberDays; i++) {
            var indexOfDayInWeekList = weekList.indexOf(createOption.startDay);
            var dayToAdd = weekList[(indexOfDayInWeekList + i) % 7];
            updatedArray.push(dayToAdd);
        }
        this.setState({daysToPlanFor: updatedArray
        });
    }

    // create state variable for each when Selection is first rendered and
    // default their value to "none" (because if user doesn't change a cell's
    // selection, the state variable for that cell in app is never declared)

    // OR create object for each mealCell and recipePicked can be mealCell.recipePicked?
    handleSelectionChange = recipePicked => {
        // this is a nested state and should be avoided
        // this.setState({recipesPicked: {[recipePicked.target.name]: recipePicked.target.value}});

        this.setState({[recipePicked.target.name]: recipePicked.target.value});
        const stateVariables = [this.state];
        this.setState({stateVariables: stateVariables});

        // for (let i = 0; i < stateVariables.length; i++) {
        //     if (stateVariables[i] === 'createOptions' || stateVariables[i] === 'daysToPlanFor' || stateVariables[i] === 'recipesPicked') {
        //         continue
        //     }else{
        //         this.setState({[this.state.recipesPicked]: stateVariables[i]});
        //     }
        // }
    }

// render GroceryList component by going through state and adding any besides createOptions
// and daysToPlanFor to recipesPicked, pass recipes picked to python function that calculates
// ingredient info

    render() {
        // pass navigation options through as props since they don't need to be
        // modified
        const navigationOptions = ['Add', 'Edit', 'Create'];
        const { createOptions } = this.state;
        const { daysToPlanFor } = this.state;
        const { recipesPicked } = this.state;

        return (
            <div className="container">
                <Options navigationOptions={navigationOptions} />
                <Create handleSubmit={this.handleSubmit} />
                <Selection daysToPlanFor={daysToPlanFor} handleSelectionChange={this.handleSelectionChange} />
            </div>
        );
    }
}

export default App;
