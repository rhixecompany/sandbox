# Code Exemplars — xamehi.tv

## 1. DRF ViewSet with JWT Auth

```python
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
```

## 2. Redux Action with Axios

```javascript
export const fetchMovies = () => async (dispatch) => {
  dispatch({ type: MOVIE_LIST_REQUEST });
  try {
    const { data } = await axios.get("/api/movies/");
    dispatch({ type: MOVIE_LIST_SUCCESS, payload: data });
  } catch (error) {
    dispatch({
      type: MOVIE_LIST_FAIL,
      payload: error.response?.data?.message || error.message,
    });
  }
};
```
