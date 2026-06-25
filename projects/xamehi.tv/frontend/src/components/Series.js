<<<<<<< HEAD
import React from "react";
import { Card } from "react-bootstrap";
import { Link } from "react-router-dom";

import Rating from "./Rating";

const Series = ({ post }) => {
  return (
    <Card className="my-3 p-3 rounded">
      <Card.Body>
        <Card.Title as="div">
          <Link to={`/serie/${post._id}`}>
            <h4>{post.name}</h4>
          </Link>
          <Link to={`/serie/${post._id}`}>
            <Card.Img src={post.image} />
          </Link>
        </Card.Title>
        <Card.Text as="div">
          <div className="my-3">
            <Rating
              value={post.rating}
              text={`${post.likes} likes`}
              color={"#f8e825"}
            />
          </div>
        </Card.Text>
        <Card.Text as="h4">{post.rating}</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default Series;
=======
import React from "react";
import { Card } from "react-bootstrap";
import { Link } from "react-router-dom";

import Rating from "./Rating";

const Series = ({ post }) => {
  return (
    <Card className="my-3 p-3 rounded">
      <Card.Body>
        <Card.Title as="div">
          <Link to={`/serie/${post._id}`}>
            <h4>{post.name}</h4>
          </Link>
          <Link to={`/serie/${post._id}`}>
            <Card.Img src={post.image} />
          </Link>
        </Card.Title>
        <Card.Text as="div">
          <div className="my-3">
            <Rating
              value={post.rating}
              text={`${post.likes} likes`}
              color={"#f8e825"}
            />
          </div>
        </Card.Text>
        <Card.Text as="h4">{post.rating}</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default Series;
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
