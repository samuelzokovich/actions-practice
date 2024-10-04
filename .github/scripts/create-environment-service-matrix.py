import json
import os
import re

def extract_environment_and_service():
    # Path to the JSON file that stores file changes from the last commit
    json_file_path = os.path.expanduser(".github/scripts/files.json")

    if not os.path.isfile(json_file_path):
        print("Error: files.json does not exist.")
        exit(1)

    # List to hold environments and their respective services
    env_service_list = []

    # Read the file paths from the JSON file
    with open(json_file_path, 'r') as json_file:
        file_paths = json.load(json_file)

    # Loop through each file path and extract the environment and service names
    for file_path in file_paths:
        match = re.match(r'envs/([^/]+)/web-container/services/([^/]+)\.libsonnet', file_path)
        if match:
            env, service = match.groups()
            print(f"Matched file path: {file_path}")

            # Check if the environment already exists in the list
            env_entry = next((entry for entry in env_service_list if entry['environment'] == env), None)
            if env_entry:
                # If it exists, append the service to the existing list
                env_entry['services'].append(service)
            else:
                # If it does not exist, create a new entry
                env_service_list.append({'environment': env, 'services': [service]})

    # Convert to JSON and write to a file for GitHub Actions to capture
    output_file_path = os.getenv('GITHUB_OUTPUT', 'output.json')
    with open(output_file_path, 'w') as output_file:
        json.dump(env_service_list, output_file)

# Call the function
extract_environment_and_service()
