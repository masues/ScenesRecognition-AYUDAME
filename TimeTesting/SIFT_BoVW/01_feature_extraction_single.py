""" Test script to measure feature extraction performance over time with a single frame """

import numpy as np
import time
import cv2 as cv
from prepareFiles import prepareFiles

# Path of RGB images divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_rgb"

files_paths = prepareFiles(pcd_dir,1)
filename = files_paths[568] # Fixed frame

time_frames = np.zeros(10) # Number of iterations

descriptor = cv.SIFT_create()

for i in range(len(time_frames)):
    init = time.process_time()
    img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    descriptor.detectAndCompute(img, None)
    end = time.process_time()
    time_frames[i] = end - init

for i in range(len(time_frames)):
    print(f"The iteration {i} took {time_frames[i]}")

print(f"The max value was: {np.max(time_frames)}")
print(f"The min value was: {np.min(time_frames)}")
print(f"The average was:   {np.mean(time_frames)}")
