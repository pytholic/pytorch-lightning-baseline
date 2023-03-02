import glob
import os

data_dir = os.getcwd() + "/data/images/"

file_list = sorted(glob.glob(data_dir + "*"))
for class_path in file_list:
    for idx, img_path in enumerate(glob.glob(class_path + "/*")):
        if idx > 50:
            os.remove(img_path)
