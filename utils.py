import cv2

def draw_eye_dots(frame, pts, color=(0,255,0)):
    for pt in pts:
        cv2.circle(frame,pt,2,color,-1)
    
def draw_ui(frame, ear, is_drowsy):
    color = (0, 0, 255) if is_drowsy else (0, 255, 0)
    
    cv2.putText(frame, f"EAR: {ear:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    if is_drowsy:
        cv2.putText(frame, "DROWSINESS DETECTED!", (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)