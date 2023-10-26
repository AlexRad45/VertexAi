from pydantic import BaseModel


class GenImage(BaseModel):
    prompt: str
    hash: str
    number_of_images: int


class GenText(BaseModel):
    prompt: str
    max_output_tokens: int
    temperature: float
