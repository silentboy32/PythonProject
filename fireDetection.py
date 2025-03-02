
import cv2
import numpy as np
from playsound import playsound

# Path to the alarm sound file
ALARM_SOUND = "fire_alarm.mp3"

def detect_fire():
    # Open the webcam (use video file path for pre-recorded video)
    cap = cv2.VideoCapture(1)

    fire_detected = False

    print("Fire detection system active...")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame. Exiting...")
            break

        # Resize the frame for better performance
        frame = cv2.resize(frame, (640, 480))

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the range for fire colors (orange-red)
        lower_bound = np.array([0, 50, 50])  # Lower bound of fire color
        upper_bound = np.array([35, 255, 255])  # Upper bound of fire color

        # Create a mask for detecting fire
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Apply the mask to the original frame
        fire = cv2.bitwise_and(frame, frame, mask=mask)

        # Count non-zero pixels in the mask to determine fire presence
        non_zero_pixels = cv2.countNonZero(mask)

        # Threshold for fire detection
        if non_zero_pixels > 5000:  # Adjust this value based on environment
            if not fire_detected:
                print("Fire detected!")
                fire_detected = True
                playsound(ALARM_SOUND, block=False)
        else:
            fire_detected = False

        # Show the original frame and the fire mask
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Fire Detection", fire)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_fire()
