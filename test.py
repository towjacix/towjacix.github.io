import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
face_image = genai.upload_file("temp.jpg")
print(f"{face_image=}")

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-002")
result = model.generate_content(
        [face_image, "\n\n", "Can you tell me how many people are there in the photos? Please tell me the number without talking further."]
    )

print(f"{result.text=}")

