
import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Initialize the webcam
cap = cv2.VideoCapture(1)

# Previous position of the hand (used to detect if the hand is moving)
prev_x, prev_y = None, None

def is_fist(hand_landmarks):
    """Check if the hand is in a fist position by examining the finger positions."""
    # Check if the fingertips (index 4, 8, 12, 16, 20) are below the knuckles (index 3, 7, 11, 15, 19)
    fingers_closed = [
        hand_landmarks.landmark[4].y < hand_landmarks.landmark[3].y,  # Thumb
        hand_landmarks.landmark[8].y < hand_landmarks.landmark[7].y,  # Index
        hand_landmarks.landmark[12].y < hand_landmarks.landmark[11].y,  # Middle
        hand_landmarks.landmark[16].y < hand_landmarks.landmark[15].y,  # Ring
        hand_landmarks.landmark[20].y < hand_landmarks.landmark[19].y,  # Pinky
    ]
    return all(fingers_closed)

while True:
    # Capture each frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB (MediaPipe works with RGB images)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Check if the hand is in a fist
            if is_fist(hand_landmarks):
                # Press Enter when a fist is detected
                pyautogui.press('enter')
                time.sleep(0.5)  # To prevent multiple presses during the same fist detection
                continue

            # Get the position of the index finger tip (landmark 8)
            index_finger_tip = hand_landmarks.landmark[8]

            # Get the coordinates of the index finger tip
            h, w, _ = frame.shape
            x = int(index_finger_tip.x * w)
            y = int(index_finger_tip.y * h)

            # Move the mouse cursor only if the hand is moving
            if prev_x is not None and prev_y is not None:
                # Check if the hand has moved (based on the difference in coordinates)
                if abs(prev_x - x) > 5 or abs(prev_y - y) > 5:
                    pyautogui.moveTo(x, y)

            # Update previous coordinates
            prev_x, prev_y = x, y

            # Draw landmarks on the hand for visualization
            for landmark in hand_landmarks.landmark:
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)

    # Display the webcam feed with hand landmarks
    cv2.imshow("Hand Tracking", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
