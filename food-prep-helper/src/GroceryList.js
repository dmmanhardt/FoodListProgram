import React, { Component } from 'react';

class GroceryList extends Component {
    state = {
        groceryList: []
    };

    // POST recipesPicked to create.py '/grocerylist' and fetch
    // return groceryList which is returned as list
    fetchGroceryList() {
        const { recipesPicked } = this.props;
        const groceryListUrl = 'http://localhost:5000/grocerylist'
        fetch(groceryListUrl, {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(
                recipesPicked,
            )
        })
        .then(response => response.json())
        .then(response => {
            this.setState({
                groceryList: response
            })
        });
    }

    componentDidMount() {
        this.fetchGroceryList();
    }

    componentDidUpdate(prevProps) {
        if (prevProps.recipesPicked !== this.props.recipesPicked) {
            this.fetchGroceryList();
        }
    }
    
    render() {
        const ingredients = this.state.groceryList.map((ingredient) => {
            return (
                <li>{ingredient}</li>
            );
        });
    
        return (
            <form>
                <h4>Grocery List:</h4>
                <ul>{ingredients}</ul>
            </form>
        );
    }
}

export default GroceryList;
