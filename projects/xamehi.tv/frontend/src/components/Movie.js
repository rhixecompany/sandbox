import React from "react";
import { Card, Image } from "react-bootstrap";
import { Link } from "react-router-dom";

import Rating from "./Rating";

const Movie = ({ movie }) => {
  return (
    <Card className="my-3 p-3 rounded">
      <Card.Body>
        <Card.Title as="div">
          <Link to={`/movie/${movie._id}`}>
            <h4>{movie.name}</h4>
          </Link>
          <Link to={`/movie/${movie._id}`}>
            <Image src={movie.image} alt={movie.name} fluid />
          </Link>
        </Card.Title>

        <Card.Text as="div">
          <div className="my-3">
            <Rating
              value={movie.rating}
              text={`${movie.likes} likes`}
              color={"#f8e825"}
            />
          </div>
        </Card.Text>
        <Card.Text as="h4">{movie.rating}</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default Movie;
