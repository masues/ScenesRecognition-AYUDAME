""" Test script to measure histogram generation performance over time with BOF """

import numpy as np
import pickle
from sklearn.model_selection import train_test_split
import sys
sys.path.append("SharedFunctions")
from BoVW import getBoVWRepresentation

# Descriptors load
filehandler = open("Data/dscs_bof.bin", 'rb')
dscs_bof = pickle.load(filehandler)
filehandler.close()

# Codebook load
codebook = np.load("Data/codebook_bof.npy")

# Data division
X_train, X_test = train_test_split(dscs_bof,
    shuffle = True, random_state = 8)

# Histogram generation
print("Extracting BOF visual word representations")
vw_train = getBoVWRepresentation(X_train,codebook)
np.save("Data/vw_bof",vw_train)
