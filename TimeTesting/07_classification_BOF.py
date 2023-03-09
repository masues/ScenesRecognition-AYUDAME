""" Test script to measure model classification performance over time with BOF
"""

import numpy as np
from joblib import load
from sklearn.model_selection import train_test_split
import sys
sys.path.append("SharedFunctions")
from classification import classification_time

# Input data load
y_train = np.load("Data/y_bof.npy")
vw_train = np.load("Data/vw_bof.npy")

# Data division
y_train, y_test = train_test_split(y_train,
    shuffle = True, random_state = 8)

# Model load
std_slr = load("Data/std_slr_bof.joblib")
model = load("Data/svm_bof.joblib")

print("SVM model classification using BOF")
classification_time(vw_train,y_train,std_slr,model)
