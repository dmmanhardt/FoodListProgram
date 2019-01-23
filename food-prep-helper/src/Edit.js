import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
import EditRecipe from './EditRecipe';


// this component lets the user choose which recipe to enter from recipes
// pulled from API and stored as state at App component
class Edit extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            recipeToEdit: ""
        };

        this.state = this.initialState;
    }

    // change this to pass all info to Options.js in order to pass
    // to EditRecipe component. Maybe create class object for the recipe
    // with all the info and pass that?
    handleChange = event => {
        const {value} = event.target;

        this.setState({
            recipeToEdit : value,
        });
    }

    // fetch recipeInfo from API and then pass as props to EditRecipe
    handleEditRecipe = () => {
        const recipeToEdit = this.state.recipeToEdit;
        const editUrl = "http://localhost:5000/edit";

        fetch(editUrl, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
                recipeToEdit,
            )
        })
            .then(result => result.json())
            .then(result => this.props.handleIngredientInfo(result))
            .then(result => {
                this.props.history.push({
                    pathname: '/EditRecipe',
                    search: '?query=abc',
                })
            })
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
                        { recipes.map(recipe => {
                            return <option name="recipeToEdit" value={recipe["recipeID"]}>
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