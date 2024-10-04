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

            env_entry = next((entry for entry in env_service_list if entry['environment'] == env), None)
            if env_entry:
                env_entry['services'].append(service)
            else:
                env_service_list.append({'environment': env, 'services': [service]})

    # Convert to a matrix-friendly format
    matrix_output = [{'environment': entry['environment'], 'service': svc}
                     for entry in env_service_list for svc in entry['services']]

    output_string = json.dumps(matrix_output)
    
    '''
    # Approach 1 Write to GITHUB_OUTPUT
    #with open(os.getenv('GITHUB_OUTPUT'), 'a') as output_file:
    #    output_file.write(f'env_service_matrix={output_string}\n')
    '''
    # Approach 2
    with open(os.getenv('GITHUB_OUTPUT'), 'at', encoding="utf-8") as outfile:
        outfile.write(f'env_service_matrix={output_string}\n')

# Call the function
extract_environment_and_service()
