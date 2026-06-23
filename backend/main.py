import cv2
from detector import detect
from violations.wrong_side import check_wrong_side
from violations.illegal_parking import get_parking_status
from violations.parking_zone import LEFT_ZONE, RIGHT_ZONE
from road_zone import inside_road
from road_zone import BACK_ROAD, FRONT_ROAD
from preprocessing import preprocess
from evidence.evidence_generator import save_evidence
from evidence.violation_logger import log_violation

VIDEO_PATH = "../videos/test2.mp4"

cap = cv2.VideoCapture(VIDEO_PATH)

saved_violations = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = preprocess(frame)
    detections = detect(frame)
    print("IDs:", detections.boxes.id)
    print("Conf:", detections.boxes.conf)

    if detections.boxes.id is not None:
        boxes = detections.boxes.xyxy.cpu().numpy()
        ids = detections.boxes.id.cpu().numpy()
        confs = detections.boxes.conf.cpu().numpy()
        for box, track_id, conf in zip(boxes, ids, confs):
            x1, y1, x2, y2 = map(int, box)
            width = x2 - x1
            height = y2 - y1
            center_x = (x1 + x2) // 2
            center_y = y2 - 20
            if not inside_road(center_x, center_y):
                continue
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
            parking_status = get_parking_status(int(track_id), center_x, center_y)
            if conf < 0.45:
                continue
            if width < 50 or height < 50:
                continue
            ## is_wrong_side = check_wrong_side(int(track_id), center_x, center_y)
            is_wrong_side = False
            if parking_status == "red":
                color = (0, 0, 255)
                label = f"ILLEGAL PARKING {int(track_id)}"
                if int(track_id) not in saved_violations:
                    evidence_path = save_evidence(frame, int(track_id), "illegal_parking")
                    log_violation(int(track_id), "illegal_parking", evidence_path)
                    saved_violations.add(int(track_id))
            elif parking_status == "yellow":
                color = (0, 255, 255)
                label = f"PARKING SUSPECT {int(track_id)}"
            elif is_wrong_side:
                color = (255, 0, 255)
                label = f"WRONG SIDE {int(track_id)}"
            else:
                color = (0, 255, 0)
                label = f"ID {int(track_id)}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

    cv2.polylines(frame, [BACK_ROAD], True, (255,255,0), 2)
    cv2.polylines(frame, [FRONT_ROAD], True, (255,255,0), 2)
    cv2.polylines(frame, [LEFT_ZONE], True, (255,0,0), 2)
    cv2.polylines(frame, [RIGHT_ZONE], True, (255,0,0), 2)
    cv2.imshow("Traffic Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #No video detected
        break
cap.release()
cv2.destroyAllWindows()