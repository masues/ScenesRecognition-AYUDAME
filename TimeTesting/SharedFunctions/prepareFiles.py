import os

def prepareFiles(rootpath,num_classes):
    """ Generates file path lists """
    files_paths = []
    classpath = sorted(os.listdir(rootpath))
    for i in range(num_classes):
        filenames = sorted(os.listdir(os.path.join(rootpath, classpath[i])))
        for filename in filenames:
            files_paths.append(os.path.join(rootpath, classpath[i], filename))
    return files_paths
