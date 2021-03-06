import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom"
import Header from './Components/Header'
import Footer from './Components/Footer'
import Home from './Views/Home'
import User from './Views/User'
import Door from './Views/Door'

function App() {
  return (
    <div className="relative pb-10 min-h-screen">
      <Router>
        
        <Header />

        <div className="p-3">
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route path="/users">
            <User />
          </Route>
          <Route path="/doors/:id">
            <Door />
          </Route>
        </Switch>
        </div>

        <Footer />

      </Router>
    </div>
  );
}

export default App;
