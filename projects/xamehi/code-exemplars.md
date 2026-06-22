# Code Exemplars — xamehi

## 1. Express.js Server

```javascript
const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

app.get("/api/health", (req, res) => {
  res.json({ status: "ok" });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server on port ${PORT}`));
```

## 2. Axios React Component

```jsx
import { useState, useEffect } from "react";
import axios from "axios";

function MovieList() {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/api/movies/")
      .then((res) => setMovies(res.data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="movie-list">
      {movies.map((movie) => (
        <div key={movie.id}>{movie.title}</div>
      ))}
    </div>
  );
}
```
