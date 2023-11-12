import openai
import json

with open("data/chatgpt_credentials.json", "r") as config_file:
    config_data = json.load(config_file)
    api_key = config_data.get("openai_api_key", "")

openai.api_key = api_key


def chat_with_gpt():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Given an initial product name and description you will generate new unique product descriptions then generate the material names, unit_cost and quantity. Do not include any explanations, only provide a RFC8259 compliant JSON response",
                },
                {
                    "role": "system",
                    "name": "example_user",
                    "content": """What materials can be used to create a Green and Purple Women's Skirt with this description: Dark Green and Dark Purple patterned cotton weave, featuring a Mesh & crinkled chiffon underskirt. This skirt is designed with a Printed weave for a nautical touch, a solid color base for versatility, and a pleated wrapover style. It comes with a Twill waistband for comfort and a slit at the front for a hint of allure. """,
                },
                {
                    "role": "system",
                    "name": "example_assistant",
                    "content": """{ "input_text": "What materials can be used to create a Green and Purple Women's Skirt with this description: Dark Green and Dark Purple patterned cotton weave, featuring a Mesh & crinkled chiffon underskirt. This skirt is designed with a Printed weave for a nautical touch, a solid color base for versatility, and a pleated wrapover style. It comes with a Twill waistband for comfort and a slit at the front for a hint of allure.", "output_text": [ { "name": "Dark Green and Dark Purple Fabric", "unit_cost": 15.99, "quantity": 2 }, { "name": "Mesh Fabric", "unit_cost": 9.99, "quantity": 1.5 }, { "name": "Crinkled Chiffon", "unit_cost": 12.49, "quantity": 1 }, { "name": "Printed Weave Fabric", "unit_cost": 14.99, "quantity": 1.5 }, { "name": "Solid Color Fabric", "unit_cost": 13.99, "quantity": 1.5 }, { "name": "Twill Fabric", "unit_cost": 10.99, "quantity": 1 }, { "name": "Zippers or Buttons", "unit_cost_per_unit": 1.25, "quantity": 2 }, { "name": "Thread and Sewing Supplies", "unit_cost": 9.99, "quantity": 1 }, { "name": "Interfacing", "unit_cost": 5.99, "quantity": 0.5 }, { "name": "Slit Material", "unit_cost": 7.99, "quantity": 0.5 } ]}""",
                },
                {
                    "role": "user",
                    "content": """ Generate a new clothing product description, and then from that description, generate a list of materials that could be used to create the product. There must be at least 4 materials and vary how the input text is presented so that it does not always start with "what materials can be used to create..", however it should start with some variation of asking what materials can be used to create the item. Ensure it follows the same JSONL format as before""",
                },
            ],
        )
        return response.choices[0].message["content"]

    except Exception as e:
        print(f"Error: {e}")
        return None


with open("comps_responses.txt", "w") as file:
    for i in range(10):
        response = chat_with_gpt()
        if response != None:
            file.write(f"{response}\n")
            print(f"Response: {response}n")

print("Responses saved")
