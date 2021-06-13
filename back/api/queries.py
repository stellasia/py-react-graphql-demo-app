from .models import Movie


def resolve_movies(obj, info):
    try:
        payload = [
            movie.to_dict()
            for movie in Movie.nodes.all()
        ]
    except Exception as e:
        raise e
    return payload


def resolve_movie(obj, info, title):
    try:
        movie = Movie.nodes.get(title=title)
        payload = movie.to_dict()
    except Exception as e:
        raise e
    return payload
