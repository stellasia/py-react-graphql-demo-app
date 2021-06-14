import React, {useState} from 'react';
import {
  useQuery,
  gql
} from "@apollo/client";
import MovieForm from './MovieForm.js';

export const LIST_MOVIES = gql`
  query GetMovies {
    movies {
      title
      released
      image
    }
  }
`;

const MovieList = () => {
    const [showForm, setShowForm] = useState(false);
    const { loading, error, data } = useQuery(LIST_MOVIES);
    
    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error</p>;

    
    return (
	<>
	    <button onClick={() => setShowForm(!showForm)}>New Movie</button>
	    <MovieForm show={showForm} />
	    <table>
		<thead>
		    <tr>
			<th>Title</th>
			<th>Released</th>
			<th>Image</th>
		    </tr>
		</thead>
		<tbody>
		    {
			data.movies.map((movie) => {
			    return (
				<tr>
				    <td>{movie.title}</td>
				    <td>{movie.released}</td>
				    <td>{movie.image ? <img src={movie.image} alt='movie poster' width="200px" /> : null }</td>
				</tr>
			    )
			})
		    }
		</tbody>
	    </table>
	</>
    )
}

export default MovieList
