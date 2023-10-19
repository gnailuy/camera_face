import cv2
import face_recognition
import sys


quit_hint = "Press 'Esc' or 'q' to quit the program."
start_hint = "Face detection paused, press 'R' or 'r' to start face detection."
pause_hint = "Face detection started, press 'G' or 'g' to pause face detection."

# Print error message to stderr
def print_error(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Detect faces in a frame
def detect_faces(frame):
    color_red = (0, 0, 200)
    face_locations = face_recognition.face_locations(frame)

    # Draw rectangles on the faces detected
    for location in face_locations:
        top, right, bottom, left = location
        cv2.rectangle(frame, (left, top), (right, bottom), color_red, thickness=2)

def main():
    # Open the first camera
    capture = cv2.VideoCapture(0)

    print(start_hint, quit_hint)
    paused = True

    while True:
        # Read a frame from the camera
        ok, frame = capture.read()
        if not ok:
            print_error('Error: Cannot read frame from the video source.')
            break

        # Detect faces and draw a rectangle on each face
        if not paused:
            detect_faces(frame)

        # Show the image frame
        cv2.imshow('Frame', frame)

        # Wait for 1 millisecond or until any key is pressed
        key = cv2.waitKey(1)
        if key == 27 or key == ord('q'):
            # Quit the capture on Esc(27) or the 'q' key
            break
        elif paused and (key == ord('R') or key == ord('r')):
            print(pause_hint, quit_hint)
            paused = False
        elif not paused and (key == ord('G') or key == ord('g')):
            print(start_hint, quit_hint)
            paused = True

        # If the window is closed by the user, quit the program
        if cv2.getWindowProperty('Frame', cv2.WND_PROP_VISIBLE) < 1:
            break

    # Release the capture and destroy all OpenCV windows
    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

