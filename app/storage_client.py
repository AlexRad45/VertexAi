from google.cloud import storage
import os


def init_storage():
    storage_credentials = "data/images-storage-service-account.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = storage_credentials

    storage_client = storage.Client(project="omnithink")

    storage_bucket = storage_client.get_bucket("omni_images_47")

    return storage_bucket


def upload_blob_fromfile(bucket, source_file, destination_blob):
    blob = bucket.blob(destination_blob)
    blob.upload_from_file(source_file)


def upload_blob_fromstr(bucket, text, destination_blob):
    blob = bucket.blob(destination_blob)
    blob.upload_from_string(text)
