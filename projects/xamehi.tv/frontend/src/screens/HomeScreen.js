<<<<<<< HEAD
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
=======
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
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
