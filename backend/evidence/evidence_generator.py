import cv2
import os
from datetime import datetime

os.makedirs("evidence", exist_ok=True)

def save_evidence(frame, track_id, violation_type):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = (f"evidence/{violation_type}_{track_id}_{timestamp}.jpg")

    cv2.imwrite(filename, frame)

    return filename