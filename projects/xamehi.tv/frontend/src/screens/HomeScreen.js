import React from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";

const HomeScreen = () => {
  return (
    <div>
      <Link to="/movies">
        <Button>Views Recent Movies</Button>
      </Link>
      <Link to="/series">
        <Button>Views Recent Series</Button>
      </Link>
    </div>
  );
};

export default HomeScreen;
import React from "react";
import { Link } from "react-router-dom";
import { Button } from "react-bootstrap";

const HomeScreen = () => {
  return (
    <div>
      <Link to="/movies">
        <Button>Views Recent Movies</Button>
      </Link>
      <Link to="/series">
        <Button>Views Recent Series</Button>
      </Link>
    </div>
  );
};

export default HomeScreen;
