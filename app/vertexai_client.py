import vertexai
import os


def init_vertexai():
    vertexai_credentials = "data/vertexai_credentials.json"
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = vertexai_credentials

    vertexai.init(project="omnithink")
