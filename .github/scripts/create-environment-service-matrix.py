import json
import os
import re

def extract_environment_and_service():
    json_file_path = ".github/scripts/files.json"

    if not os.path.isfile(json_file_path):
        print("Error: files.json does not exist.")
        exit(1)

    env_service_list = []

    # Read the file paths from the JSON file
    with open(json_file_path, 'r') as json_file:
        file_paths = json.load(json_file)

    for file_path in file_paths:
        match = re.match(r'envs/([^/]+)/web-container/services/([^/]+)\.libsonnet', file_path)
        if match:
            env, service = match.groups()
            print(f"Matched file path: {file_path}")

            # Append each service under its respective environment
            env_service_list.append(f"{env}:{service}")

    # Write to GITHUB_OUTPUT
    output_file_path = os.getenv('GITHUB_OUTPUT')
    with open(output_file_path, 'a') as output_file:
        output_file.write(f'env_service_matrix={json.dumps(env_service_list)}\n')

# Call the function
extract_environment_and_service()
