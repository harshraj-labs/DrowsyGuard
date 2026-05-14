import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import config

LEFT_EYE  = [362, 385, 387, 263, 373, 380]
RIGHT_EYE = [33, 160, 158, 133, 153, 144]


def get_ear(landmarks, eye_indices, frame_w, frame_h):
    pts = []
    for idx in eye_indices:
        lm = landmarks[idx]
        pts.append((int(lm.x * frame_w), int(lm.y * frame_h)))

    v1  = np.linalg.norm(np.array(pts[1]) - np.array(pts[5]))
    v2  = np.linalg.norm(np.array(pts[2]) - np.array(pts[4]))
    h   = np.linalg.norm(np.array(pts[0]) - np.array(pts[3]))
    ear = (v1 + v2) / (2.0 * h)
    return ear, pts


class DrowsinessDetector:
    def __init__(
        self,
        ear_threshold=config.EAR_THRESHOLD,
        consec_frames=config.CONSEC_FRAMES,
    ):
        self.EAR_THRESHOLD = ear_threshold
        self.CONSEC_FRAMES = consec_frames
        self.frame_counter = 0
        self.alarm_on      = False

        base_options = python.BaseOptions(model_asset_path=config.MODEL_PATH)
        options = vision.FaceLandmarkerOptions(
            base_options=base_options,
            num_faces=1,
            min_face_detection_confidence=config.MIN_FACE_DETECTION_CONFIDENCE,
            min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE,
        )
        self.detector = vision.FaceLandmarker.create_from_options(options)

    def process(self, frame):
        h, w = frame.shape[:2]
        rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
        result   = self.detector.detect(mp_image)

        is_drowsy  = False
        avg_ear    = 0.0
        left_pts   = []
        right_pts  = []

        if result.face_landmarks:
            landmarks = result.face_landmarks[0]
            left_ear,  left_pts  = get_ear(landmarks, LEFT_EYE,  w, h)
            right_ear, right_pts = get_ear(landmarks, RIGHT_EYE, w, h)
            avg_ear = (left_ear + right_ear) / 2.0

            if avg_ear < self.EAR_THRESHOLD:
                self.frame_counter += 1
                if self.frame_counter >= self.CONSEC_FRAMES:
                    is_drowsy     = True
                    self.alarm_on = True
            else:
                self.frame_counter = 0
                self.alarm_on      = False


        return frame, is_drowsy, avg_ear, left_pts, right_pts