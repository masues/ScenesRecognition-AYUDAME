""" This program separates a set of PLY files in a integer num of zones in the
most equitable way.
If this program is rerun, remove the directory "zones"
"""
import os

dataset_path = "Proyecto_AYUDAME_Datasets/AYUDAME_02/"
ply_path = dataset_path+"pcd"


num_zones = 18
plys = os.listdir(ply_path)
plys.sort()
num_plys = len(plys)

rem = num_plys % num_zones

# count the number of elements that has been added to a zone
zone_idx = 0

for i in range(num_zones):
    os.makedirs(dataset_path+f"zones/zone_{i:0>2}")

    # Number of plys per zone
    num_el_zone = num_plys // num_zones

    # If num_plys / num_zones is not an integer, it adds an element to the zone
    if rem != 0 and i < rem:
        num_el_zone += 1

    for j in range(num_el_zone):
        os.symlink(
            src=os.path.abspath(ply_path+"/"+plys[zone_idx+j]),
            dst=os.path.abspath(dataset_path+f"zones/zone_{i:0>2}/"+plys[zone_idx+j])
        )

    zone_idx += num_el_zone

    print(f"{num_el_zone} elements where added to zone {i:0>2}")

print("Done!")
