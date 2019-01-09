import React, { Component } from 'react';

// use recipesPicked passed from Selection component to create GroceryList
// might have to pass recipesPicked to Python then return groceryList from
// python?
class GroceryList extends Component {
    render() {
        const { recipesPicked } = this.props;
        const ingredients = recipesPicked.map((recipe) => {
            return (
                <li>{recipe}</li>
            );
        });
    
        return (
            <form>
                <h6>Grocery List</h6>
                <ul>{ingredients}</ul>
            </form>
        );
        // loop through selectionCellIndexes here and populate recipesPicked here?
        // or do it before in app component and pass recipesPicked through as props?

        // pass recipesPicked to python file

        // once python file passes back ingredient info
        // loop over ingredient info and create list item component
        // for each in format "Ingredient: amount measurement"

    }
}

export default GroceryList;
