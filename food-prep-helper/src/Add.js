import React, { Component } from 'react';

class Add extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            // recipeToAddInfo: []
            recipeName: "",
            mealServed: "",
            servingSize: "",
            ingredientInfo: "",
        };

        this.state = this.initialState;
    }

    handleChange = event => {
        const { name, value } = event.target;
        // const updatedState = this.state;
        // updatedState[name] = value;

        this.setState({
            [name] : value
        });
    }

    // create recipe class to store recipeInfo in, then stringify whole recipe and
    // pass to API?
    handleAddRecipe = () => {
        const recipeName = this.state.recipeName;
        const mealServed = this.state.mealServed;
        const servingSize = this.state.servingSize;
        const ingredientInfo = this.state.ingredientInfo;
        const addRecipeUrl = "http://localhost:5000/add";

        fetch(addRecipeUrl, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
                // recipeName
                {recipeName, mealServed, servingSize, ingredientInfo}
            )
        })
            .then(result => result.json())
            // add resulting ingredient info to recipeToEditInfo
            .then((result) => {
                console.log(result)
                });   
        this.props.history.push({
            pathname: '/'
        }); 
    }

    render() {
        return (
            <form>
                <label>Recipe Name</label>
                <input
                    type="text"
                    name="recipeName"
                    value={this.recipeName}
                    onChange={this.handleChange} />
                <label>Meal Served</label>
                <input
                    type="text"
                    name="mealServed"
                    value={this.mealServed}
                    onChange={this.handleChange} />
                <label>Meals Served for Two People</label>
                <input
                    type="number"
                    name="servingSize"
                    value={this.servingSize}
                    onChange={this.handleChange} />
                <label>Ingredient List (paste ingredient list here)</label>
                <textarea name="ingredientInfo" value={this.ingredientInfo} onChange={this.handleChange} />
                <input type="submit" value="Add Recipe!" onClick={this.handleAddRecipe} />
            </form>
        );
    }
}

export default Add;