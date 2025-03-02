import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error ")

else:
    print("Webcam")


cap.release()


