import cv2
import os

username = input("Enter your username: ")

# Create faces folder if not exists
if not os.path.exists("faces"):
    os.makedirs("faces")

cap = cv2.VideoCapture(0)

print("Press S to capture your face")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Face Registration", frame)
    key = cv2.waitKey(1)

    if key == ord('s'):
        file_path = f"faces/{username}.jpg"
        cv2.imwrite(file_path, frame)
        print("Face saved successfully!")
        break

cap.release()
cv2.destroyAllWindows()
