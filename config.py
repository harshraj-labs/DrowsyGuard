# Drowsiness Detection 
EAR_THRESHOLD   = 0.25   # Eye Aspect Ratio below which eye is "closed"
CONSEC_FRAMES   = 20     # Consecutive frames needed to trigger alarm

# MediaPipe 
MODEL_PATH                    = "models/face_landmarker.task"
MIN_FACE_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE       = 0.7

# Assets 
ALARM_PATH = "assets/alarm.wav"