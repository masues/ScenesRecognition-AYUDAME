""" Test script to measure model training performance over time with SIFT 
  using defined parameters
"""

import numpy as np
import sys
sys.path.append("SharedFunctions")
from Model_Training import ModelTrainingTime

# Input data load
y_train = np.load("Data/y_sift.npy")
vw_train = np.load("Data/vw_sift.npy")

mtt = ModelTrainingTime(x_train=vw_train,y_train=y_train)

print("SVM model training using defined parameters, SIFT")
mtt.train_def_params(C=4.45,kernel='rbf')
