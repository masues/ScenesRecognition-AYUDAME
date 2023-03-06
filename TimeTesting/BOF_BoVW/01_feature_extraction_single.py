""" Test script to measure feature extraction performance over time with a single frame """

import numpy as np
import time
from extractBofs import extractBofs
from prepareFiles import prepareFiles

# Path of point clouds divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_pcd"

files_paths = prepareFiles(pcd_dir, 1)
filename = files_paths[568]  # Fixed frame

time_frames_cpu = np.zeros(10)  # Number of iterations
time_frames_r = time_frames_cpu.copy()

for i in range(len(time_frames_cpu)):
    init_cpu = time.process_time()
    init_r = time.perf_counter()
    pcd_bofs = extractBofs(filename, axis=2, method=2, layers=3)
    end_cpu = time.process_time()
    end_r = time.perf_counter()
    time_frames_cpu[i] = end_cpu - init_cpu  # CPU time
    time_frames_r[i] = end_r - init_r  # real time
    if len(pcd_bofs) == 0:
        raise ValueError("The selected frame is empty")

for i in range(len(time_frames_cpu)):
    print(
        f"The iteration {i} took {time_frames_cpu[i]:.6f}[s] CPU, {time_frames_r[i]:.6f}[s] real")

print(
    f"The max value was: {np.max(time_frames_cpu):.6f}[s] CPU, {np.max(time_frames_r):.6f}[s] real")
print(
    f"The min value was: {np.min(time_frames_cpu):.6f}[s] CPU, {np.min(time_frames_r):.6f}[s] real")
print(
    f"The average was:   {np.mean(time_frames_cpu):.6f}[s] CPU, {np.mean(time_frames_r):.6f}[s] real")
