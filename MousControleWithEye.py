
import cv2
import dlib
import pyautogui

# Initialize face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")  # Download from dlib's website

# Function to calculate the midpoint
def midpoint(p1, p2):
    return (p1.x + p2.x) // 2, (p1.y + p2.y) // 2

# Open the webcam
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    if not ret:
        break

    # Convert to grayscale for better detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = detector(gray)

    for face in faces:
        # Get the landmarks for the face
        landmarks = predictor(gray, face)

        # Get points for left and right eye
        left_eye = [landmarks.part(i) for i in range(36, 42)]
        right_eye = [landmarks.part(i) for i in range(42, 48)]

        # Calculate the midpoint of each eye
        left_mid = midpoint(left_eye[0], left_eye[3])
        right_mid = midpoint(right_eye[0], right_eye[3])

        # Mark the eyes
        for point in left_eye + right_eye:
            cv2.circle(frame, (point.x, point.y), 2, (0, 255, 0), -1)

        # Control the cursor (this is just a demonstration of mapping)
        screen_width, screen_height = pyautogui.size()
        frame_height, frame_width = frame.shape[:2]

        # Normalize gaze point and move cursor
        cursor_x = int((left_mid[0] / frame_width) * screen_width)
        cursor_y = int((left_mid[1] / frame_height) * screen_height)
        pyautogui.moveTo(cursor_x, cursor_y)

    # Display the frame
    cv2.imshow("Eye Controlled Mouse", frame)

    # Break the loop on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()