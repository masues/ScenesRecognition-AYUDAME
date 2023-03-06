""" Test script to measure feature extraction performance over time with a single frame """

from extractBofs import extractBofs
import sys
sys.path.append("SharedFunctions")
from feature_extraction import FeatureExtractionTime


# Path of point clouds divided into classes
pcd_dir = "../../Proyecto_AYUDAME_Datasets/Microsoft_7scenes_pcd"
num_classes = 1
filename_num = 568 # Fixed frame
num_iterations = 10 # Number of iterations

featureExtractionTime = FeatureExtractionTime(pcd_dir,num_classes)

def callback_extractBofs(filename,_):
  pcd_bofs = extractBofs(filename, axis=2, method=2, layers=3)
  if len(pcd_bofs) == 0:
    raise ValueError("The selected frame is empty")

print("Single feature extraction BOF")
featureExtractionTime.feature_extraction_single(filename_num, num_iterations,
                                callback_extractBofs, descriptor=None)
