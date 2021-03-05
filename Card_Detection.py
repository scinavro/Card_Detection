import cv2
import numpy as np
import math

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>2000:
            print(area)
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            print(approx[0])
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 4:
                objectType = "Card"

                width, height = 124, 176
                if math.dist(approx[0][0], approx[1][0]) > math.dist(approx[0][0], approx[3][0]):
                    pts1 = np.float32([approx[0], approx[1], approx[2], approx[3]])
                else:
                    pts1 = np.float32([approx[1], approx[2], approx[3], approx[0]])
                pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])
                matrix = cv2.getPerspectiveTransform(pts1, pts2)

                imgCard = cv2.warpPerspective(img, matrix, (width, height))
                imgNum = imgCard[0:30, 0:20]
                imgSym = imgCard[30:50, 0:20]


                cv2.imshow("Card Image", imgCard)
                cv2.imshow("Num Image", imgNum)
                cv2.imshow("Symbol Image", imgSym)
                cv2.waitKey(500)

            else: objectType = "Not Card"

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 780)
cap.set(10, 100)

while True:
    success, img = cap.read()
    # path = 'Resources/card_L.jpg'
    # img = cv2.imread(path)
    imgContour = img.copy()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)

    getContours(imgCanny)

    # cv2.imshow("Original", img)
    # cv2.imshow("Gray", imgGray)
    # cv2.imshow("Blur", imgBlur)
    # cv2.imshow("Video", img)
    # cv2.imshow("Canny", imgCanny)
    cv2.imshow("Contour", imgContour)
    cv2.waitKey(1)