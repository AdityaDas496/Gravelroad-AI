import cv2
import easyocr

reader = easyocr.Reader(['en'])

image = cv2.imread("../test_images/car.jpg")

results = reader.readtext(image)

for result in results:
    bbox, text, confidence = result
    if len(text) < 6:
        continue
    print(text)
    print("Plate Text:", text)
    print("Confidence:", confidence)
    x1 = int(bbox[0][0])
    y1 = int(bbox[0][1])
    x2 = int(bbox[2][0])
    y2 = int(bbox[2][1])
    cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)
    cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
cv2.imwrite("ocr_result.jpg", image)
print("Saved OCR result as ocr_result.jpg")