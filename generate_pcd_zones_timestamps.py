""" This program separates PLY files in zones given timestamps
    If this program is rerun, remove the directory "zones"
"""
import os

dataset_path = "Proyecto_AYUDAME_Datasets/AYUDAME_03"
dataset_path = os.path.abspath(dataset_path)
ply_path = os.path.join(dataset_path,"pcd")

plys = sorted(os.listdir(ply_path))

timestamps = [
    ("233.110605","255.209080"),
    ("265.028148","283.561955"),
    ("292.352675","309.283404"),
    ("316.190633","327.310946"),
    ("336.245007","347.668691"),
    ("354.803948","368.597508"),
    ("374.501028","382.514355"),
    ("389.431335","403.611473")
]

for i in range(len(timestamps)):
    os.makedirs(os.path.join(dataset_path,"zones",f"zone_{i:0>2}"))

    ply_per_zone = list(
        filter(
            lambda file_name: file_name >= timestamps[i][0]+".ply" and file_name <= timestamps[i][1]+".ply",
            plys
        )
    )

    num_plys = len(ply_per_zone)
    for ply_name in ply_per_zone:
        os.symlink(
            src=os.path.join(ply_path,ply_name),
            dst=os.path.join(dataset_path,"zones",f"zone_{i:0>2}",ply_name)
        )

    print(f"{num_plys} files where added to zone_{i:0>2}")

print("Done!")
