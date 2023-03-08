""" Test script to measure histogram generation performance over time with SIFT """

import numpy as np
from joblib import load
import sys
sys.path.append("SharedFunctions")
from BoVW import getBoVWRepresentation

# Descriptors load
dscs_train = load("Data/dscs_sift.joblib")

# Codebook load
codebook = np.load("Data/codebook_sift.npy")

# Histogram generation
print("Extracting SIFT visual word representations")
vw_train = getBoVWRepresentation(dscs_train,codebook)
np.save("Data/vw_sift",vw_train)
