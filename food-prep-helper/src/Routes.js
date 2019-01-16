import React from 'react';
import { Route, IndexRoute } from 'react-router-dom';

import App from './components/App';
import MainPage from './components/MainPage';
import Add from './components/Add';

export default (
    <Route path="/" component={App}>
        <IndexRoute component={MainPage} />
        <Route path="/add" component={Add} />
    </Route>
);