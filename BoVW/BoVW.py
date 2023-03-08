""" Bag of Visual Words implementation """

import time
import numpy as np
import scipy.cluster.vq as vq


def getCodebook(descriptors_list, k, num_samples=None, seed=None):
    """ Generate the codebook

    Args:
        descriptors_list (list): List of descriptors
        k (int): Size of the codebook
        num_samples (int): Used to sample the descriptors if the amount of them
            is too big.
        seed (int): Seed for kmeans algorithm in order to be deterministic
    """
    descriptors = np.vstack(descriptors_list)
    if num_samples:
        np.random.seed(seed)
        descriptors = descriptors[
            np.random.choice(descriptors.shape[0], num_samples, replace=False)
        ]
    else:
        num_samples = descriptors.shape[0]
    print("Computing kmeans on "+str(num_samples) +
            " samples with "+str(k)+" centroids")
    init_cpu = time.process_time()
    init_r = time.perf_counter()
    codebook = vq.kmeans(obs=descriptors, k_or_guess=k, iter=6, seed=seed)[0]
    end_cpu = time.process_time()
    end_r = time.perf_counter()
    print(f"The codebook generation took {end_cpu - init_cpu:.6f}[s] CPU, {end_r - init_r:.6f}[s] real")
    return codebook


def getBoVWRepresentation(descriptors, codebook):
    """ Given a codebook, return the BoVW representation """
    num_imgs = len(descriptors)
    print(f"Processing histogram generation over {num_imgs} samples")
    k = codebook.shape[0]
    visual_words = np.zeros((num_imgs, k), dtype=np.float32)
    init_cpu = time.process_time()
    init_r = time.perf_counter()
    for i in range(num_imgs):
        words = vq.vq(descriptors[i], codebook)[0]
        visual_words[i, :] = np.bincount(words, minlength=k)
    end_cpu = time.process_time()
    end_r = time.perf_counter()
    print(f"The histogram generation took {end_cpu - init_cpu:.6f}[s] CPU, {end_r - init_r:.6f}[s] real")
    return visual_words
