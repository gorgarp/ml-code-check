import requests

# Authenticate with the OpenAI API
headers = {"Authorization": f"Bearer {your_api_key}"}

# Define the folder containing the files to be analyzed
folder_path = "path/to/folder"

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    with open(file_path, "r") as file:
        file_contents = file.read()

        # Submit the file contents to the OpenAI API for code analysis
        data = {"prompt": f"find code errors in this file {file_contents}"}
        response = requests.post("https://api.openai.com/v1/engines/davinci/completions", json=data, headers=headers)
        response_text = response.text

        # Extract the code errors from the API response
        errors = extract_errors_from_response(response_text)

        # Add the errors to the report
        for error in errors:
            report.append(f"{filename}: {error}")

# Save the report to a file
with open("code_errors_report.txt", "w") as report_file:
    for item in report:
        report_file.write("%s\n" % item)
