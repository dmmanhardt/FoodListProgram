import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

class EditRecipe extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            recipeToEditInfo: this.props.location.state.recipeToEditInfo,
        };

        this.state = this.initialState;
    }

    componentDidMount() {
        const recipeToEditInfo = this.state.recipeToEditInfo;
        const recipeToEditID = recipeToEditInfo.recipeID;
        const editUrl = "http://localhost:5000/edit";

        fetch(editUrl, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
                recipeToEditID,
            )
        })
            .then(result => result.json())
            // add resulting ingredient info to recipeToEditInfo
            .then((result) => {
                recipeToEditInfo.ingredientInfo = result;
                this.setState({
                    recipeToEditInfo: recipeToEditInfo
                });    
            })
    }

    handleChange = event => {
        const { name, value } = event.target;
        const editedRecipe = this.state.recipeToEditInfo;
        editedRecipe[name] = value;

        this.setState({
            recipeToEditInfo : editedRecipe
        });
    }

    handleIngredientInfoChange = event => {
        const { id, value } = event.target;
        const updatedState = this.state.recipeToEditInfo;
        const ingredientKey = event.target.getAttribute('ingredientKey');
        const updatedIngredientInfo = updatedState.ingredientInfo[ingredientKey];

        updatedIngredientInfo[id] = value;

        this.setState({
            recipeToEditInfo : updatedState
        });
    }

    // adds new index with empty parameters that adds empty row to let user add a new ingredient
    handleAddIngredient = () => {
        const newIngredientInfo = this.state.ingredientInfo;
        { newIngredientInfo.push({
            amount: "",
            ingredientID: "",
            measurement: "",
            name: "",
            recipeID: ""
        }); }
        this.setState({
            ingredientInfo : newIngredientInfo
        });
    }

    handleSubmitEdits = () => {
        const recipeToEditInfo = this.state.recipeToEditInfo;
        const { recipeID, recipeName } = recipeToEditInfo;
        const editRecipeUrl = "http://localhost:5000/edit_recipe";

        console.log(recipeName);
        console.log(recipeID);

        fetch(editRecipeUrl, {
            method: 'POST',
            headers: {
                'Accept' : 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                recipeName,
                recipeID
            )
        })
            .then(result => result.json())
            .then(result => {
                console.log(result);
            })

        this.props.history.push({
            pathname: '/'
        });
    }

    render() {
        // checks to see if ingredientInfo exists, then creates new row for
        // each ingredient that lists ingredient info
        const ingredientInfoRows = this.state.recipeToEditInfo.ingredientInfo && this.state.recipeToEditInfo.ingredientInfo.map((ingredient, index) => {
            return (
                <tr>
                    <td><input key={index} ingredientKey={index} id="amount" value={ingredient["amount"]} onChange={this.handleIngredientInfoChange} /></td>
                    <td><input key={index} ingredientKey={index} id="name" value={ingredient["name"]} onChange={this.handleIngredientInfoChange} /></td>
                    <td><input key={index} ingredientKey={index} id="measurement" value={ingredient["measurement"]} onChange={this.handleIngredientInfoChange} /></td>
                </tr>)})

        // const recipeName = this.state.recipeToEditInfo.recipeName;
        const mealServed = this.state.recipeToEditInfo.mealServed;
        const servingSize = this.state.recipeToEditInfo.servingSize;

        return (
            <form>
                <label>Recipe Name</label>
                <input
                    type="text"
                    name="recipeName"
                    value={this.state.recipeToEditInfo.recipeName}
                    onChange={this.handleChange} />
                {/* change this to be a select element with 
                Breakfast, Lunch, Dinner as options */}
                <label>Meal Served</label>
                <input
                    type="text"
                    name="mealServed"
                    value={mealServed}
                    onChange={this.handleChange} />
                <label>Meals Served for Two People</label>
                <input
                    type="number"
                    name="servingSize"
                    value={servingSize}
                    onChange={this.handleChange} />
                <label>Ingredient List</label>
                <table>
                    <tr>
                        <th>Amount</th>
                        <th>Ingredient</th>
                        <th>Measurement</th>
                    </tr>
                    { ingredientInfoRows } 
                </table>
                <input type="button" value="Add Ingredient" onClick={this.handleAddIngredient} />
                <input type="submit" value="Update Recipe!" onClick={this.handleSubmitEdits} />
            </form>
        )
    }
}

export default EditRecipe;