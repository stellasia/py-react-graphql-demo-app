import './App.css';
import MovieList from './components/MovieList.js'

function App() {
  return (
    <div className="App">
	  <header className="App-header">
	  <h1>Movie database</h1>
	  </header>
	  <section>
	  {
	      <MovieList />
	  }
	  </section>
    </div>
  );
}

export default App;
