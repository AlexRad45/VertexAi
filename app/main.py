from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app import genimage

app = FastAPI()


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

app.include_router(genimage.router)
