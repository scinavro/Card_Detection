import cv2
import torch
import numpy as np
import math
import CNN_Model as cnn

def load_checkpoint(checkpoint):
    print("Loading checkpoint")
    loaded_model.load_state_dict(checkpoint['state_dict'])

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if 5000>area>1000:
            # print(area)
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
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
                torchMahjong = torch.from_numpy(imgMahjong)
                torchMahjong = torchMahjong.unsqueeze(0)
                torchMahjong = torchMahjong.unsqueeze(1)
                torchMahjong = torchMahjong.float()

                MahjongType = torch.argmax(loaded_model(torchMahjong))
                print(MahjongType)

                if MahjongType.item() == 0: objectType = "Sak_5"
                elif MahjongType.item() == 1: objectType = "Man_7"
                elif MahjongType.item() == 2: objectType = "Man_7"
                elif MahjongType.item() == 3: objectType = "Choong"
                elif MahjongType.item() == 4: objectType = "Choong"

                cv2.imshow("Mahjong Image", imgMahjong)
                cv2.waitKey(1)

            else: objectType = " "

            cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 255), 2)


loaded_model = cnn.model
load_checkpoint(torch.load("my_checkpoint.pth.tar"))

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 780)
cap.set(10, 100)

while True:
    success, img = cap.read()
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