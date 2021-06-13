import json
from neomodel import config
from flask import Flask, request, jsonify
from flask_cors import CORS

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, ObjectType, combine_multipart_data, upload_scalar
from ariadne.constants import PLAYGROUND_HTML

from api.queries import (
    resolve_movies, resolve_movie,
)
from api.mutations import (
    resolve_create_movie,
)
from api.scalars import (
    parse_upload_value_and_push_to_gcloud_storage,
    serialize_upload_value,
)

config.DATABASE_URL = 'bolt://neo4j:admin@localhost:7687'

app = Flask(__name__)
CORS(app)


# queries
query = ObjectType("Query")
query.set_field("movies", resolve_movies)
query.set_field("movie", resolve_movie)

# mutations
mutation = ObjectType("Mutation")
mutation.set_field("createMovie", resolve_create_movie)

# custom scalar definition
upload_scalar.set_value_parser(parse_upload_value_and_push_to_gcloud_storage)
upload_scalar.set_serializer(serialize_upload_value)


# graphql schema
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs,
    [
        query,
        mutation,
        upload_scalar,
    ]
)


# Flask view
@app.route("/graphql", methods=["POST"])
def graphql_server():
    # manage multi part request to deal with files
    if request.content_type.startswith("multipart/form-data"):
        data = combine_multipart_data(
            json.loads(request.form.get("operations")),
            json.loads(request.form.get("map")),
            dict(request.files)
        )
    else:
        data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
