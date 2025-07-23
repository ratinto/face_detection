import face_recognition, os, pickle


encodings, names = [], []


for person in os.listdir("dataset"):
   for img in os.listdir(f"dataset/{person}"):
       img_path = f"dataset/{person}/{img}"
       image = face_recognition.load_image_file(img_path)
       boxes = face_recognition.face_locations(image, model="hog")
       for enc in face_recognition.face_encodings(image, boxes):
           encodings.append(enc)
           names.append(person)


data = {"encodings": encodings, "names": names}
with open("encodings.pickle", "wb") as f:
   pickle.dump(data, f)


print(f"Trained on {len(encodings)} face encodings.")
