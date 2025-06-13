import os
import base64
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Initialize the Google GenAI client globally
client = None

# Function to load environment variables from a .env file
def configure():
    load_dotenv()

# Function to generate response using the Google GenAI client
def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash-lite"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""Tell me about Androids Dreaming about Electric Sheep."""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")


def main():
    
    # Configure environment variables
    configure()

    # Call the API and generate response
    generate()

    print(50 * "=")
    print("Demo completed successfully.")

if __name__ == "__main__":
    main()