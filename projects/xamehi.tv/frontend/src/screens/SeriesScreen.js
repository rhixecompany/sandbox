import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Row, Col, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import Loader from "../components/Loader";
import Message from "../components/Message";
import SeriesPaginate from "../components/SeriesPaginate";
import Series from "../components/Series";
import SearchBox from "../components/SearchBox";
import SeriesCarousel from "../components/SeriesCarousel";

import { listSeries } from "../actions/seriesActions";

const SeriesScreen = ({ history }) => {
  const dispatch = useDispatch();

  const seriesList = useSelector((state) => state.seriesList);
  const { error, loading, series, page, pages } = seriesList;

  let keyword = history.location.search;

  useEffect(() => {
    dispatch(listSeries(keyword));
  }, [dispatch, keyword]);

  return (
    <div>
      <div>
        <SearchBox />
      </div>
      {!keyword && <SeriesCarousel />}
      <Link to="/movies">
        <Button>Views Movies</Button>
      </Link>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <div>
            <Row>
              {series.map((post) => (
                <Col key={post._id} sm={12} md={6} lg={4} xl={3}>
                  <Series post={post} />
                </Col>
              ))}
            </Row>
            <SeriesPaginate page={page} pages={pages} keyword={keyword} />
          </div>
        </div>
      )}
    </div>
  );
};

export default SeriesScreen;
