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
            </select>
        );
    }
}

// const ReturnRecipeOptions = props => {
//     var daysToPlanFor = [];
//     const weekList = [
//         "Sunday",
//         "Monday",
//         "Tuesday",
//         "Wednesday",
//         "Thursday",
//         "Friday",
//         "Saturday"
//     ];
//
//     for (let i = 0; i < props.createOptions[0].numberDays; i++) {
//         // todo: get corresponding index of startDay from week
//         var indexOfDayInWeekList = weekList.indexOf(props.createOptions[0].startDay);
//         var dayToAdd = weekList[(indexOfDayInWeekList + 1 + i) % 7];
//         daysToPlanFor.push(dayToAdd);
//     }
//
//     return (
//         <option>{daysToPlanFor}</option>
//     );
// }

// class SelectionDays extends Component {
//     // move function that outputs daysToPlanFor here or earlier, then map
//     // over that array and create new row for each day with day as first column
//     // then select boxes for other columns
//     render () {
//         const { createOptions } = this.props;
//         const rows = createOptions.map((row, index) => {
//             // change the select elements to be their own components
//             return (
//                 <tr key={index}>
//                     <td>{row.startDay}</td>
//                     <td>
//                         <RecipeOption createOptions={createOptions} />
//                     </td>
//                     <td>
//                         <RecipeOption createOptions={createOptions} />
//                     </td>
//                     <td>
//                         <RecipeOption createOptions={createOptions} />
//                     </td>
//                 </tr>
//             );
//         });
//
//         return (
//             <tbody>{rows}</tbody>
//         );
//     }
// }

class Selection extends Component {
    render () {
        const { createOptions } = this.props;

        return (
            <table>
                <SelectionHeader />
            </table>
        );
    }
}

export default Selection;
