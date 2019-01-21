import React, { Component } from 'react';
import { BrowswerRouter as Router, Route, Link } from 'react-router-dom';

class EditRecipe extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            recipeName: "",
            mealServed: "",
            servingSize: "",
            ingredientInfo: "",
        };

        this.state = this.initialState;
    }

    // on component mount, fetch current recipe info
    componentDidMount() {
        const url = "http://localhost:5000/edit";

        fetch(url)
            .then(result => result.json())
            .then(result => {
                this.setState({
                    recipes: result
                })
            });
    }

    handleChange = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
    }

    handleSubmitEdits = () => {
        // send edits to API to update db
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
                <textarea name="ingredientInfo">
                    {this.ingredientInfo}
                </textarea>
                <input type="submit" value="Add" href="{{ url_for('create.index') }}" />
            </form>
        )
    }
}

export default EditRecipe;