""" This script iterate over the name of each category in Microsoft 7 scenes and
creates likns to each folder of point clouds
"""
import os

# Path of the full dataset
m7s_path = "Microsoft_7scenes"
# Path where the symlinks will be stored
m7s_pcd_path = "Microsoft_7scenes_pcd"
# Name of the directory that has the point clouds in the full dataset
seq_dir = "seq-01_pcd"

labels = os.listdir(m7s_path)
# filter the listed files that are directories
labels = filter(lambda label: os.path.isdir(os.path.join(m7s_path,label)),labels)

for label in labels:
    os.symlink(
        src = os.path.abspath(os.path.join(m7s_path,label,seq_dir)),
        dst = os.path.join(m7s_pcd_path,label)
    )
