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

init_cpu = time.process_time()
init_r = time.perf_counter()
for filename in files_paths:
    img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    descriptor.detectAndCompute(img, None)
end_cpu = time.process_time()
end_r = time.perf_counter()

print(f"{len(files_paths)} frames processed")
print(f"The feature extraction took {end_cpu - init_cpu:.6f}[s] CPU, {end_r - init_r:.6f}[s] real")
