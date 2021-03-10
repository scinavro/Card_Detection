import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

path = './sak_five'

training_data = []
for img in os.listdir(path):
    pic = cv2.imread(os.path.join(path, img))
    training_data.append([pic])
