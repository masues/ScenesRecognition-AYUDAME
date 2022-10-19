""" This script creates a fixed named symlink frames, in order to create
a video with ffmpeg.
To create a video, use the following command
ffmpeg -r 20 -f image2 -i 'Proyecto_AYUDAME_Datasets/Ayudame_1/rgb2/%04d.png' -qscale 0 'test.mp4'
"""
import os

dataset_path = "Proyecto_AYUDAME_Datasets/AYUDAME_03"
plys = os.listdir(dataset_path+"/rgb")
plys.sort()
os.makedirs(dataset_path+"/rgb2",exist_ok=True)
for i in range(len(plys)):
    os.symlink(
        src=os.path.abspath(dataset_path+"/rgb/"+plys[i]),
        dst=os.path.abspath(dataset_path+f"/rgb2/{i:0>4}.png")
    )
