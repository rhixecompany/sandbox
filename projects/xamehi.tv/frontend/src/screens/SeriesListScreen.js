import React, { useEffect } from "react";
import { LinkContainer } from "react-router-bootstrap";
import { Table, Button, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import SerieForm from "../components/SerieForm";
import SeriesPaginate from "../components/SeriesPaginate";
import { listSeries, deleteSeries } from "../actions/seriesActions";
import { SERIES_CREATE_RESET } from "../constants/seriesConstants";

const SeriesListScreen = ({ history, match }) => {
  const dispatch = useDispatch();

  const seriesList = useSelector((state) => state.seriesList);
  const { loading, error, series, pages, page } = seriesList;

  const seriesDelete = useSelector((state) => state.seriesDelete);
  const {
    loading: loadingDelete,
    error: errorDelete,
    success: successDelete,
  } = seriesDelete;

  const seriesCreate = useSelector((state) => state.seriesCreate);
  const {
    loading: loadingCreate,
    error: errorCreate,
    success: successCreate,
    series: createdSeries,
  } = seriesCreate;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  let keyword = history.location.search;

  useEffect(() => {
    dispatch({ type: SERIES_CREATE_RESET });

    if (!userInfo.isAdmin) {
      history.push("/login");
    }

    if (successCreate) {
      history.push(`/admin/series/${createdSeries._id}/edit`);
    } else {
      dispatch(listSeries(keyword));
    }
  }, [
    dispatch,
    history,
    userInfo,
    successDelete,
    successCreate,
    createdSeries,
    keyword,
  ]);

  const deleteHandler = (id) => {
    if (window.confirm("Are you sure you want to delete this series?")) {
      dispatch(deleteSeries(id));
    }
  };
  return (
    <div>
      <Row className="align-items-center">
        <Col>
          <h1>series</h1>
        </Col>
      </Row>

      <SerieForm />

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

                <th></th>
              </tr>
            </thead>

            <tbody>
              {series.map((post) => (
                <tr key={post._id}>
                  <td>{post.name}</td>
                  <td>
                    <img src={post.image} alt={post.name} />
                  </td>

                  <td>
                    <LinkContainer to={`/admin/serie/${post._id}/edit`}>
                      <Button variant="light" className="btn-sm">
                        <i className="fas fa-edit">Edit</i>
                      </Button>
                    </LinkContainer>

                    <Button
                      variant="danger"
                      className="btn-sm"
                      onClick={() => deleteHandler(post._id)}
                    >
                      <i className="fas fa-trash">Delete</i>
                    </Button>
                  </td>
                </tr>
              ))}
            </tbody>
          </Table>
          <SeriesPaginate pages={pages} page={page} isAdmin={true} />
        </div>
      )}
    </div>
  );
};

export default SeriesListScreen;
