import React, { Component } from 'react';

class AddRecipe extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            recipeName: "",
            mealServed: "",
            servingSize: "",
            ingredientInfo: "",
        };

        this.setState = this.initialState;
    }

    handleChange = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
    }

    handleSubmitRecipe = () => {
        // POST recipe info to API
    }

    render() {
        return (
            <form>
                <label>Recipe Name</label>
                <input
                    type="text"
                    name="recipeName"
                    value={recipeName}
                    onChange={this.handleChange} />
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
                <textarea name="ingredientInfo" style="width:200px; height:600px">
                    {ingredientInfo}
                </textarea>
                <input type="submit" value="Add" href="{{ url_for('create.index') }}" />
            </form>
        );
    }
}

export default AddRecipe;