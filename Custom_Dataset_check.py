import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from Custom_Dataset import path, training_data

np.save(os.path.join(path, 'features'), np.array(training_data))

saved = np.load(os.path.join(path, 'features.npy'))

plt.imshow(saved[0])
pit.imshow(np.array(training_data[0]))