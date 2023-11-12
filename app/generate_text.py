from vertexai.preview.language_models import TextGenerationModel, TextGenerationResponse
import app.vertexai_client as vertexai_client


def generate_text_from_prompt(
    prompt: str, max_output_tokens: int, temperature: float
) -> str:
    vertexai_client.init_vertexai()
    model = TextGenerationModel.from_pretrained("text-bison@001")

    response = model.predict(
        prompt=prompt, max_output_tokens=max_output_tokens, temperature=temperature
    )

    return response.text
