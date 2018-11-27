import React, { Component } from 'react';
import Options from './Options';
import Create from './Create';
import Selection from './Selection';

class App extends Component {
    state = {
        createOptions: [],
        daysToPlanFor: []
    };

    handleSubmit = createOption => {
        this.setState({createOptions: [...this.state.createOptions, createOption]});
    }
    
    // return daysToPlanFor before passing to Selection component?
    returnRecipeOptions = props => {
        var daysToPlanFor = [];
        const weekList = [
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
            var indexOfDayInWeekList = weekList.indexOf(props.createOptions[0].startDay);
            var dayToAdd = weekList[(indexOfDayInWeekList + 1 + i) % 7];
            daysToPlanFor.push(dayToAdd);
        }
        this.setState({daysToPlanFor: [...this.state.daysToPlanFor, daysToPlanFor]});
    }

    render() {
        // pass navigation options through as props since they don't need to be
        // modified
        const navigationOptions = ['Add', 'Edit', 'Create'];
        const { createOptions } = this.state;

        return (
            <div className="container">
                <Options navigationOptions={navigationOptions} />
                <Create handleSubmit={this.handleSubmit} />
                <Selection createOptions={createOptions}/>
            </div>
        );
    }
}

export default App;
