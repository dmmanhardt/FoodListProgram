import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import EditRecipe from './EditRecipe';


// this component lets the user choose which recipe to enter from recipes
// pulled from API and stored as state at App component
class Edit extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            recipeToEdit: null
        };

        this.state = this.initialState;
    }

    // return all recipe info based on index from recipes
    handleChange = event => {
        const {value} = event.target;

        this.setState({
            recipeToEdit : this.props.recipes[value]
        });
    }

    // fetch ingredientInfo from API using recipeID, pass
    // up to AppRouter, and then navigate to EditRecipe
    // move this to EditRecipe instead?
    handleEditRecipe = () => {
        const recipeToEditInfo = this.state.recipeToEdit;
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
            .then(function(result) {
                recipeToEditInfo.ingredientInfo = result;
                return recipeToEditInfo})
            .then(recipeToEditInfo => this.props.handleIngredientInfo(recipeToEditInfo))
            .then(
                this.props.history.push({
                    pathname: '/EditRecipe',
                    search: '?query=abc',
                    state: { recipeToEditInfo: recipeToEditInfo }
                })
            )
        };

    render() {
        const { recipes } = this.props;

        // lets user select the recipe name they want to change,
        // set value to be recipe["recipe_key"] in order to send
        // the key to API
        return (
            <div>
                <form>
                    <label>Select the Recipe to Edit</label>
                    <select name="recipeToEdit" id="recipeToEdit" onChange={this.handleChange}>
                        <option value="none"></option>
                        { recipes.map((recipe, index) => {
                            return <option name="recipeToEdit" value={index}>
                                        {recipe["recipeName"]}                                    
                                    </option>
                        })}
                    </select>
                    <input
                        type="button"
                        value="Edit"
                        onClick={this.handleEditRecipe} />
                </form>

                {this.props.children}
            </div>
        );
    }
}

export default Edit;