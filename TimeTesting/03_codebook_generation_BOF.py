""" Test script to measure codebook generation performance over time with BOF """

import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import sys
sys.path.append("SharedFunctions")
from BoVW import getCodebook

y_bof = np.load("Data/y_bof.npy")
filehandler = open("Data/dscs_bof.bin", 'rb')
dscs_bof = pickle.load(filehandler)
filehandler.close()

# Data division
X_train, X_test, y_train, y_test = train_test_split(dscs_bof, y_bof,
    shuffle = True, random_state = 8)


k = 256 # Codebook size
print("Codebook generation BOF")
getCodebook(X_train,k,None,13)
