<<<<<<< HEAD
import {
  SERIES_LIST_REQUEST,
  SERIES_LIST_SUCCESS,
  SERIES_LIST_FAIL,
  SERIES_DETAILS_REQUEST,
  SERIES_DETAILS_SUCCESS,
  SERIES_DETAILS_FAIL,
  SERIES_DELETE_REQUEST,
  SERIES_DELETE_SUCCESS,
  SERIES_DELETE_FAIL,
  SERIES_CREATE_REQUEST,
  SERIES_CREATE_SUCCESS,
  SERIES_CREATE_FAIL,
  SERIES_CREATE_RESET,
  SERIES_UPDATE_REQUEST,
  SERIES_UPDATE_SUCCESS,
  SERIES_UPDATE_FAIL,
  SERIES_UPDATE_RESET,
  SERIES_CREATE_REVIEW_REQUEST,
  SERIES_CREATE_REVIEW_SUCCESS,
  SERIES_CREATE_REVIEW_FAIL,
  SERIES_CREATE_REVIEW_RESET,
  SERIES_TOP_REQUEST,
  SERIES_TOP_SUCCESS,
  SERIES_TOP_FAIL,
} from "../constants/seriesConstants";

export const seriesListReducer = (state = { series: [] }, action) => {
  switch (action.type) {
    case SERIES_LIST_REQUEST:
      return { loading: true, series: [] };

    case SERIES_LIST_SUCCESS:
      return {
        loading: false,
        series: action.payload.series,
        page: action.payload.page,
        pages: action.payload.pages,
      };

    case SERIES_LIST_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const seriesDetailsReducer = (
  state = { serie: { reviews: [] } },
  action
) => {
  switch (action.type) {
    case SERIES_DETAILS_REQUEST:
      return { loading: true, ...state };

    case SERIES_DETAILS_SUCCESS:
      return { loading: false, serie: action.payload };

    case SERIES_DETAILS_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const seriesDeleteReducer = (state = {}, action) => {
  switch (action.type) {
    case SERIES_DELETE_REQUEST:
      return { loading: true };

    case SERIES_DELETE_SUCCESS:
      return { loading: false, success: true };

    case SERIES_DELETE_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const seriesCreateReducer = (state = {}, action) => {
  switch (action.type) {
    case SERIES_CREATE_REQUEST:
      return { loading: true };

    case SERIES_CREATE_SUCCESS:
      return { loading: false, success: true, serie: action.payload };

    case SERIES_CREATE_FAIL:
      return { loading: false, error: action.payload };

    case SERIES_CREATE_RESET:
      return {};

    default:
      return state;
  }
};

export const seriesUpdateReducer = (state = { serie: {} }, action) => {
  switch (action.type) {
    case SERIES_UPDATE_REQUEST:
      return { loading: true };

    case SERIES_UPDATE_SUCCESS:
      return { loading: false, success: true, serie: action.payload };

    case SERIES_UPDATE_FAIL:
      return { loading: false, error: action.payload };

    case SERIES_UPDATE_RESET:
      return { serie: {} };

    default:
      return state;
  }
};

export const seriesReviewCreateReducer = (state = {}, action) => {
  switch (action.type) {
    case SERIES_CREATE_REVIEW_REQUEST:
      return { loading: true };

    case SERIES_CREATE_REVIEW_SUCCESS:
      return { loading: false, success: true };

    case SERIES_CREATE_REVIEW_FAIL:
      return { loading: false, error: action.payload };

    case SERIES_CREATE_REVIEW_RESET:
      return {};

    default:
      return state;
  }
};

export const seriesTopRatedReducer = (state = { series: [] }, action) => {
  switch (action.type) {
    case SERIES_TOP_REQUEST:
      return { loading: true, series: [] };

    case SERIES_TOP_SUCCESS:
      return { loading: false, series: action.payload };

    case SERIES_TOP_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};
=======
import {
  SERIES_LIST_REQUEST,
  SERIES_LIST_SUCCESS,
  SERIES_LIST_FAIL,
  SERIES_DETAILS_REQUEST,
  SERIES_DETAILS_SUCCESS,
  SERIES_DETAILS_FAIL,
  SERIES_DELETE_REQUEST,
  SERIES_DELETE_SUCCESS,
  SERIES_DELETE_FAIL,
  SERIES_CREATE_REQUEST,
  SERIES_CREATE_SUCCESS,
  SERIES_CREATE_FAIL,
  SERIES_CREATE_RESET,
  SERIES_UPDATE_REQUEST,
  SERIES_UPDATE_SUCCESS,
  SERIES_UPDATE_FAIL,
  SERIES_UPDATE_RESET,
  SERIES_CREATE_REVIEW_REQUEST,
  SERIES_CREATE_REVIEW_SUCCESS,
  SERIES_CREATE_REVIEW_FAIL,
  SERIES_CREATE_REVIEW_RESET,
  SERIES_TOP_REQUEST,
  SERIES_TOP_SUCCESS,
  SERIES_TOP_FAIL,
} from "../constants/seriesConstants";

export const seriesListReducer = (state = { series: [] }, action) => {
  switch (action.type) {
    case SERIES_LIST_REQUEST:
      return { loading: true, series: [] };

    case SERIES_LIST_SUCCESS:
      return {
        loading: false,
        series: action.payload.series,
        page: action.payload.page,
        pages: action.payload.pages,
      };

    case SERIES_LIST_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const seriesDetailsReducer = (
  state = { serie: { reviews: [] } },
  action
) => {
  switch (action.type) {
    case SERIES_DETAILS_REQUEST:
      return { loading: true, ...state };

    case SERIES_DETAILS_SUCCESS:
      return { loading: false, serie: action.payload };

    case SERIES_DETAILS_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const seriesDeleteReducer = (state = {}, action) => {
  switch (action.type) {
    case SERIES_DELETE_REQUEST:
      return { loading: true };

    case SERIES_DELETE_SUCCESS:
      return { loading: false, success: true };

    case SERIES_DELETE_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const seriesCreateReducer = (state = {}, action) => {
  switch (action.type) {
    case SERIES_CREATE_REQUEST:
      return { loading: true };

    case SERIES_CREATE_SUCCESS:
      return { loading: false, success: true, serie: action.payload };

    case SERIES_CREATE_FAIL:
      return { loading: false, error: action.payload };

    case SERIES_CREATE_RESET:
      return {};

    default:
      return state;
  }
};

export const seriesUpdateReducer = (state = { serie: {} }, action) => {
  switch (action.type) {
    case SERIES_UPDATE_REQUEST:
      return { loading: true };

    case SERIES_UPDATE_SUCCESS:
      return { loading: false, success: true, serie: action.payload };

    case SERIES_UPDATE_FAIL:
      return { loading: false, error: action.payload };

    case SERIES_UPDATE_RESET:
      return { serie: {} };

    default:
      return state;
  }
};

export const seriesReviewCreateReducer = (state = {}, action) => {
  switch (action.type) {
    case SERIES_CREATE_REVIEW_REQUEST:
      return { loading: true };

    case SERIES_CREATE_REVIEW_SUCCESS:
      return { loading: false, success: true };

    case SERIES_CREATE_REVIEW_FAIL:
      return { loading: false, error: action.payload };

    case SERIES_CREATE_REVIEW_RESET:
      return {};

    default:
      return state;
  }
};

export const seriesTopRatedReducer = (state = { series: [] }, action) => {
  switch (action.type) {
    case SERIES_TOP_REQUEST:
      return { loading: true, series: [] };

    case SERIES_TOP_SUCCESS:
      return { loading: false, series: action.payload };

    case SERIES_TOP_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
