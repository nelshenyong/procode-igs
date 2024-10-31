import MovieItem from "./movie-item";
function MovieList({ movies, onSelectMovieId }) {
    return (
      <ul className="list list-movies">
        {movies?.map((movie) => (
          <MovieItem
            key={movie.imdbID}
            movie={movie}
            onSelectMovieId={onSelectMovieId}
          />
        ))}
      </ul>
    );
}
export default MovieList;