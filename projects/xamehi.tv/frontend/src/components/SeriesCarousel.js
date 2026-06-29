import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Link } from "react-router-dom";
import { Carousel, Image } from "react-bootstrap";
import Loader from "./Loader";
import Message from "./Message";
import { listTopSeries } from "../actions/seriesActions";

const SeriesCarousel = () => {
  const dispatch = useDispatch();

  const seriesTopRated = useSelector((state) => state.seriesTopRated);
  const { error, loading, series } = seriesTopRated;

  useEffect(() => {
    dispatch(listTopSeries());
  }, [dispatch]);
  return loading ? (
    <Loader />
  ) : error ? (
    <Message variant="danger">{error}</Message>
  ) : (
    <Carousel pause="hover" className="bg-dark">
      {series.map((serie) => (
        <Carousel.Item key={serie._id}>
          <Link to={`/series/${serie._id}`}>
            <Image src={serie.image} alt={serie.name} fluid />
            <Carousel.Caption className="carousel.caption">
              <h4>{serie.name}</h4>
            </Carousel.Caption>
          </Link>
        </Carousel.Item>
      ))}
    </Carousel>
  );
};

export default SeriesCarousel;
