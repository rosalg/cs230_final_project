import os

def main():
    preprocess('data_folder')


def preprocess(data_folder_path):
    processed_path = os.path.join(data_folder_path, 'lfw_processed')
    os.makedirs(processed_path, exist_ok=True)
    raw_path = os.path.join(data_folder_path, 'lfw_raw')
    for filename in os.listdir(raw_path):
        if filename==".DS_Store": continue
        path_to_raw_image = os.path.join(raw_path, filename)
        images = os.listdir(path_to_raw_image)
        if len(images) >= 2:
            processed_img_path = os.path.join(processed_path, filename)
            os.makedirs(processed_img_path, exist_ok=True)
            for img_file_name in images:
                ex_img_path = os.path.join(path_to_raw_image, img_file_name)
                with open(ex_img_path, "rb") as f, open(os.path.join(processed_img_path, img_file_name), "wb") as p:
                    p.write(f.read())
                    p.close()
                    f.close()


if __name__ == "__main__":
    main()