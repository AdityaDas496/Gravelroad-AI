import cv2
import numpy as np

BACK_ROAD = np.array([
    [243,430],
    [453,114],
    [341,113],
    [1,288],
    [1,430]
], dtype=np.int32)

FRONT_ROAD = np.array([
    [475,115], # p2
    [595,111],
    [768,313],
    [768,432],
    [305,432]
], dtype=np.int32)

def inside_road(x, y):

    back = cv2.pointPolygonTest(
        BACK_ROAD.astype(np.float32),
        (float(x), float(y)),
        False
    )

    front = cv2.pointPolygonTest(
        FRONT_ROAD.astype(np.float32),
        (float(x), float(y)),
        False
    )

    return back >= 0 or front >= 0