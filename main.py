import cv2
from detector import DrowsinessDetector
from alert import play_alarm, stop_alarm
from utils import draw_ui, draw_eye_dots
import config


def main():
    cap= cv2.VideoCapture(0)
    #cap = cv2.VideoCapture("assets/demo_input.mp4") #use for demo video check instead of camera
    detector = DrowsinessDetector()  # pulls all defaults from config.py

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame, is_drowsy, avg_ear, left_pts, right_pts = detector.process(frame)

        if is_drowsy:
            play_alarm(config.ALARM_PATH)
        else:
            stop_alarm()

        draw_ui(frame, avg_ear, is_drowsy)
        draw_eye_dots(frame, left_pts)
        draw_eye_dots(frame, right_pts)

        cv2.imshow("DrowsyGuard", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()