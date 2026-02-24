import cv2
import numpy as np
import os

username = input("Enter your username: ")
stored_path = f"faces/{username}.jpg"

if not os.path.exists(stored_path):
    print("No registered face found.")
    exit()

# Capture live image
cap = cv2.VideoCapture(0)
print("Press S to verify your face")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Face Verification", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        cv2.imwrite("live.jpg", frame)
        break

cap.release()
cv2.destroyAllWindows()

# Load images
img1 = cv2.imread(stored_path, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("live.jpg", cv2.IMREAD_GRAYSCALE)

# Resize to same size
img1 = cv2.resize(img1, (200, 200))
img2 = cv2.resize(img2, (200, 200))

# Calculate similarity
difference = cv2.absdiff(img1, img2)
score = np.sum(difference)

print("Difference score:", score)

if score < 3000000:
    print("Identity Verified")
else:
    print("Verification Failed")
