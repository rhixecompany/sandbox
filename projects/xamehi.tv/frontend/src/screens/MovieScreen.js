import React, { useEffect } from "react";
import { Row, Col, Image } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { listMovieDetails } from "../actions/movieActions";

const MovieScreen = ({ match }) => {
  const dispatch = useDispatch();
  const movieDetails = useSelector((state) => state.movieDetails);
  const { error, loading, movie } = movieDetails;
  let id = match.params.id;

  useEffect(() => {
    dispatch(listMovieDetails(id));
  }, [dispatch, id]);

  return (
    <div>
      <h3>Single Movie Page</h3>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Row>
            <Col>
              <div>
                <Image src={movie.image} alt={movie.name} fluid />
              </div>
              <div>
                {" "}
                <h4>{movie.name}</h4>
                <p>{movie.description}</p>
                <i>{movie.createdAt}</i>
                <span>
                  <strong>{movie.rating}</strong>
                </span>
                <p>{movie.actor}</p>
                <span>
                  <strong>{movie.likes}</strong>
                </span>
              </div>
              <div>
                <video src={movie.file} controls width="485" height="360" />
              </div>
            </Col>
          </Row>
        </div>
      )}
    </div>
  );
};

export default MovieScreen;
import React, { useEffect } from "react";
import { Row, Col, Image } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { listMovieDetails } from "../actions/movieActions";

const MovieScreen = ({ match }) => {
  const dispatch = useDispatch();
  const movieDetails = useSelector((state) => state.movieDetails);
  const { error, loading, movie } = movieDetails;
  let id = match.params.id;

  useEffect(() => {
    dispatch(listMovieDetails(id));
  }, [dispatch, id]);

  return (
    <div>
      <h3>Single Movie Page</h3>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Row>
            <Col>
              <div>
                <Image src={movie.image} alt={movie.name} fluid />
              </div>
              <div>
                {" "}
                <h4>{movie.name}</h4>
                <p>{movie.description}</p>
                <i>{movie.createdAt}</i>
                <span>
                  <strong>{movie.rating}</strong>
                </span>
                <p>{movie.actor}</p>
                <span>
                  <strong>{movie.likes}</strong>
                </span>
              </div>
              <div>
                <video src={movie.file} controls width="485" height="360" />
              </div>
            </Col>
          </Row>
        </div>
      )}
    </div>
  );
};

export default MovieScreen;
