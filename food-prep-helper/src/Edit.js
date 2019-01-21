import React, { Component } from 'react';


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
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
    }

    handleEditRecipe = () => {
        // POST new recipe info to API
    }

    render() {
        const { recipes } = this.props;

        return (
            <form>
                <select name="recipeToEdit" id="recipeToEdit" style="width: 150px">
                    <option value="none"></option>
                    { recipes.map(recipe => {
                        return <option name="recipeToEdit" value={recipe["recipe_name"]}>
                                    {recipe["recipe_name"]}                                    
                                </option>
                    })}
                </select>
            </form>
        );
    }
}

export default Edit;