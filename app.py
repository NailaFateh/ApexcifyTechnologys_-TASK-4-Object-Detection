import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

# 0 = webcam
# OR replace with video file path: "video.mp4"
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(" Error: Cannot open camera or video")
    exit()

print(" Press 'q' to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print(" Failed to grab frame")
        break

    # Run detection + tracking
    results = model.track(frame, persist=True)
    annotated_frame = results[0].plot()

    cv2.imshow("Object Detection & Tracking", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()