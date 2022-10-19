""" This script generates the point cloud files given the path of rgb images and the depth images
    If rerun, delete dirs "pcd/" and "rgb_pcd/"
"""
import open3d as o3d
import numpy as np
import os
from tqdm import tqdm

dataset_path = 'Proyecto_AYUDAME_Datasets/AYUDAME_04_arm1/'

# Reading associated_files.txt
associated_files = np.loadtxt(dataset_path+'associated_files.txt',dtype='U')

print('Creating PLY files in '+dataset_path+'pcd/')
os.makedirs(dataset_path+'pcd',exist_ok=True)
print('Creating RGB links in '+dataset_path+'rgb_pcd/')
os.makedirs(dataset_path+'rgb_pcd',exist_ok=True)
for associated_file in tqdm(associated_files):
    # Read the images
    color_raw = o3d.io.read_image(dataset_path+associated_file[1])
    depth_raw = o3d.io.read_image(dataset_path+associated_file[3])
    # Create an RGBD image in Open3D format
    # TUM dataset
    # rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    #  color_raw, depth_raw,depth_scale=5000,convert_rgb_to_intensity=False
    # )
    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
        color_raw,depth_raw,depth_trunc=3.5,
        convert_rgb_to_intensity=False
    )
    # Create an Open3D point cloud
    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(
        rgbd_image,
        o3d.camera.PinholeCameraIntrinsic(
            o3d.camera.PinholeCameraIntrinsicParameters.PrimeSenseDefault
        )
    )
    # Count the number of points in the point cloud, if it's empty,
    # skip the iteration
    num_points = len(np.asarray(pcd.points))
    if num_points == 0: continue
    # Flip it, otherwise the pointcloud will be upside down
    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
    # Write the point cloud file
    o3d.io.write_point_cloud(dataset_path+'pcd/'+associated_file[0]+'.ply', pcd,
        write_ascii=False,compressed=True,print_progress=True
    )
    # Create a reference to the used RGB images, in order to have a reference of
    # of the point cloud
    os.symlink(
        src=os.path.abspath(dataset_path+associated_file[1]),
        dst=os.path.abspath(dataset_path+'rgb_pcd/'+associated_file[0]+'.png')
    )
print('Done!')
