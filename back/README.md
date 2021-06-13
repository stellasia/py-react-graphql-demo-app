# Backend GraphQL API (Flask + ariadne)

NB: this is a test project, to experiment and demonstrate how to do GraphQL with Python and Neo4j
It is not configured and not meant to be used in production.


## Features

- Model definition using Neomodel
- GraphQL schema with Ariadne
- GraphQL view with Flask
- Support for file upload to Google Cloud Storage


## Setup

### Database: Neo4j

With the movie database.

### Python env

Virtual env:

    python3 -m venv venv
    pip install --upgrade pip
    pip install -r requirements.txt


## Running the app locally

    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
    export BUCKET_NAME=myBucket
    flask run


## Testing

- Recommended: Use a graphical GraphQL explorer (eg: [`altair`](https://altair.sirmuel.design/)).
- Or: any tool to perform HTTP query will work (curl, Postman, httpie...)
