import openai
import time
import json

with open("data/chatgpt_credentials.json", "r") as config_file:
    config_data = json.load(config_file)
    api_key = config_data.get("openai_api_key", "")

openai.api_key = api_key


# { "input_text": "", "output_text": [ ]}
def chat_with_gpt():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Given a product description and attributes you will come up with an explanation why we came up with that product design in detail. Refer to specific attributes and trend reasons in the explanation. Only show the explanation. Make it between 7 and 10 sentences long",
                },
                {
                    "role": "system",
                    "name": "example_user",
                    "content": """This effortlessly chic mini dress features spaghetti straps and a straight silhouette printed all-over in a Briana Mora original - bold abstract shapes in coral, teal, yellow and ivory. Drawstring cinches the waist.""",
                },
                {
                    "role": "system",
                    "name": "example_assistant",
                    "content": """{"input_text":"This effortlessly chic mini dress features spaghetti straps and a straight silhouette printed all-over in a Briana Mora original - bold abstract shapes in coral, teal, yellow and ivory. Drawstring cinches the waist." , "output_text": "Firstly, it incorporates the "Briana Mora" and "saturated hues" realizing her signature bold, vibrant aesthetic in the abstract print. Secondly, the effortless faux wrap style flatters with its surplice neckline and tie waist. Thirdly, the slinky jersey moves gracefully due to the soft, fluid fabrication."}""",
                },
                {
                    "role": "user",
                    "content": """ Generate a new brief clothing product description, and from that description generate a new explanation paragraph as to why and how the product was designed. Reference key attributes in the input description to generate the explanation. Provide only a RFC8259 compliant JSON response""",
                },
            ],
        )
        return response.choices[0].message["content"]

    except Exception as e:
        print(f"Error: {e}")
        return None


with open("explanation_responses.txt", "w") as file:
    for i in range(100):
        response = chat_with_gpt()
        if response != None:
            file.write(f"{response}\n")
            print(f"{response}\n")
        time.sleep(1)

print("Responses saved to prompt_responses_description.txt")
