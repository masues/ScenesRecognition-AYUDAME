""" Test script to measure feature extraction performance over time with 1000 frames """

import time
from extractBofs import extractBofs
from prepareFiles import prepareFiles

# Path of point clouds divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_pcd"

# Extracts features on the first n classes only
num_classes = 1

# Skipped frames due to empty point cloud
skippted_frames = 0

files_paths = prepareFiles(pcd_dir,num_classes)

init_cpu = time.process_time()
init_r = time.perf_counter()
for filename in files_paths:
    pcd_bofs = extractBofs(filename,axis=2,method=2,layers=3)

    # Skip iteration if the point cloud is empty
    if len(pcd_bofs) == 0:
        skippted_frames += 1
        continue

end_cpu = time.process_time()
end_r = time.perf_counter()

print(f"{len(files_paths)} frames processed")
print(f"{skippted_frames} frames were skipped")
print(f"The feature extraction took {end_cpu - init_cpu:.6f}[s] CPU, {end_r - init_r:.6f}[s] real")
