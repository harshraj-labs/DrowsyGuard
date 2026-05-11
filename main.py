import cv2
from detector import DrowsinessDetector
from alert import play_alarm, stop_alarm
from utils import draw_ui, draw_eye_dots

ALARM_PATH = "assets/alarm.wav"

def main():
    cap = cv2.VideoCapture(0)
    detector = DrowsinessDetector()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame, is_drowsy, avg_ear = detector.process(frame)
        
        if is_drowsy:
            play_alarm(ALARM_PATH)
        else:
            stop_alarm()
        
        draw_ui(frame, avg_ear, is_drowsy)
        
        cv2.imshow("DrowsyGuard", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()