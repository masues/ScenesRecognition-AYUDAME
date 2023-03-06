""" Test script to measure feature extraction performance over time with 1000 frames """

import time
import cv2 as cv
from prepareFiles import prepareFiles

# Path of RGB images divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_rgb"

# Extracts features on the first n classes only
num_classes = 1

files_paths = prepareFiles(pcd_dir,num_classes)

descriptor = cv.SIFT_create()

init = time.process_time()
for filename in files_paths:
    img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    descriptor.detectAndCompute(img, None)
end = time.process_time()

print(f"{len(files_paths)} frames processed")
print(f"The feature extraction took {end - init}s")
