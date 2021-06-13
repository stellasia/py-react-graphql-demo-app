"""
Override behaviour for ariadne Upload scalar type
"""
import os
import random
import string
import datetime
from google.cloud import storage

from ariadne.file_uploads import upload_scalar


BUCKET_NAME = os.getenv("BUCKET_NAME", "")


def parse_upload_value(obj):
    """Input value (eg: mutation)

    obj is a file
    """
    # push file to gcloud and return URL
    name = None
    if obj:
        # https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
        # print(image.filename, image.content_type, image.name, image.stream)
        # image_blob = bucket.blob(f'users/test')
        # image_blob.upload_from_file(
        #    imagefile.stream,
        #    content_type=imagefile.content_type
        # )
        rid = ''.join(random.sample(string.ascii_letters, 4))
        name = f"{obj.filename}_{rid}.png"
        obj.save(name)
    return name


def parse_upload_value_and_push_to_gcloud_storage(obj):
    """
    """
    if obj is None:
        return obj
    # project = os.getenv("GCLOUD_PROJECT")
    # bucket = bucket or settings.GCLOUD_STORAGE_BUCKET_NAME
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    rid = ''.join(random.sample(string.ascii_letters, 4))
    name = f"{obj.filename}_{rid}.png"
    blob = bucket.blob(name)
    blob.upload_from_file(obj.stream)
    # return blob.public_url
    return name


def serialize_upload_value(value):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(value)
    url = blob.generate_signed_url(
        version="v4",
        expiration=datetime.timedelta(minutes=15),
        method="GET",
    )
    return url
