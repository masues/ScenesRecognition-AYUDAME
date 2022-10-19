""" This script extracts RGB and depth images from a rosbag created with realsense
    camera.
    rgb_path and depth_path must exist
"""
import os
import rosbag
import cv2
from cv_bridge import CvBridge

bag_file = "/Proyecto_AYUDAME_Datasets/IIMAS_Scene/20220824_131611.bag"
output_dir = "/Proyecto_AYUDAME_Datasets/TestDatasets/"
rgb_path = output_dir + "rgb/"
depth_path = output_dir + "depth/"
bridge = CvBridge()

rgb_file = output_dir + "rgb.txt"
rgb_file_o = open(rgb_file,"w")
rgb_file_o.write("# color images\n")
rgb_file_o.write("# file: "+ os.path.basename(bag_file) + "\n")
rgb_file_o.write("# timestamp filename \n")

depth_file = output_dir + "depth.txt"
depth_file_o = open(depth_file,"w")
depth_file_o.write("# depth maps\n")
depth_file_o.write("# file: "+ os.path.basename(bag_file) + "\n")
depth_file_o.write("# timestamp filename \n")


with rosbag.Bag(bag_file, "r") as bag:
    for topic,msg,t in bag.read_messages():
        # Color images
        if topic == "/device_0/sensor_1/Color_0/image/data": 
            cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")
            timestr = "%.8f" %  msg.header.stamp.to_sec()
            image_name = timestr + ".png"# an extension is necessary
            cv2.imwrite(rgb_path + image_name, cv_image)
            rgb_file_o.write(f"{timestr} rgb/{image_name}\n")
            print(f"Wrote rgb/{image_name}")
        # Depth maps
        if topic == "/device_0/sensor_0/Depth_0/image/data": 
            cv_image = bridge.imgmsg_to_cv2(msg, "passthrough")
            timestr = "%.8f" %  msg.header.stamp.to_sec()
            image_name = timestr + ".png"# an extension is necessary
            cv2.imwrite(depth_path + image_name, cv_image)
            depth_file_o.write(f"{timestr} depth/{image_name}\n")
            print(f"Wrote depth/{image_name}")

rgb_file_o.close()
depth_file_o.close()
