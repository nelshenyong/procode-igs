import { useState, useEffect } from "react";
import { OMDB_API_KEY } from "./config";
import Logo from "./components/Nav-bar/Logo";
import Search from "./components/Nav-bar/Search";
import NumResults from "./components/Nav-bar/Num-result";
import NavBar from "./components/Nav-bar/Nav-bar";
import Main from "./components/Nav-bar/Main";
import BoxMovies from "./components/box/Box-movie";
import MovieItem from "./components/box/movie-item";
import MovieList from "./components/box/movie-list";
import Loader from "./components/box/Loader";
import MovieDetails from "./components/box/Movie-detail";

function App() {
  const [query,setQuery]=useState("oppenheimer")
  const [movies,setMovies]=useState([])
  const [selectedMovieId,setSelectedMovieId]=useState(null);
  const [isLoading,setIsLoading]=useState(false)
  function handleSelectedMovieId(id){
    setSelectedMovieId((selectedId)=>(selectedId===id?null:id));
  }
  function handleCloseMovie(){
    selectedMovieId(null)
  }
  useEffect(()=>{
    async function fetchMovie() {
      try{
        setIsLoading(true);
        const res=await fetch(
          `http://www.omdbapi.com/?s=${query}&apikey=${OMDB_API_KEY}`
        )
        const data = await res.json();
        // console.log(data.Search)
        setMovies(data.Search||[])
        setIsLoading(false)
      } catch(err){
        console.log(err)
      }
    }
    if(query.length<3){
      setMovies([])
      return
    }
    fetchMovie();
  },[query])
  return (
    <>
      <NavBar>
        <Logo/>
        <Search query={query} setQuery={setQuery}/>
        <NumResults movies={movies}/>
      </NavBar>
      <Main>
        <BoxMovies>
          {isLoading ?
              <Loader/> :
              <MovieList movies={movies} onSelectMovieId={handleSelectedMovieId}/>}
        </BoxMovies>
        <BoxMovies>
          {selectedMovieId &&(
              <MovieDetails selectedId={selectedMovieId} onCloseMovie={handleCloseMovie}/>
          )}
        </BoxMovies>
      </Main>
    </>
  )
}
export default App;