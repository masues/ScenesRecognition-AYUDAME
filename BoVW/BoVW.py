""" Implement the code necesary for BoVW """

import time
import numpy as np
import scipy.cluster.vq as vq
from joblib import dump

def getCodebook(descriptors_list,k,seed):
    descriptors = np.vstack(descriptors_list)
    num_samples = descriptors.shape[0]
    print("Computing kmeans on "+str(num_samples)+" samples with "+str(k)+" centroids")
    init = time.time()
    codebook = vq.kmeans(obs=descriptors,k_or_guess=k,iter=10,seed=seed)[0]
    end = time.time()
    print("Done in "+str(end-init)+" secs.")
    return codebook
																					
def getBoVWRepresentation(descriptors,codebook):
    print("Extracting visual word representations")
    init = time.time()
    num_imgs = len(descriptors)
    k = codebook.shape[0]
    visual_words = np.zeros((num_imgs,k),dtype=np.float32)
    for i in range(num_imgs):
        words = vq.vq(descriptors[i],codebook)[0]
        visual_words[i,:] = np.bincount(words,minlength=k)
    end=time.time()
    print("Done in "+str(end-init)+" secs.")
    return visual_words
