import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { Carousel, Image } from "react-bootstrap";
import Loader from "./Loader";
import Message from "./Message";
import { listTopMovies } from "../actions/movieActions";

const MovieCarousel = () => {
  const dispatch = useDispatch();

  const movieTopRated = useSelector((state) => state.movieTopRated);
  const { error, loading, movies } = movieTopRated;

  useEffect(() => {
    dispatch(listTopMovies());
  }, [dispatch]);
  return loading ? (
    <Loader />
  ) : error ? (
    <Message variant="danger">{error}</Message>
  ) : (
    <Carousel pause="hover" className="bg-dark">
      {movies.map((movie) => (
        <Carousel.Item key={movie._id}>
          <Link to={`/movies/${movie._id}`}>
            <Image src={movie.image} alt={movie.name} fluid />
            <Carousel.Caption className="carousel.caption">
              <h4>{movie.name}</h4>
            </Carousel.Caption>
          </Link>
        </Carousel.Item>
      ))}
    </Carousel>
  );
};

export default MovieCarousel;
import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { Carousel, Image } from "react-bootstrap";
import Loader from "./Loader";
import Message from "./Message";
import { listTopMovies } from "../actions/movieActions";

const MovieCarousel = () => {
  const dispatch = useDispatch();

  const movieTopRated = useSelector((state) => state.movieTopRated);
  const { error, loading, movies } = movieTopRated;

  useEffect(() => {
    dispatch(listTopMovies());
  }, [dispatch]);
  return loading ? (
    <Loader />
  ) : error ? (
    <Message variant="danger">{error}</Message>
  ) : (
    <Carousel pause="hover" className="bg-dark">
      {movies.map((movie) => (
        <Carousel.Item key={movie._id}>
          <Link to={`/movies/${movie._id}`}>
            <Image src={movie.image} alt={movie.name} fluid />
            <Carousel.Caption className="carousel.caption">
              <h4>{movie.name}</h4>
            </Carousel.Caption>
          </Link>
        </Carousel.Item>
      ))}
    </Carousel>
  );
};

export default MovieCarousel;
