<<<<<<< HEAD
import React, { useEffect } from "react";
import { Row, Col, Image } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { listSeriesDetails } from "../actions/seriesActions";

const SerieScreen = ({ match }) => {
  const dispatch = useDispatch();
  const seriesDetails = useSelector((state) => state.seriesDetails);
  const { error, loading, serie } = seriesDetails;
  let id = match.params.id;

  useEffect(() => {
    dispatch(listSeriesDetails(id));
  }, [dispatch, id]);

  return (
    <div>
      <h2>{serie.name}</h2>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Row>
            <Col>
              <Image src={serie.image} alt={serie.name} fluid />
              <p>{serie.description}</p>
              <i>{serie.createdAt}</i>
              <span>{serie.actor}</span>
              <span>{serie.rating}</span>
              <span>{serie.numReviews}</span>
            </Col>
          </Row>
          <ul>
            <h2>Episodes</h2>
            <li>
              <div>
                <h3>{serie.episodes}</h3>
              </div>
            </li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default SerieScreen;
=======
import React, { useEffect } from "react";
import { Row, Col, Image } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { listSeriesDetails } from "../actions/seriesActions";

const SerieScreen = ({ match }) => {
  const dispatch = useDispatch();
  const seriesDetails = useSelector((state) => state.seriesDetails);
  const { error, loading, serie } = seriesDetails;
  let id = match.params.id;

  useEffect(() => {
    dispatch(listSeriesDetails(id));
  }, [dispatch, id]);

  return (
    <div>
      <h2>{serie.name}</h2>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <Row>
            <Col>
              <Image src={serie.image} alt={serie.name} fluid />
              <p>{serie.description}</p>
              <i>{serie.createdAt}</i>
              <span>{serie.actor}</span>
              <span>{serie.rating}</span>
              <span>{serie.numReviews}</span>
            </Col>
          </Row>
          <ul>
            <h2>Episodes</h2>
            <li>
              <div>
                <h3>{serie.episodes}</h3>
              </div>
            </li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default SerieScreen;
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
