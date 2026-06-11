import axios from "axios";
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
  SERIES_UPDATE_REQUEST,
  SERIES_UPDATE_SUCCESS,
  SERIES_UPDATE_FAIL,
  SERIES_CREATE_REVIEW_REQUEST,
  SERIES_CREATE_REVIEW_SUCCESS,
  SERIES_CREATE_REVIEW_FAIL,
  SERIES_TOP_REQUEST,
  SERIES_TOP_SUCCESS,
  SERIES_TOP_FAIL,
} from "../constants/seriesConstants";

export const listSeries =
  (keyword = "") =>
  async (dispatch) => {
    try {
      dispatch({ type: SERIES_LIST_REQUEST });

      const { data } = await axios.get(`/api/series${keyword}`);

      dispatch({
        type: SERIES_LIST_SUCCESS,
        payload: data,
      });
    } catch (error) {
      keyword = "";
      dispatch({
        type: SERIES_LIST_FAIL,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };

export const listTopSeries = () => async (dispatch) => {
  try {
    dispatch({ type: SERIES_TOP_REQUEST });

    const { data } = await axios.get(`/api/series/top/`);

    dispatch({
      type: SERIES_TOP_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: SERIES_TOP_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const listSeriesDetails = (id) => async (dispatch) => {
  try {
    dispatch({ type: SERIES_DETAILS_REQUEST });

    const { data } = await axios.get(`/api/series/${id}`);

    dispatch({
      type: SERIES_DETAILS_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: SERIES_DETAILS_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const deleteSeries = (id) => async (dispatch, getState) => {
  try {
    dispatch({
      type: SERIES_DELETE_REQUEST,
    });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${userInfo.token}`,
      },
    };

    // eslint-disable-next-line no-unused-vars
    const { data } = await axios.delete(`/api/series/delete/${id}/`, config);

    dispatch({
      type: SERIES_DELETE_SUCCESS,
    });
  } catch (error) {
    dispatch({
      type: SERIES_DELETE_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const createSeries = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: SERIES_CREATE_REQUEST,
    });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${userInfo.token}`,
      },
    };

    const { data } = await axios.post(`/api/series/create/`, {}, config);
    dispatch({
      type: SERIES_CREATE_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: SERIES_CREATE_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const updateSeries = (series) => async (dispatch, getState) => {
  try {
    dispatch({
      type: SERIES_UPDATE_REQUEST,
    });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${userInfo.token}`,
      },
    };

    const { data } = await axios.put(
      `/api/series/update/${series._id}/`,
      series,
      config
    );
    dispatch({
      type: SERIES_UPDATE_SUCCESS,
      payload: data,
    });

    dispatch({
      type: SERIES_DETAILS_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: SERIES_UPDATE_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const createSeriesReview =
  (seriesId, review) => async (dispatch, getState) => {
    try {
      dispatch({
        type: SERIES_CREATE_REVIEW_REQUEST,
      });

      const {
        userLogin: { userInfo },
      } = getState();

      const config = {
        headers: {
          "Content-type": "application/json",
          Authorization: `Bearer ${userInfo.token}`,
        },
      };

      const { data } = await axios.post(
        `/api/series/${seriesId}/reviews/`,
        review,
        config
      );
      dispatch({
        type: SERIES_CREATE_REVIEW_SUCCESS,
        payload: data,
      });
    } catch (error) {
      dispatch({
        type: SERIES_CREATE_REVIEW_FAIL,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
