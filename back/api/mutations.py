from api.models import Movie


def resolve_create_movie(obj, info, title, released=None, tagline=None, image=None):
    movie = Movie(
        title=title,
        released=released,
        tagline=tagline,
        image=image,
    )
    movie.save()
    payload = movie.to_dict()
    return payload
