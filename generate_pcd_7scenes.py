""" This script generates the point cloud files given the path of rgb images and
    the depth images, in the Microsoft 7 scenes RGB-D Dataset
    If rerun, delete directory "seq-0X_pcd/"
"""
import open3d as o3d
import numpy as np
import os
from tqdm import tqdm
from glob import iglob

dataset_path = "Proyecto_AYUDAME_Datasets/Microsoft_7scenes/stairs"
dataset_sequence = "seq-01"

# Reading associated_files.txt
color_img_names = iglob(os.path.join(dataset_path,dataset_sequence,"frame-[0-9]*.color.png"))

pcd_path = os.path.join(dataset_path,dataset_sequence+"_pcd")
print("Creating PLY files in "+pcd_path)
os.makedirs(pcd_path,exist_ok=True)

for color_img_name in tqdm(color_img_names):
    # Read the images
    color_raw = o3d.io.read_image(color_img_name)
    depth_raw = o3d.io.read_image(color_img_name.replace("color","depth"))
    # Create an RGBD image in Open3D format
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw,depth_raw,depth_trunc=4,convert_rgb_to_intensity=False
    )
    # Create an Open3D point cloud
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
             width=640, height=480, fx=585, fy=585, cx=320, cy=240
        )
    )
    # Count the number of points in the point cloud, if it's empty,
    # skip the iteration
    num_points = len(np.asarray(pcd.points))
    if num_points == 0:
        print(f"No points found at {color_img_name}")
        continue
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    # Write the point cloud file
    o3d.io.write_point_cloud(
        os.path.join(pcd_path,os.path.basename(color_img_name).replace(".color","").replace("png","ply")),
        pcd,write_ascii=False,compressed=True,print_progress=True
    )
print('Done!')
