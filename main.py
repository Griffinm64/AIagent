import os, sys
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai
from google.genai import types

# from subdirectory.filename import function_name
from functions.get_files_info import get_files_info



def main():
#accept user input, exit if nothing passed
    try:
        user_prompt = sys.argv[1]
    except:
        raise SystemExit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt) ]),
    ]


    #calls api key from stored value
    client = genai.Client(api_key=api_key)

    #calls llm model and passes previous input
    client_response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages)


    #displays result. If verbose flag is passed include usage tokens.
    print(client_response.text)
    try:
        if "--verbose" in sys.argv:
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {client_response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {client_response.usage_metadata.candidates_token_count}")
    except:
        pass

if __name__ == "__main__":
    main()