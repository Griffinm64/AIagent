import os, sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

try:
    program_input = sys.argv[1]
except:
    raise SystemExit(1)


client = genai.Client(api_key=api_key)

client_response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=program_input)


print(client_response.text)
print(f"Prompt tokens: {client_response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {client_response.usage_metadata.candidates_token_count}")