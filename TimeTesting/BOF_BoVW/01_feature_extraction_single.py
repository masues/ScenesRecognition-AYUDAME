""" Test script to measure feature extraction performance over time with a single frame """

import numpy as np
import time
from extractBofs import extractBofs
from prepareFiles import prepareFiles

# Path of point clouds divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_pcd"

files_paths = prepareFiles(pcd_dir,1)
filename = files_paths[568] # Fixed frame

time_frames = np.zeros(10) # Number of iterations


for i in range(len(time_frames)):
    init = time.process_time()
    pcd_bofs = extractBofs(filename,axis=2,method=2,layers=3)
    end = time.process_time()
    time_frames[i] = end - init
    if len(pcd_bofs) == 0:
        raise ValueError("The selected frame is empty")

for i in range(len(time_frames)):
    print(f"The iteration {i} took {time_frames[i]}")

print(f"The max value was: {np.max(time_frames)}")
print(f"The min value was: {np.min(time_frames)}")
print(f"The average was:   {np.mean(time_frames)}")
