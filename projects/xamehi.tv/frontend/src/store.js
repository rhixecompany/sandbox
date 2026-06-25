import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

import {
  userLoginReducer,
  userRegisterReducer,
  userDetailsReducer,
  userUpdateProfileReducer,
  userListReducer,
  userDeleteReducer,
  userUpdateReducer,
} from "./reducers/userReducers";

import {
  movieListReducer,
  movieDetailsReducer,
  movieDeleteReducer,
  movieCreateReducer,
  movieUpdateReducer,
  movieReviewCreateReducer,
  movieTopRatedReducer,
} from "./reducers/movieReducers";

import {
  seriesListReducer,
  seriesDetailsReducer,
  seriesDeleteReducer,
  seriesCreateReducer,
  seriesUpdateReducer,
  seriesReviewCreateReducer,
  seriesTopRatedReducer,
} from "./reducers/seriesReducers";

const reducer = combineReducers({
  movieList: movieListReducer,
  movieDetails: movieDetailsReducer,
  movieDelete: movieDeleteReducer,
  movieCreate: movieCreateReducer,
  movieUpdate: movieUpdateReducer,
  movieReviewCreate: movieReviewCreateReducer,
  movieTopRated: movieTopRatedReducer,

  seriesList: seriesListReducer,
  seriesDetails: seriesDetailsReducer,
  seriesDelete: seriesDeleteReducer,
  seriesCreate: seriesCreateReducer,
  seriesUpdate: seriesUpdateReducer,
  seriesReviewCreate: seriesReviewCreateReducer,
  seriesTopRated: seriesTopRatedReducer,

  userLogin: userLoginReducer,
  userRegister: userRegisterReducer,
  userDetails: userDetailsReducer,
  userUpdateProfile: userUpdateProfileReducer,
  userList: userListReducer,
  userDelete: userDeleteReducer,
  userUpdate: userUpdateReducer,
});

const userInfoFromStorage = localStorage.getItem("userInfo")
  ? JSON.parse(localStorage.getItem("userInfo"))
  : null;

const initialState = {
  userLogin: { userInfo: userInfoFromStorage },
};

const middleware = [thunk];

const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

import {
  userLoginReducer,
  userRegisterReducer,
  userDetailsReducer,
  userUpdateProfileReducer,
  userListReducer,
  userDeleteReducer,
  userUpdateReducer,
} from "./reducers/userReducers";

import {
  movieListReducer,
  movieDetailsReducer,
  movieDeleteReducer,
  movieCreateReducer,
  movieUpdateReducer,
  movieReviewCreateReducer,
  movieTopRatedReducer,
} from "./reducers/movieReducers";

import {
  seriesListReducer,
  seriesDetailsReducer,
  seriesDeleteReducer,
  seriesCreateReducer,
  seriesUpdateReducer,
  seriesReviewCreateReducer,
  seriesTopRatedReducer,
} from "./reducers/seriesReducers";

const reducer = combineReducers({
  movieList: movieListReducer,
  movieDetails: movieDetailsReducer,
  movieDelete: movieDeleteReducer,
  movieCreate: movieCreateReducer,
  movieUpdate: movieUpdateReducer,
  movieReviewCreate: movieReviewCreateReducer,
  movieTopRated: movieTopRatedReducer,

  seriesList: seriesListReducer,
  seriesDetails: seriesDetailsReducer,
  seriesDelete: seriesDeleteReducer,
  seriesCreate: seriesCreateReducer,
  seriesUpdate: seriesUpdateReducer,
  seriesReviewCreate: seriesReviewCreateReducer,
  seriesTopRated: seriesTopRatedReducer,

  userLogin: userLoginReducer,
  userRegister: userRegisterReducer,
  userDetails: userDetailsReducer,
  userUpdateProfile: userUpdateProfileReducer,
  userList: userListReducer,
  userDelete: userDeleteReducer,
  userUpdate: userUpdateReducer,
});

const userInfoFromStorage = localStorage.getItem("userInfo")
  ? JSON.parse(localStorage.getItem("userInfo"))
  : null;

const initialState = {
  userLogin: { userInfo: userInfoFromStorage },
};

const middleware = [thunk];

const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
