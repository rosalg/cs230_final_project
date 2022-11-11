import os

def main():
    preprocess('data_folder')
    

def writeToFile(read_dir, write_dir, img):
    with open(os.path.join(read_dir, img), "rb") as r, \
        open(os.path.join(write_dir, img), "wb") as p:
        p.write(r.read())
        r.close()
        p.close()  


def preprocess(data_folder_path):
    processed_path = os.path.join(data_folder_path, 'lfw_processed')
    os.makedirs(processed_path, exist_ok=True)
    raw_path = os.path.join(data_folder_path, 'lfw_raw')
    first_dir=prev_dir=negative_sample=None

    # Loop through each directory of headshot images
    for directory in os.listdir(raw_path):
        if directory.startswith("."): continue
        path_to_raw_image_folder = os.path.join(raw_path, directory)
        images = os.listdir(path_to_raw_image_folder)

        # Only add directories which contain more than two headshots (needed for triplet loss)
        if len(images) >= 2:
            processed_img_path = os.path.join(processed_path, directory)
            os.makedirs(processed_img_path, exist_ok=True)

            # Cache first directory to add a negative sample after all loops
            if not first_dir: first_dir = path_to_raw_image_folder

            # Add negative sample
            if negative_sample: writeToFile(prev_dir, processed_img_path, negative_sample)

            # Add each image to our processed folder structure and retain the last image as a negative sample
            # for future directory
            for img_file_name in images:

                writeToFile(path_to_raw_image_folder, processed_img_path, img_file_name)
                negative_sample = img_file_name

            prev_dir=path_to_raw_image_folder
   
    # Add a negative sample to the first headshot directory
    writeToFile(prev_dir, first_dir, negative_sample)
       
    


if __name__ == "__main__":
    main()