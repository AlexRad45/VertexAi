import openai
import time



# { "input_text": "", "output_text": [ ]}
def chat_with_gpt():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Given a clothing product description you will generate a new product name, description, a prompt to generate a corresponding image, containing only keywords split by commas. Do not include any explanations, only provide a RFC8259 compliant JSON response",
                },
                {
                    "role": "system",
                    "name": "example_user",
                    "content": """ A new product design of Ladieswear Skirt, Women’s Trend. Use attributes from "Dark Green, Dark Purple, Patterned cotton weave, Mesh & crinkled chiffon, Printed weave, Solid, Mesh underskirt, Pleated wrapover, Twill waistband, Slit at the front". Make it very Nautical and slightly Shiny. Make it suitable for Female ages 25-35 Affluent Metro.""",
                },
                {
                    "role": "system",
                    "name": "example_assistant",
                    "content": """ {"input_text":"A new product design of Ladieswear Skirt, Women’s Trend. Dark Green, Dark Purple, Patterned cotton weave, Mesh & crinkled chiffon, Printed weave, Solid, Mesh underskirt, Pleated wrapover, Twill waistband, Slit at the front. Make it very Nautical and slightly Shiny. Suitable for Female ages 25-35 Affluent Metro." , "output_text": [{"name": "Nautical Elegance Skirt"}, {"description": "Dark Green and Dark Purple patterned cotton weave, featuring a Mesh & crinkled chiffon underskirt. This skirt is designed with a Printed weave for a nautical touch, a solid color base for versatility, and a pleated wrapover style. It comes with a Twill waistband for comfort and a slit at the front for a hint of allure."}, {"image_prompt": "Skirt, Dark Green, Dark Purple, Patterned cotton weave, Mesh & crinkled chiffon, Printed weave, Solid, Mesh underskirt, Pleated wrapover, Twill waistband, Slit at the front, Nautical, Slightly Shiny, Female, 25-35, Affluent Metro"}]}""",
                },
                {
                    "role": "system",
                    "name": "example_user",
                    "content": """ A new product design of Men's T-shirt, Casual style. Use attributes from Cotton fabric, Round neck, Short sleeves, Solid color, Regular fit. Make it vibrant and trendy. Suitable for Male ages 18-30 Urban.""",
                },
                {
                    "role": "system",
                    "name": "example_assistant",
                    "content": """ {A new product design of Men's T-shirt, Casual style. Use attributes from Cotton fabric, Round neck, Short sleeves, Solid color, Regular fit. Make it vibrant and trendy. Suitable for Male ages 18-30 Urban." , "output_text": [{"name": "Urban Vibes T-shirt"}, {"description": "Stay comfortable and stylish with our Urban Vibes T-shirt. Made from soft cotton fabric, this t-shirt features a classic round neck and short sleeves. The solid color design adds a timeless appeal, while the regular fit ensures a comfortable wear. Suitable for males aged 18-30 living in urban areas, this t-shirt is perfect for everyday casual wear."}, {"image_prompt": "T-shirt, Cotton fabric, Round neck, Short sleeves, Solid color, Regular fit, Vibrant, Trendy, Male, 18-30, Urban"}]}""",
                },
                {
                    "role": "user",
                    "content": """ Generate a new brief clothing product description matching the format of the examples(no dresses, pants, shirts, hoodies), make sure the product is diverse and that you generate different results when run multiple times (no floral print), and from that description generate a new product name, description, and a prompt to generate a corresponding image. Provide only a RFC8259 compliant JSON response, ensure the format of the input follows the examples: A new product design of ... """,
                },
            ],
        )
        return response.choices[0].message["content"]

    except Exception as e:
        print(f"Error: {e}")
        return None


with open("description_responses.txt", "w") as file:
    for i in range(50):
        response = chat_with_gpt()
        if response != None:
            file.write(f"{response}\n")
            print(f"{response}\n")
        time.sleep(1)

print("Responses saved to prompt_responses_description.txt")
