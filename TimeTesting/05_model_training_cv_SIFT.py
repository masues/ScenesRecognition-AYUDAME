""" Test script to measure model training performance over time with SIFT 
  using cross validation for hyperparameter tuning
"""

import numpy as np
import sys
sys.path.append("SharedFunctions")
from Model_Training import ModelTrainingTime

# Input data load
y_train = np.load("Data/y_sift.npy")
vw_train = np.load("Data/vw_sift.npy")

mtt = ModelTrainingTime(x_train=vw_train,y_train=y_train)
folds = 5

print("Cross-validation across kernel types, SIFT")
mtt.train_cv(folds,tune_kernel=True)

print("Cross-validation across C Regulator, SIFT")
mtt.train_cv(folds,tune_kernel=False)
