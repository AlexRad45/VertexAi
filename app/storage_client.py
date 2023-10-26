from google.cloud import storage
import os


def init_storage():
    storage_credentials = "data/storage_credentials.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = storage_credentials

    storage_client = storage.Client(project="omnithink")

    storage_bucket = storage_client.get_bucket("omni_images_47")

    return storage_bucket
