""" Test script to measure model training performance over time with BOF 
  using defined parameters
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

print("SVM model training using defined parameters, BOF")
mtt.train_def_params(C=0.01,kernel='linear')
