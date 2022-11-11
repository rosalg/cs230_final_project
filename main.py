import os

def main():
    preprocess('.\data_folder')


def preprocess(data_folder_path):
    processed_path = os.path.join(data_folder_path, 'lfw_processed')
    os.makedirs(processed_path, exist_ok=True)
    raw_path = os.path.join(data_folder_path, 'lfw_raw')
    for filename in os.listdir(raw_path):
        path_to_raw_image = os.path.join(raw_path, filename)
        images = os.listdir(path_to_raw_image)
        if len(images) >= 2:
            processed_img_path = os.path.join(processed_path, filename)
            os.makedirs(processed_img_path, exist_ok=True)
            for img_file_name in images:
                raw_image = open(path_to_raw_image)
                new_processed_img = open(os.path.join(processed_img_path, img_file_name), "wb")
                new_processed_img.write(raw_image)
                new_processed_img.close()


if __name__ == "__main__":
    main()
