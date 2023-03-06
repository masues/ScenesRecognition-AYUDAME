""" Test script to measure feature extraction performance over time with 1000 frames """

from extractBofs import extractBofs
import sys
sys.path.append("SharedFunctions")
from feature_extraction import FeatureExtractionTime


# Path of point clouds divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_pcd"
num_classes = 1

featureExtractionTime = FeatureExtractionTime(pcd_dir,num_classes)

def callback_extractBofs(filename,_):
  return extractBofs(filename,axis=2,method=2,layers=3)

print("Mutiple frames feature extraction BOF")
featureExtractionTime.feature_extraction_n(callback_extractBofs)
