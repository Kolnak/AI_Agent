import os, sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
client = genai.Client(api_key=api_key)
if len(sys.argv) >= 2:
    input_string = sys.argv[1]
else:
    print("No input detected")
    exit(1)

response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=input_string
)
print(response.text)
print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
print("Response tokens: " + str(response.usage_metadata.candidates_token_count))