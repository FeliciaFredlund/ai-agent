import os, sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

from llm_instructions import generate_content

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Agent")
        print('Usage: python3 main.py "your prompt here" [--verbose]')
        print('Example: python3 main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}")

    messages = [
        types.Content(
            role="user", 
            parts=[types.Part(text=user_prompt)]
        )
    ]

    generate_content(client, messages, verbose)


if __name__ == "__main__":
    main()