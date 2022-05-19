import cv2
import numpy as np

img = cv2.imread("Resources/330px-Lenna.png")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7),0)
imgCanny = cv2.Canny(img, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel=kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel=kernel, iterations=1)

cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dialation", imgDialation)
cv2. imshow("Eroded", imgEroded)
cv2.waitKey(0)