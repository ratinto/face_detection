import cv2
import pickle
import face_recognition
from playsound import playsound
import os

with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

cap = cv2.VideoCapture(0)
already_played = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb, model="hog")
    encs = face_recognition.face_encodings(rgb, boxes)

    for box, enc in zip(boxes, encs):
        matches = face_recognition.compare_faces(data["encodings"], enc)
        name = "Unknown"
        if True in matches:
            idxs = [i for i, m in enumerate(matches) if m]
            name = max((data["names"][i] for i in idxs), key=(lambda n: data["names"].count(n)))

            # ✅ Play song only once per person per session
            if name not in already_played:
                already_played.add(name)
                print(f"🎵 Playing song for {name}")
                playsound("song.mp3")  # Replace with your own song

        top, right, bottom, left = box
        cv2.rectangle(frame, (left, top), (right, bottom), (0,255,0), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
