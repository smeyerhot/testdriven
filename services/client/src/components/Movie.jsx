import React, { useEffect, useState } from "react";
// import "./App.css";
import { Movies } from "./Movies";
import { MovieForm } from "./MovieForm";
import { Container } from "semantic-ui-react";


function Movie() {
  const [movies, setMovies] = useState([]);
  // axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/people/movies`)
  useEffect(() => {
    fetch(`${process.env.REACT_APP_USERS_SERVICE_URL}/people`).then(response =>
      response.json().then(data => {
        setMovies(data.movies);
        
      })
    );
  }, []);

  return (
    <Container style={{ marginTop: 40 }}>
      <MovieForm
        onNewMovie={movie =>
          setMovies(currentMovies => [movie, ...currentMovies])
        }
      />
      <Movies movies={movies} />
    </Container>
  );
}

export default Movie;