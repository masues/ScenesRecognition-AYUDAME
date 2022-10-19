#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2016 Massachusetts Institute of Technology

"""Extract images from a rosbag.
"""

import os
import argparse

import cv2

import rosbag
from cv_bridge import CvBridge

def main():
    """Extract a folder of images from a rosbag.
    """
    parser = argparse.ArgumentParser(description="Extract images from a ROS bag.")
    parser.add_argument("bag_file", help="Input ROS bag.")
    parser.add_argument("output_dir", help="Output directory.")
    parser.add_argument("image_topic", help="Image topic.")
    parser.add_argument("type",help="rgb or depth")

    args = parser.parse_args()

    print ("Extract images from %s on topic %s into %s" % (args.bag_file,
                                                          args.image_topic, args.output_dir))

    file=args.output_dir + "/"+ args.type + ".txt"
    f=open(file,"w")
    print(args.type)
    print(file)
    f.write("# "+ args.type + " images"+"\n")
    f.write("# file: "+ os.path.basename(args.bag_file) + "\n")
    f.write("# timestamp filename \n")

    bag = rosbag.Bag(args.bag_file, "r")
    bridge = CvBridge()
    count = 0
    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        encoding = "bgr8" if msg.encoding == "rgb8" else "passthrough"
        cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding=encoding)
        filename= "%.8f" %  msg.header.stamp.to_sec()
        cv2.imwrite(os.path.join(args.output_dir, args.type+ "/" +filename+".png" ), cv_img)
        print ("Wrote image " + str(count))
        f.write(filename+" " + args.type + "/" + filename + ".png\n" )
        count += 1

    bag.close()
    f.close()
    return

if __name__ == '__main__':
    main()