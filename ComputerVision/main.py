from turtle import width
import cv2
import numpy as np

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)
# cap.set(4, 480)
# cap.set(10, 100)

# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# kernel = np.ones((5, 5), np.uint8)

img = cv2.imread("imgs/logo.png")

width, height = 500, 500

pts1 = np.float32([[100, 200], [300, 188], [150, 480], [350, 450]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Output Image", imgOutput)

# imgCropped = img[0:200, 200:400]
# imgResize = cv2.resize(img, (300, 300))
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)
# imgCanny = cv2.Canny(img, 100, 100)
# imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
# imgEroded = cv2.erode(imgDialation, kernel, iterations=1)


# cv2.imshow("Cropped Img", imgCropped)
# cv2.imshow("Resized Img", imgResize)
# cv2.imshow("Gray Img", imgGray)
# cv2.imshow("Blur Img", imgBlur)
# cv2.imshow("Canny Img", imgCanny)
# cv2.imshow("Dialation  Img", imgDialation)
# cv2.imshow("Eroded  Img", imgEroded)


# crtimg = np.zeros((512, 512, 3), np.uint8)
# # crtimg[:300] = 255, 0, 0   #BGR

# cv2.circle(crtimg, (250, 250), 99, (255, 0, 255), 5)
# cv2.line(crtimg, (0, 0), (crtimg.shape[1], crtimg.shape[0]), (0, 255, 255), 3)

# cv2.rectangle(crtimg, (0, 0), (250, 250), (0, 255, 0), cv2.FILLED)
# cv2.rectangle(crtimg, (0, 0), (350, 350), (255, 255, 0), 2)

# cv2.putText(crtimg, " OpenCV ", (25, 50),
#             cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 150, 0), 2)

# cv2.imshow("Image", crtimg)


cv2.waitKey(0)
