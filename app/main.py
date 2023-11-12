from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import app.schemas as schemas
import app.generate_images as generate_images
import app.generate_text as generate_text
import app.storage_client as storage_client
import os, PIL, io

app = FastAPI()
router = APIRouter()

# for edit later when serving the main app
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:36021",
    # domain
    "http://portal.omnithink.ai",
    "https://portal.omnithink.ai",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@router.post("/genimage")
def gen_images(genimage: schemas.GenImage):
    try:
        response_images = generate_images.generate_images_from_prompt(
            genimage.prompt, genimage.number_of_images
        )

    except Exception as e:
        print(e)
        return {"status": "failed"}

    bucket = storage_client.init_storage()
    for i, image_data in enumerate(response_images):
        # Construct a unique destination blob name for each image
        destination_blob_name = f"image_response{i}.png"

        # Upload the image to the bucket
        storage_client.upload_blob_fromfile(
            bucket, io.BytesIO(image_data._image_bytes), destination_blob_name
        )

    """for i, image_data in enumerate(response_images):
        # Save each image locally in the "images" folder
        image_path = os.path.join("images", f"image_response{i}.png")
        image_data.save(image_path, "PNG")"""

    return {"status": "success"}


@router.post("/gentext")
def gen_text(gentext: schemas.GenText):
    try:
        response_text = generate_text.generate_text_from_prompt(
            gentext.prompt, gentext.max_output_tokens, gentext.temperature
        )

    except Exception as e:
        return {"status": "failed"}

    bucket = storage_client.init_storage()
    # create unique id for response
    destination_blob_name = f"text_response.txt"
    # maybe need another setup for text responses? new bucket

    storage_client.upload_blob_fromstr(bucket, response_text, destination_blob_name)

    print(response_text)
    return {"text": response_text}


app.include_router(router)
