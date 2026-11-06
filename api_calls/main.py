import os
from google import genai

Client = genai.client()
MODEL = os.environ.get(
    "GEMINI_API_KEY",
    "gemini-3.8-flash"
    )
response = Client.models.generate_content(
    model=MODEL,
    contents="What is s neura link"
)

with open("api.txt", "a") as file:
    content = file.write(response.text)
    print("successfully responded into the api file")