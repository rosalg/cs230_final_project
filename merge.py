import os
import shutil


def renameImages(data_folder_path):
    raw_path = os.path.join(data_folder_path, 'pubfig_raw')
    for file in os.listdir(raw_path):
        file_split = file.split()
        file_joined = "_".join(file_split)
        os.rename(os.path.join(raw_path, file), os.path.join(raw_path, file_joined))


def mergeSameImages(data_folder_path):

    ftw_path = os.path.join(data_folder_path, 'lfw_processed')
    all_data_path = os.path.join(data_folder_path, 'all_data_processed')
    for directory in os.listdir(ftw_path):
        if directory.startswith("."): continue
        src_dir = os.path.join(ftw_path, directory)
        dest_dir = os.path.join(all_data_path, directory)
        for img in os.listdir(src_dir):
            src_image = os.path.join(src_dir, img)
            shutil.copy(src_image, dest_dir)
    
renameImages('data_folder')
mergeSameImages('data_folder')

