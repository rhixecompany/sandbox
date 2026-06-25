import React, { useEffect } from "react";
import { LinkContainer } from "react-router-bootstrap";
import { Table, Button, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import MovieForm from "../components/MovieForm";
import Paginate from "../components/Paginate";
import { listMovies, deleteMovie } from "../actions/movieActions";
import { MOVIE_CREATE_RESET } from "../constants/movieConstants";

function MoviesListScreen({ history, match }) {
  const dispatch = useDispatch();

  const movieList = useSelector((state) => state.movieList);
  const { loading, error, movies, pages, page } = movieList;

  const movieDelete = useSelector((state) => state.movieDelete);
  const {
    loading: loadingDelete,
    error: errorDelete,
    success: successDelete,
  } = movieDelete;

  const movieCreate = useSelector((state) => state.movieCreate);
  const {
    loading: loadingCreate,
    error: errorCreate,
    success: successCreate,
    movie: createdMovie,
  } = movieCreate;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  let keyword = history.location.search;
  useEffect(() => {
    dispatch({ type: MOVIE_CREATE_RESET });

    if (!userInfo.isAdmin) {
      history.push("/login");
    }

    if (successCreate) {
      history.push(`/admin/movies/${createdMovie._id}/edit`);
    } else {
      dispatch(listMovies(keyword));
    }
  }, [
    dispatch,
    history,
    userInfo,
    successDelete,
    successCreate,
    createdMovie,
    keyword,
  ]);

  const deleteHandler = (id) => {
    if (window.confirm("Are you sure you want to delete this movie?")) {
      dispatch(deleteMovie(id));
    }
  };

  return (
    <div>
      <Row className="align-items-center">
        <Col>
          <h1>movies</h1>
        </Col>
      </Row>

      <MovieForm />

      {loadingDelete && <Loader />}
      {errorDelete && <Message variant="danger">{errorDelete}</Message>}

      {loadingCreate && <Loader />}
      {errorCreate && <Message variant="danger">{errorCreate}</Message>}

      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Table striped bordered hover responsive className="table-sm">
            <thead>
              <tr>
                <th>NAME</th>
                <th>IMAGE</th>
                <th>FILE</th>

                <th></th>
              </tr>
            </thead>

            <tbody>
              {movies.map((movie) => (
                <tr key={movie._id}>
                  <td>{movie.name}</td>
                  <td>
                    <img src={movie.image} alt={movie.name} />
                  </td>
                  <td>
                    <video
                      src={movie.file}
                      type="video/mp4"
                      id="myvideo"
                      class="video-js"
                      controls
                      preload="auto"
                      width="485"
                      height="360"
                      muted="true"
                      data-setup="{}"
                    />
                  </td>

                  <td>
                    <LinkContainer to={`/admin/movie/${movie._id}/edit`}>
                      <Button variant="light" className="btn-sm">
                        <i className="fas fa-edit">Edit</i>
                      </Button>
                    </LinkContainer>

                    <Button
                      variant="danger"
                      className="btn-sm"
                      onClick={() => deleteHandler(movie._id)}
                    >
                      <i className="fas fa-trash">Delete</i>
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
          <Paginate pages={pages} page={page} isAdmin={true} />
        </div>
      )}
    </div>
  );
}

export default MoviesListScreen;
import React, { useEffect } from "react";
import { LinkContainer } from "react-router-bootstrap";
import { Table, Button, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import MovieForm from "../components/MovieForm";
import Paginate from "../components/Paginate";
import { listMovies, deleteMovie } from "../actions/movieActions";
import { MOVIE_CREATE_RESET } from "../constants/movieConstants";

function MoviesListScreen({ history, match }) {
  const dispatch = useDispatch();

  const movieList = useSelector((state) => state.movieList);
  const { loading, error, movies, pages, page } = movieList;

  const movieDelete = useSelector((state) => state.movieDelete);
  const {
    loading: loadingDelete,
    error: errorDelete,
    success: successDelete,
  } = movieDelete;

  const movieCreate = useSelector((state) => state.movieCreate);
  const {
    loading: loadingCreate,
    error: errorCreate,
    success: successCreate,
    movie: createdMovie,
  } = movieCreate;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  let keyword = history.location.search;
  useEffect(() => {
    dispatch({ type: MOVIE_CREATE_RESET });

    if (!userInfo.isAdmin) {
      history.push("/login");
    }

    if (successCreate) {
      history.push(`/admin/movies/${createdMovie._id}/edit`);
    } else {
      dispatch(listMovies(keyword));
    }
  }, [
    dispatch,
    history,
    userInfo,
    successDelete,
    successCreate,
    createdMovie,
    keyword,
  ]);

  const deleteHandler = (id) => {
    if (window.confirm("Are you sure you want to delete this movie?")) {
      dispatch(deleteMovie(id));
    }
  };

  return (
    <div>
      <Row className="align-items-center">
        <Col>
          <h1>movies</h1>
        </Col>
      </Row>

      <MovieForm />

      {loadingDelete && <Loader />}
      {errorDelete && <Message variant="danger">{errorDelete}</Message>}

      {loadingCreate && <Loader />}
      {errorCreate && <Message variant="danger">{errorCreate}</Message>}

      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Table striped bordered hover responsive className="table-sm">
            <thead>
              <tr>
                <th>NAME</th>
                <th>IMAGE</th>
                <th>FILE</th>

                <th></th>
              </tr>
            </thead>

            <tbody>
              {movies.map((movie) => (
                <tr key={movie._id}>
                  <td>{movie.name}</td>
                  <td>
                    <img src={movie.image} alt={movie.name} />
                  </td>
                  <td>
                    <video
                      src={movie.file}
                      type="video/mp4"
                      id="myvideo"
                      class="video-js"
                      controls
                      preload="auto"
                      width="485"
                      height="360"
                      muted="true"
                      data-setup="{}"
                    />
                  </td>

                  <td>
                    <LinkContainer to={`/admin/movie/${movie._id}/edit`}>
                      <Button variant="light" className="btn-sm">
                        <i className="fas fa-edit">Edit</i>
                      </Button>
                    </LinkContainer>

                    <Button
                      variant="danger"
                      className="btn-sm"
                      onClick={() => deleteHandler(movie._id)}
                    >
                      <i className="fas fa-trash">Delete</i>
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
          <Paginate pages={pages} page={page} isAdmin={true} />
        </div>
      )}
    </div>
  );
}

export default MoviesListScreen;
