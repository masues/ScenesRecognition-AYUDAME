""" This script orders the color images of Microsoft 7scenes to be used in
    feature extraction and classification
    If rerun this script, delete dataset_ordered_path directory first
"""

import os
from glob import iglob

dataset_path = "Proyecto_AYUDAME_Datasets/Microsoft_7scenes_seq-02"
dataset_ordered_path = "Proyecto_AYUDAME_Datasets/Microsoft_7scenes_rgb_seq-02"
dataset_sequence = "seq-02"

os.makedirs(dataset_ordered_path,exist_ok=True)

classnames = map(
    os.path.basename,
    filter(os.path.isdir,iglob(os.path.join(dataset_path,"*")))
)

for classname in classnames:
    # Generate the string path to the current classname
    content_path = os.path.join(dataset_path,classname,dataset_sequence)
    # Find all paths to every color image
    color_img_paths = iglob(os.path.join(content_path,"frame-[0-9]*.color.png"))
    # Generate the string path to the destination class directory
    class_dest_path = os.path.join(dataset_ordered_path,classname)
    # Create the destination class directory if it doesn't exist
    os.makedirs(class_dest_path,exist_ok=True)
    # Creates a symlink for every img_path in color_img_paths
    for img_path in color_img_paths:
        os.symlink(
            os.path.abspath(img_path),
            os.path.join(
                class_dest_path,
                os.path.basename(img_path).replace(".color",""))
        )
