import Loader from "./Loader";
import { OMDB_API_KEY } from "../../config";
import { useState, useEffect } from "react";

function MovieDetails({ selectedId, onCloseMovie }) {
  const [movie, setMovie] = useState({});
  const [isLoading, setIsLoading] = useState(false);

  const {
    Title: title,
    Year: year,
    Released: released,
    Poster: poster,
    imbdRating,
    Runtime: runtime,
    Plot: plot,
    Genre: genre,
    Actors: actors,
    Director: director,
  } = movie;

  useEffect(() => {
    async function getMovieDetails() {
      try {
        setIsLoading(true);
        const res = await fetch(
          `http://www.omdbapi.com/?apikey=${OMDB_API_KEY}&i=${selectedId}`
        );
        const data = await res.json();
        setMovie(data);
        setIsLoading(false);
      } catch (err) {
        console.log(err);
      }
    }
    getMovieDetails();
  }, [selectedId]);

  return (
    <div className="details">
      {isLoading ? (
        <Loader />
      ) : (
        <>
          <header>
            <button className="btn-back" onClick={onCloseMovie}>
              X
            </button>
            {poster !== "N/A" ? (
              <img src={poster} alt={`${title} poster`} />
            ) : (
              <div
                style={{
                  width: "200px",
                  height: "300px",
                  backgroundColor: "red",
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  color: "white",
                  fontWeight: "bold",
                }}
              >
                No Image Available
              </div>
            )}
            <div className="details-overview">
              <h2>{title}</h2>
              <p>
                <span>📅</span>
                <span>{released}</span>
              </p>
              <p>
                <span>⏱</span>
                <span>{runtime}</span>
              </p>
              <p>
                <span>⭐</span>
                <span>{imbdRating}</span>
              </p>
            </div>
          </header>
          <section>
            <p>
              <em>{plot}</em>
            </p>
            <p>Year : {year}</p>
            <p>Genre : {genre}</p>
            <p>Actors : {actors}</p>
            <p>Directed by : {director}</p>
          </section>
        </>
      )}
    </div>
  );
}

export default MovieDetails;
