import React from 'react';
import { Formik } from 'formik';
import {LIST_MOVIES} from './MovieList.js';
import {
  useMutation,
  gql
} from "@apollo/client";


const CREATE_MOVIE = gql`
  mutation CreateMovie($title: String!, $released: Int, $image: Upload) {
    createMovie(title: $title, released: $released, image: $image) {
      title
    }
  }
`;


const MovieForm = (props) => {
    const {show} = props;

    const [createMovie] = useMutation(CREATE_MOVIE,);

    if (!show) return null

    return (
	<Formik
	    initialValues={{ title: '', released: null, image: null }}
	    validate={values => {
		const errors = {};
		return errors;
	    }}
	    onSubmit={(values, { setSubmitting }) => {
		console.log("form submit");
		setTimeout(() => {
		    console.log(values);
		    createMovie({
			variables: { title: values.title, released: values.released, image: values.image },
			refetchQueries: [
			    {query: LIST_MOVIES},
			]
		    });
		    setSubmitting(false);
		}, 400);
	    }}
	>
	    {({
		values,
		errors,
		handleChange,
		handleSubmit,
		isSubmitting,
		setFieldValue
		/* and other goodies */
	    }) => (
		<form onSubmit={handleSubmit}>
		    <label>Title:</label>
		    <input
			type="text"
			name="title"
			onChange={handleChange}
			value={values.title}
		    />
		    <input
			type="number"
			name="released"
			onChange={handleChange}
			value={values.releeased}
		    />
		    <input
			type="file"
			name="image"
			onChange={(event) => {
			    console.log(event);
			    if (event.target.files)
				setFieldValue("image", event.target.files[0]);
			}}
		    />
		    <button type="submit" disabled={isSubmitting}>
			Submit
		    </button>
		</form>
	    )}
	</Formik>
    )

}


export default MovieForm;
