import React, { Component } from 'react';

class Create extends Component {
    constructor(props) {
        super(props);

        this.initialState = {
            startDay: '',
            numberDays: '',
        };

        this.state = this.initialState;
    }

    handleChange = event => {
        const { name, value } = event.target;

        this.setState({
            [name] : value
        });
    }

    submitForm = () => {
        this.props.handleSubmit(this.state);
        this.setState(this.initialState);
    }

    render() {
        const { startDay, numberDays } = this.state;

        return (
            <form>
                <label>Day to Start On</label>
                <input
                    type="text"
                    name="startDay"
                    value={startDay}
                    onChange={this.handleChange} />
                <label>Number of Days to Plan For</label>
                <input
                    type="int"
                    name="numberDays"
                    value="numberDays"
                    onChange="{this.handleChange}" />
                <input
                    type="button"
                    value="Submit"
                    onClick={this.submitForm} />
            </form>
        );
    }
}

export default Create;
