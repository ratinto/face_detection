# Face Recognition with Song Playback

This project is a real-time face recognition system using OpenCV and the `face_recognition` library. When a known face is detected via webcam, a song is played for that person (only once per session). The system is designed for quick prototyping and demonstration purposes.

## Features
- Detects faces from webcam video stream
- Recognizes known faces using pre-trained encodings
- Plays a song for each recognized person (once per session)
- Displays bounding boxes and names on the video feed

## Folder Structure
```
face_recognition/
├── capture.py           # (Optional) Script to capture images for training
├── encodings.pickle     # Pickle file containing face encodings and names
├── face_recog.py        # Main face recognition script
├── song.mp3             # Song to play when a face is recognized
├── train.py             # Script to train and generate encodings.pickle
└── dataset/
    └── <person_name>/   # Folder for each person, containing their images
        └── image files  # e.g., ritesh_0.jpg, ritesh_1.jpg, ...
```

## Setup Instructions

### 1. Install Dependencies
Make sure you have Python 3.7+ installed. Install required packages:

```bash
pip install opencv-python face_recognition playsound
```

### 2. Prepare Dataset
- Create a folder named `dataset` in the project directory.
- Inside `dataset`, create a subfolder for each person (e.g., `ritesh`).
- Add multiple face images of each person in their respective folder.

Example:
```
dataset/
└── ritesh/
    ├── ritesh_0.jpg
    ├── ritesh_1.jpg
    └── ...
```

### 3. Train Face Encodings
Run the training script to generate `encodings.pickle`:

```bash
python train.py
```

This will process all images in `dataset/` and save the encodings and names in `encodings.pickle`.

### 4. Add Song
Place your desired song file as `song.mp3` in the project directory. You can change the filename in `face_recog.py` if needed.

### 5. Run Face Recognition
Start the recognition script:

```bash
python face_recog.py
```

- The webcam window will open.
- When a known face is detected, the song will play (once per person per session).
- Press `q` to quit.

## How It Works
- Loads face encodings and names from `encodings.pickle`.
- Captures video from webcam.
- Detects faces and computes encodings for each frame.
- Compares detected encodings with known encodings.
- If a match is found, displays the name and plays the song (if not already played for that person).
- Draws bounding boxes and names on the video feed.

## Customization
- **Change Song:** Replace `song.mp3` with your own audio file.
- **Add More People:** Add more folders/images to `dataset/` and rerun `train.py`.
- **Recognition Model:** The script uses the HOG model for face detection. For better accuracy (but slower), change `model="hog"` to `model="cnn"` in `face_recog.py`.

## Troubleshooting
- If you get errors about missing packages, ensure all dependencies are installed.
- If the webcam does not open, check your camera permissions.
- If faces are not recognized, ensure images are clear and well-lit.

## Requirements
- Python 3.7+
- OpenCV
- face_recognition
- playsound

## Credits
- [face_recognition](https://github.com/ageitgey/face_recognition)
- OpenCV

## License
This project is for educational purposes.
