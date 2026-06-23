import cv2

def preprocess(frame): #Increase za brightness, but restore the colors of the image
    lab = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2LAB
    )
    l, a, b = cv2.split(lab)

    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8,8)
    )

    l = clahe.apply(l)

    enhanced = cv2.merge([l, a, b])

    return cv2.cvtColor(
        enhanced,
        cv2.COLOR_LAB2BGR
    )