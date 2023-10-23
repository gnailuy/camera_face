import cv2
import face_recognition

from console_helper import print_error
from play_alert import play_alert


quit_hint = "Press 'Esc' or 'q' to quit the program."
start_hint = "Face detection paused, press 'R' or 'r' to start face detection."
pause_hint = "Face detection started, press 'G' or 'g' to pause face detection."

alert = play_alert()


def detect_faces(frame):
    # Detect faces in a frame
    color_red = (0, 0, 200)
    face_locations = face_recognition.face_locations(frame)

    # Draw rectangles on the faces detected
    for location in face_locations:
        top, right, bottom, left = location
        cv2.rectangle(frame, (left, top), (right, bottom),
                      color_red, thickness=2)

    # Play the alert if there is any face detected
    # We do not stop the alert if there is no face detected as the alert will stop automatically
    if len(face_locations) > 0:
        alert.start_alert()


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

        if paused:
            # Stop any alert if the face detection is paused
            alert.stop_alert()
        else:
            # Detect faces and draw a rectangle on each face
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

    # Stop the alert in case it is still playing
    alert.stop_alert()

    # Release the capture and destroy all OpenCV windows
    capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
