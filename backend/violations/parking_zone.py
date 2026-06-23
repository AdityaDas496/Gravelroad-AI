import cv2
import numpy as np

LEFT_ZONE = np.array([[0,252], [280,144], [337,143], [0,423]])

RIGHT_ZONE = np.array([[578,155], [685,170], [768,246], [768, 413], [707,432]])

def inside_parking_zone(x, y):

    left = cv2.pointPolygonTest(
        LEFT_ZONE.astype(np.float32),
        (float(x), float(y)),
        False
    )

    right = cv2.pointPolygonTest(
        RIGHT_ZONE.astype(np.float32),
        (float(x), float(y)),
        False
    )

    return left >= 0 or right >= 0