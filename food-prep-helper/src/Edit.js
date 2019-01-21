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

    handleChange = event => {
        const {value} = event.target;

        this.setState({
            recipeToEdit : value,
        });
    }

    // fetch recipeInfo from API and then pass as props to EditRecipe
    handleEditRecipe = () => {
        const url = "http://localhost:5000/edit";

        fetch(url)
            .then(result => result.json())
            .then(result => {
                this.setState({
                    recipeInfo: result
                })
            });

        <Route path="/edit/<int:id>" component={(props) => <EditRecipe recipeToEdit={this.state.recipeToEdit} {...props} />} />
    }

    render() {
        const { recipes } = this.props;

        // lets user select the recipe name they want to change,
        // set value to be recipe["recipe_key"] in order to send
        // the key to API
        return (
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
        );
    }
}

export default Edit;