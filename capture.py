import cv2
import os

name = "ritesh"
save_dir = f"dataset/{name}"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    cv2.imshow("Capture - Press SPACE to Save, Q to Quit", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord(' '):
        cv2.imwrite(f"{save_dir}/{name}_{count}.jpg", frame)
        print(f"Saved: {name}_{count}.jpg")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
