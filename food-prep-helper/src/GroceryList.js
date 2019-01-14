import React, { Component } from 'react';

// use recipesPicked passed from Selection component to create GroceryList
// might have to pass recipesPicked to Python then return groceryList from
// python?
class GroceryList extends Component {
    render() {
        const { recipesPicked } = this.props;
        // POST recipesPicked to create.py '/grocerylist' and fetch
        // return groceryList which is returned as list
        fetch('http://localhost:5000/grocerylist', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                firstParam: recipesPicked,
            })
        })
        const ingredients = recipesPicked.map((recipe) => {
            return (
                <li>{recipe}</li>
            );
        });
    
        return (
            <form>
                <h4>Grocery List:</h4>
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
