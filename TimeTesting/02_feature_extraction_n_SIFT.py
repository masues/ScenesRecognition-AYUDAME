""" Test script to measure feature extraction performance over time with 1000 frames """

import cv2 as cv
import sys
sys.path.append("SharedFunctions")
from feature_extraction import FeatureExtractionTime

# Path of RGB images divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_rgb"
num_classes = 1

featureExtractionTime = FeatureExtractionTime(pcd_dir,num_classes)

def callback_sift(filename,descriptor):
  img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
  _, des = descriptor.detectAndCompute(img, None)
  return des

descriptor = cv.SIFT_create()
print("Mutiple frames feature extraction SIFT")
featureExtractionTime.feature_extraction_n(callback_sift,descriptor)
