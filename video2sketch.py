import cv2
cap = cv2.VideoCapture('anime.mp4')

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (720, 520))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inverted = 255 - gray
    blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
    inverted_blur = 255 - blurred
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    cv2.imshow("Sketch", sketch)
    cv2.imshow("frame", frame)
    cv2.waitKey(1000)
    # cv2.imwrite("sketch.jpg", sketch)

cv2.caprelease()
cv2.destroyAllWindows()

