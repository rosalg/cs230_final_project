import os

def main():
    preprocess('data_folder')


def preprocess(data_folder_path):
    processed_path = os.path.join(data_folder_path, 'lfw_processed')
    os.makedirs(processed_path, exist_ok=True)
    raw_path = os.path.join(data_folder_path, 'lfw_raw')
    negative_sample=processed_img_path=None
    first_dir=prev_dir=None
    counter = 0

    # Loop through each directory of headshot images
    for directory in os.listdir(raw_path):
        if directory.startswith("."): continue
        path_to_raw_image_folder = os.path.join(raw_path, directory)
        images = os.listdir(path_to_raw_image_folder)
        if counter < 5:
            print(f'prev_dir: {prev_dir}, path_to_raw_image_folder: {path_to_raw_image_folder}')

        # Only add directories which contain more than two headshots (needed for triplet loss)
        if len(images) >= 2:
            processed_img_path = os.path.join(processed_path, directory)
            os.makedirs(processed_img_path, exist_ok=True)

            # Cache first directory to add a negative sample after all loops
            if not first_dir: 
                first_dir = path_to_raw_image_folder
                print(f'first dir: {first_dir}')

            # Add negative sample
            if negative_sample:
                with open(os.path.join(prev_dir, negative_sample), "rb") as r, \
                    open(os.path.join(processed_img_path, negative_sample), "wb") as p:
                    p.write(r.read())
                    r.close()
                    p.close()

            # Add each image to our
            for img_file_name in images:
                raw_image = os.path.join(path_to_raw_image_folder, img_file_name)
                negative_sample = img_file_name
                processed_img = os.path.join(processed_img_path, img_file_name)
                if counter < 5:
                    print(f'processed_img: {processed_img}')
                with open(raw_image, "rb") as f, open(processed_img, "wb") as p:
                    p.write(f.read())
                    p.close()
                    f.close()

            prev_dir=path_to_raw_image_folder
            counter += 1

    print("finished looping")
    print(f'prev_dir: {prev_dir}, first_dir: {first_dir}, processed_img_path: {processed_img_path}, negative_sample: {negative_sample}')
    # Add a negative sample to the first headshot directory
    with open(os.path.join(prev_dir, negative_sample), "rb") as r, \
        open(os.path.join(first_dir, negative_sample), "wb") as p:
        p.write(r.read())
        r.close()
        p.close()       
    


if __name__ == "__main__":
    main()