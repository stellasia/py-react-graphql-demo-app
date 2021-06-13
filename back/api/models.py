from neomodel import (
    StructuredNode,
    StringProperty, IntegerProperty,
)


class Movie(StructuredNode):
    title = StringProperty()
    tagline = StringProperty()
    released = IntegerProperty()
    image = StringProperty()

    def to_dict(self):
        return {
            "title": self.title,
            "tagline": self.tagline,
            "released": self.released,
            "image": self.image,
        }
