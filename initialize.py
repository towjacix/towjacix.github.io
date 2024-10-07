# program to capture single image from webcam in python

# importing OpenCV
import cv2

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

img = cv2.imread("temp.png")

# Greyscale converting
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load the CascadeClassifier
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

face = face_classifier.detectMultiScale(
    gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(40, 40)
)

# Face recognition 
# Face counting
face_count = 0
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)
    face_count += 1 


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imwrite("pic.png", img_rgb)
print(face_count, "/ 44")
