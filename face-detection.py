import google.generativeai as genai
import os
from dotenv import load_dotenv
import time
import cv2
from json import dump
from os import system

# initialize the camera
cam_port = 0
cam = cv2.VideoCapture(cam_port)

# reading the input using the camera
result, image = cam.read()

# If image will detected without any error,
# show result
if result:

	# showing result, it take frame name and image
	# output
	# cv2.imshow("GeeksForGeeks", image)
	# saving image in local storage
	cv2.imwrite("temp.png", image)

	# If keyboard interrupt occurs, destroy image
	# windows
	cv2.waitKey(0)
	# cv2.destroyWindow("test")

# If captured image is corrupted, moving to else part
else:
	print("No image detected. Please! try again")


load_dotenv()
face_image = genai.upload_file("temp.jpg")
print(f"{face_image=}")

API_KEY = os.getenv("API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
result = model.generate_content(
        [face_image, "\n\n", "Can you tell me how many people are there in the photos? Please tell me the number without talking further."]
    )

print(f"{result.text=}")
face_count = result.text

# Dict json data
data = {
        "name": "Số học sinh có mặt",
        "numbers": face_count,
        "class": "12A3",
}

# Export to json
with open("students.json", "w") as f:
    dump(data, f, indent=4)

