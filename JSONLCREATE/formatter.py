import json


def format_output_text(input_dict):
    output_text_list = input_dict.get("output_text", [])

    # Convert each dictionary to a string without outer curly braces
    output_text_str = ", ".join(
        json.dumps(item, ensure_ascii=False) for item in output_text_list
    )

    # Update the 'output_text' key in the input_dict directly
    input_dict["output_text"] = f"{output_text_str}"

    return json.dumps(input_dict, ensure_ascii=False)


# Input and output file paths
input_file_path = "descriptionB.jsonl"
output_file_path = "formatted_description.jsonl"

# Open input and output files
with open(input_file_path, "r") as input_file, open(
    output_file_path, "w"
) as output_file:
    # Process each line in the input file
    for line in input_file:
        # Parse each JSON line
        input_dict = json.loads(line)

        # Format the output_text section and write to the output file
        formatted_line = format_output_text(input_dict)
        output_file.write(formatted_line + "\n")

print(f"Formatting completed. Formatted output saved to '{output_file_path}'.")
