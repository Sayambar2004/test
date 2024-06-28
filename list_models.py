import google.generativeai as genai
import json
import os

# Load API key from config.json
working_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

apikey = config_data["Google_API_KEY"]

# Configure API key
genai.configure(api_key=apikey)

# List available models
models = genai.list_models()
print(models)
