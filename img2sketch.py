import cv2
img = cv2.imread('ronaldo.jpg.jpeg')
img=cv2.resize(img,(720, 680))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inverted = 255 - gray
blurred = cv2.GaussianBlur(inverted, (21, 21), 0)
inverted_blur = 255 - blurred
sketch = cv2.divide(gray, inverted_blur, scale=256.0)
cv2.imshow("Sketch", sketch)
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
