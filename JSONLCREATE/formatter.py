import re
import json


def format_output_text(input_dict):
    output_text_list = input_dict.get("output_text", [])

    # Iterate through each dictionary in the list
    for output_text_dict in output_text_list:
        for key, value in output_text_dict.items():
            if isinstance(value, str):
                # Find everything inside and including square brackets
                matches = re.findall(r"\[.*?\]", value)

                # Escape existing quotations within the matched sections
                for match in matches:
                    escaped_match = match.replace('"', r"\"")
                    value = value.replace(match, f'"{escaped_match}"')

                # Update the value in the dictionary
                output_text_dict[key] = value

    # Update the 'output_text' key
    input_dict["output_text"] = json.dumps(output_text_list)

    return json.dumps(input_dict)


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
