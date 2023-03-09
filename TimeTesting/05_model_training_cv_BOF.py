""" Test script to measure model training performance over time with BOF 
  using cross validation for hyperparameter tuning
"""

import numpy as np
from sklearn.model_selection import train_test_split
import sys
sys.path.append("SharedFunctions")
from Model_Training import ModelTrainingTime

# Input data load
y_train = np.load("Data/y_bof.npy")
vw_train = np.load("Data/vw_bof.npy")

# Data division
y_train, y_test = train_test_split(y_train,
    shuffle = True, random_state = 8)

mtt = ModelTrainingTime(x_train=vw_train,y_train=y_train)
folds = 5

print("Cross-validation across kernel types, BOF")
mtt.train_cv(folds,tune_kernel=True)

print("Cross-validation across C Regulator, BOF")
mtt.train_cv(folds,tune_kernel=False)
