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
            for img_file_name in images:
                img_path = os.path.join(processed_path, filename, img_file_name)
                img = open(img_path)
                with open(processed_path, 'r'):
            # with open('.\data_folder\lfw_processed', "w") as f:


if __name__ == "__main__":
    main()
