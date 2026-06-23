from ultralytics import YOLO

model = YOLO("yolov8s.pt")

CONF_THRESHOLD = 0.25

def detect(frame):

    results = model.track(frame, persist=True, tracker="botsort.yaml", conf=CONF_THRESHOLD, imgsz=960, verbose=False)

    return results[0]