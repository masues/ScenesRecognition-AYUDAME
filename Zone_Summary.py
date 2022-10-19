""" This script generates images with keyframes of each zone """

import os
import numpy as np
import cv2 as cv

dataset_path = "Proyecto_AYUDAME_Datasets/AYUDAME_02"
zones_path = dataset_path+"/zones"

zones = os.listdir(zones_path)
zones.sort()

def get_keyframe_img(keyframe_name):
    key_img_name = keyframe_name.replace(".ply",".png")
    return cv.imread(dataset_path+"/rgb_pcd/"+key_img_name)

# The number of keyframes to show
num_keyframes = 5

for zone in zones:
    # Read the directory of each zone
    plys = os.listdir(zones_path+"/"+zone)
    plys.sort()
    num_plys = len(plys)
    plys = np.asarray(plys)
    # Get the name of the keyframes
    keyframes_names = plys[np.arange(start=0,stop=num_plys,step=num_plys//num_keyframes)]
    # Extract the images of each keyframe
    keyframes = list(map(get_keyframe_img,keyframes_names))
    # Generate a image where each frame is stacked horizontaly
    img_conca = np.hstack(keyframes)
    # Render the keyframes for each zone
    cv.imwrite(dataset_path+"/"+zone+".png",img_conca)
