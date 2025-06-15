import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
if len(sys.argv) >= 2:
    input_string = sys.argv[1]
else:
    print("No input detected")
    exit(1)

messages = [
    types.Content(role="user", parts=[types.Part(text=input_string)]),
]
response = client.models.generate_content(
    model='gemini-2.0-flash-001', contents=messages,
)
print(response.text)
if (len(sys.argv) >= 3) and (sys.argv[2] == "--verbose"):
    print("User prompt: " + input_string)
    print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    print("Response tokens: " + str(response.usage_metadata.candidates_token_count))