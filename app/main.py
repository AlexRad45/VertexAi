from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import app.schemas as schemas
import app.generate_images as generate_images
import app.generate_text as generate_text

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
        return {"status": "failed"}

    # Implement saving to google storage here

    return {"status": "success"}


@router.post("/gentext")
def gen_text(gentext: schemas.GenText):
    try:
        response_text = generate_text.generate_text_from_prompt(
            gentext.prompt, gentext.max_output_tokens, gentext.temperature
        )

    except Exception as e:
        return {"status": "failed"}

    # Implement saving to google storage here

    return {"text": response_text}


app.include_router(router)
