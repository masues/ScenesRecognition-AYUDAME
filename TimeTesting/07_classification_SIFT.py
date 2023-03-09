""" Test script to measure model classification performance over time with SIFT
"""

import numpy as np
from joblib import load
import sys
sys.path.append("SharedFunctions")
from classification import classification_time

# Input data load
y_train = np.load("Data/y_sift.npy")
vw_train = np.load("Data/vw_sift.npy")

# Model load
std_slr = load("Data/std_slr_sift.joblib")
model = load("Data/svm_sift.joblib")

print("SVM model classification using SIFT")
classification_time(vw_train,y_train,std_slr,model)
