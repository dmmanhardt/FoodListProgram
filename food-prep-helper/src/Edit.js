import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import EditRecipe from './EditRecipe';


// this component lets the user choose which recipe to enter from recipes
// pulled from API and stored as state at App component
class Edit extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            recipeToEditInfo: null
        };

        this.state = this.initialState;
    }

    // return all recipe info based on index from recipes
    handleChange = event => {
        const {value} = event.target;

        this.setState({
            recipeToEditInfo : this.props.recipes[value]
        });
    }

    // pass recipeToEditID to EditRecipe, which will then 
    // fetch ingredient info for recipe from API
    handleEditRecipe = () => {
        const recipeToEditInfo = this.state.recipeToEditInfo;
        // const recipeToEditID = recipeToEditInfo.recipeID;
        // const editUrl = "http://localhost:5000/edit";

        // fetch(editUrl, {
        //     method: 'POST',
        //     headers: {
        //         'Accept': 'application/json',
        //         'Content-Type': 'application/json',
        //     },
        //     body: JSON.stringify(
        //         recipeToEditID,
        //     )
        // })
        //     .then(result => result.json())
        //     // add resulting ingredient info to recipeToEditInfo
        //     .then(function(result) {
        //         recipeToEditInfo.ingredientInfo = result;
        //         return recipeToEditInfo})
        //     .then(recipeToEditInfo => this.props.handleIngredientInfo(recipeToEditInfo))
        //     .then(
        this.props.history.push({
            pathname: '/EditRecipe',
            search: '?query=abc',
            state: { recipeToEditInfo: recipeToEditInfo }
        })};

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