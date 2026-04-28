import cv2
import os
import time

def collect_gesture_images(gesture_name, num_images=100):
    output_folder = f"dataset/{gesture_name}"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(0)
    count = 0

    print(f"Prepare gesture: {gesture_name}")
    print("Recording will start in 3 seconds...")
    time.sleep(3)

    while count < num_images:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        cv2.imshow('Capturing Data', frame)

        file_path = os.path.join(output_folder, f"{gesture_name}_{count}.jpg")
        cv2.imwrite(file_path, frame)
        
        count += 1
        
        if cv2.waitKey(150) & 0xFF == ord('q'):
            break

    print(f"Done! Saved {count} photos to folder {output_folder}")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    collect_gesture_images("6o", 250)