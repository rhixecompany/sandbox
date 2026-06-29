import React, { Component } from "react";
import { Container } from "react-bootstrap";
import { HashRouter as Router, Route } from "react-router-dom";

import Header from "./components/Header";
import Footer from "./components/Footer";
import HomeScreen from "./screens/HomeScreen";
import LoginScreen from "./screens/LoginScreen";
import RegisterScreen from "./screens/RegisterScreen";
import MovieScreen from "./screens/MovieScreen";
import MoviesScreen from "./screens/MoviesScreen";
import ProfileScreen from "./screens/ProfileScreen";
import UserListScreen from "./screens/UserListScreen";
import UserEditScreen from "./screens/UserEditScreen";
import SeriesScreen from "./screens/SeriesScreen";
import SerieScreen from "./screens/SerieScreen";
import MoviesListScreen from "./screens/MoviesListScreen";
import MoviesEditScreen from "./screens/MoviesEditScreen";
import SeriesListScreen from "./screens/SeriesListScreen";

export class App extends Component {
  render() {
    return (
      <Router>
        <Header />
        <main className="py-3">
          <Container>
            <Route path="/" component={HomeScreen} exact />
            <Route path="/login" component={LoginScreen} />
            <Route path="/register" component={RegisterScreen} />
            <Route path="/movies" component={MoviesScreen} />
            <Route path="/movie/:id" component={MovieScreen} />
            <Route path="/profile" component={ProfileScreen} />
            <Route path="/admin/users" component={UserListScreen} />
            <Route path="/admin/user/:id/edit" component={UserEditScreen} />
            <Route path="/admin/movies" component={MoviesListScreen} />
            <Route path="/admin/movie/:id/edit" component={MoviesEditScreen} />
            <Route path="/admin/series" component={SeriesListScreen} />
            <Route path="/series" component={SeriesScreen} />
            <Route path="/serie/:id" component={SerieScreen} />
          </Container>
        </main>
        <Footer />
      </Router>
    );
  }
}

export default App;
