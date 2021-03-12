import cv2
import numpy as np
import math
import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader


def showMahjong(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>1000:
            # print(area)
            cv2.drawContours(frame, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            # print(len(approx))
            # print(approx[0])
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 4:
                objectType = "Mahjong"

                width, height = 200, 200
                if math.dist(approx[0][0], approx[1][0]) > math.dist(approx[0][0], approx[3][0]):
                    pts1 = np.float32([approx[0], approx[1], approx[2], approx[3]])
                else:
                    pts1 = np.float32([approx[1], approx[2], approx[3], approx[0]])
                pts2 = np.float32([[0, 0], [0, height], [width, height], [width, 0]])
                matrix = cv2.getPerspectiveTransform(pts1, pts2)

                imgMahjong = cv2.warpPerspective(img, matrix, (width, height))
                return(imgMahjong)

            else:
                objectType = "Not Mahjong"



            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 1)



cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 780)
cap.set(10, 100)

img_counter = 1

while True:
    success, frame = cap.read()

    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)

    imgTrain = showMahjong(imgCanny)
    cv2.imshow("Contour", frame)
    try:
        cv2.imshow("Mahjong Image", imgTrain)
    except cv2.error:
        pass


    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed

        img_name = "Choong_r_{}.png".format(img_counter)
        try:
            cv2.imwrite(img_name, imgTrain)
            print("{} written!".format(img_name))
            img_counter += 1
        except cv2.error:
            pass




