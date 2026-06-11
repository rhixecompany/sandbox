import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Row, Col, Button } from "react-bootstrap";
import { Link } from "react-router-dom";

import Loader from "../components/Loader";
import Message from "../components/Message";
import Paginate from "../components/Paginate";
import SearchBox from "../components/SearchBox";
import Movie from "../components/Movie";
import MovieCarousel from "../components/MovieCarousel";
import { listMovies } from "../actions/movieActions";

const MoviesScreen = ({ history }) => {
  const dispatch = useDispatch();
  const movieList = useSelector((state) => state.movieList);
  const { error, loading, movies, page, pages } = movieList;

  let keyword = history.location.search;

  useEffect(() => {
    dispatch(listMovies(keyword));
  }, [dispatch, keyword]);

  return (
    <div>
      <div>
        <SearchBox />
      </div>
      {!keyword && <MovieCarousel />}
      <Link to="/series">
        <Button>Views Series</Button>
      </Link>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <div>
            <Row>
              {movies.map((movie) => (
                <Col key={movie._id} sm={12} md={6} lg={4} xl={3}>
                  <Movie movie={movie} />
                </Col>
              ))}
            </Row>
            <Paginate page={page} pages={pages} keyword={keyword} />
          </div>
        </div>
      )}
    </div>
  );
};

export default MoviesScreen;
