import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

class EditRecipe extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            ingredientInfo: []
        };

        this.state = this.initialState;
    }

    componentDidMount() {
        const { recipeToEditInfo } = this.props;
        console.log(this.props.location.state.recipeToEditInfo);

        this.setState({
            recipeName: recipeToEditInfo.recipeName,
            mealServed: recipeToEditInfo.mealServed,
            servingSize: recipeToEditInfo.servingSize,
            recipeID: recipeToEditInfo.recipeID,
            ingredientInfo: recipeToEditInfo.ingredientInfo,
        })
    }

    handleChange = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
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
        // send edits to API to update db
    }

    render() {
        const { ingredientInfo } = this.state;

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
                <label>Ingredient List</label>
                <table>
                    <tr>
                        <th>Amount</th>
                        <th>Ingredient</th>
                        <th>Measurement</th>
                    </tr>
                    { ingredientInfo.map(ingredient => {
                        return <tr>
                                    <td><input name="amount" value={ingredient["amount"]} /></td>
                                    <td><input name="ingredient" value={ingredient["name"]} /></td>
                                    <td><input name="measurement" value={ingredient["measurement"]} /></td>
                                </tr>})}
                </table>
                <input type="button" value="Add Ingredient" onClick={this.handleAddIngredient} />
                <input type="submit" value="Update" href="{{ url_for('create.index') }}" />
            </form>
        )
    }
}

export default EditRecipe;