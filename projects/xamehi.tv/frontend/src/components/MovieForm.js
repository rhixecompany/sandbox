import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";
import FormContainer from "../components/FormContainer";
import Message from "../components/Message";

const MovieForm = () => {
  const [name, setName] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {}, []);

  const submitHandler = (e) => {
    e.preventDefault();

    setMessage("Movie Created");
  };

  return (
    <FormContainer>
      <h3>Movie Create Form</h3>
      {message && <Message variant="danger">{message}</Message>}
      <Form onSubmit={submitHandler}>
        <Form.Group controlId="name">
          <Form.Label>Name</Form.Label>
          <Form.Control
            required
            type="name"
            placeholder="Enter name"
            value={name}
            onChange={(e) => setName(e.target.value)}
          ></Form.Control>
        </Form.Group>
        <Button type="submit" variant="primary">
          Create
        </Button>
      </Form>
    </FormContainer>
  );
};

export default MovieForm;
