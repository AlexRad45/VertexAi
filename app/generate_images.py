from vertexai.preview.vision_models import ImageGenerationModel, ImageGenerationResponse
import app.vertexai_client as vertexai_client


def generate_images_from_prompt(
    prompt: str, number_of_images: int
) -> ImageGenerationResponse:
    vertexai_client.init_vertexai()
    model = ImageGenerationModel.from_pretrained("imagegeneration@002")

    response = model.generate_images(
        prompt=prompt,
        number_of_images=number_of_images,
        seed=0,
    )

    return response
