import React, { useState, useEffect } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import { Form, Button } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import FormContainer from "../components/FormContainer";
import { listMovieDetails, updateMovie } from "../actions/movieActions";
import { MOVIE_UPDATE_RESET } from "../constants/movieConstants";

function MoviesEditScreen({ match, history }) {
  const movieId = match.params.id;

  const [name, setName] = useState("");

  const [image, setImage] = useState("");
  const [file, setFile] = useState("");

  const [description, setDescription] = useState("");
  const [uploading, setUploading] = useState(false);

  const dispatch = useDispatch();

  const movieDetails = useSelector((state) => state.movieDetails);
  const { error, loading, movie } = movieDetails;

  const movieUpdate = useSelector((state) => state.movieUpdate);
  const {
    error: errorUpdate,
    loading: loadingUpdate,
    success: successUpdate,
  } = movieUpdate;

  useEffect(() => {
    if (successUpdate) {
      dispatch({ type: MOVIE_UPDATE_RESET });
      history.push("/admin/movies");
    } else {
      if (!movie.name || movie._id !== Number(movieId)) {
        dispatch(listMovieDetails(movieId));
      } else {
        setName(movie.name);

        setImage(movie.image);
        setFile(movie.file);

        setDescription(movie.description);
      }
    }
  }, [dispatch, movie, movieId, history, successUpdate]);

  const submitHandler = (e) => {
    e.preventDefault();
    dispatch(
      updateMovie({
        _id: movieId,
        name,

        image,
        file,

        description,
      })
    );
  };

  const uploadFileHandler = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();

    formData.append("file", file);
    formData.append("movie_id", movieId);

    setUploading(true);

    try {
      const config = {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      };

      const { data } = await axios.post(
        "/api/movies/upload/",
        formData,
        config
      );

      setFile(data);
      setUploading(false);
    } catch (error) {
      setUploading(false);
    }
  };

  return (
    <div>
      <Link to="/admin/movies">Go Back</Link>

      <FormContainer>
        <h1>Edit Movie</h1>
        {loadingUpdate && <Loader />}
        {errorUpdate && <Message variant="danger">{errorUpdate}</Message>}

        {loading ? (
          <Loader />
        ) : error ? (
          <Message variant="danger">{error}</Message>
        ) : (
          <Form onSubmit={submitHandler}>
            <Form.Group controlId="name">
              <Form.Label>Name</Form.Label>
              <Form.Control
                type="name"
                placeholder="Enter name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              ></Form.Control>
            </Form.Group>

            <Form.Group controlId="description">
              <Form.Label>Description</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              ></Form.Control>
            </Form.Group>

            <Form.Group controlId="image">
              <Form.Label>Image</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter image"
                value={image}
                onChange={(e) => setImage(e.target.value)}
              ></Form.Control>
            </Form.Group>

            <Form.Group controlId="file">
              <Form.Label>File</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter File"
                value={file}
                onChange={(e) => setFile(e.target.value)}
              ></Form.Control>

              <Form.File
                id="video-file"
                label="Choose File"
                custom
                onChange={uploadFileHandler}
              ></Form.File>
              {uploading && <Loader />}
            </Form.Group>

            <Button type="submit" variant="primary">
              Update
            </Button>
          </Form>
        )}
      </FormContainer>
    </div>
  );
}

export default MoviesEditScreen;
