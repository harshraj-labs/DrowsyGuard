# DrowsyGuard 🚗

Real-time driver drowsiness detection using Python, OpenCV, and MediaPipe.
Monitors eye aspect ratio (EAR) in real-time and triggers an alarm when 
drowsiness is detected.

## Demo
![Demo GIF](assets/demo.gif)

## Features
- Real-time eye tracking using MediaPipe Face Landmarker
- Eye Aspect Ratio (EAR) algorithm for drowsiness detection
- Instant audio alarm with automatic stop when driver is alert
- Live EAR value display on screen
- Lightweight — runs on low-spec hardware

## Tech Stack
- Python 3.13
- OpenCV
- MediaPipe
- Pygame
- NumPy

## Installation

1. Clone the repository
```bash
git clone https://github.com/harshraj-labs/DrowsyGuard.git
cd DrowsyGuard
```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Download the MediaPipe face landmark model
```bash
mkdir models
```
Then download [face_landmarker.task](https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task) and place it inside the `models/` folder.

## Usage

```bash
python main.py
```
- App opens your webcam automatically
- Keep your face visible to the camera
- Close your eyes for ~1 second → alarm triggers
- Open your eyes → alarm stops
- Press `Q` to quit

## Project Structure
DrowsyGuard/
├── assets/
│   └── alarm.wav        # Alert sound
├── models/
│   └── face_landmarker.task  # MediaPipe model
├── main.py              # Entry point
├── detector.py          # EAR logic + MediaPipe
├── alert.py             # Alarm system
├── utils.py             # Visual overlay
└── requirements.txt

## How It Works
1. Webcam captures live video feed
2. MediaPipe detects 468 facial landmarks per frame
3. Eye Aspect Ratio (EAR) calculated from 6 points around each eye
4. If EAR drops below 0.25 for 20 consecutive frames → drowsy
5. Alarm triggers instantly, stops when driver is alert again

## License
MIT License — see [LICENSE](LICENSE) for details.