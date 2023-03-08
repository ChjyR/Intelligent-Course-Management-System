import os
import numpy as np
from PIL import Image
import cv2
import pickle

def train_classifier():
    """train a LBPH classifyer
    """    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "data")

    # Create OpenCV LBPH recognizer for training
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    label_ids = {}
    y_label = []
    x_train = []

    # Traverse all face images in `data` folder
    for id, uid in enumerate(os.listdir(image_dir)):
        label_ids[id] = uid
        img_path = os.path.join(image_dir,uid)
        for file in os.listdir(img_path):
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(img_path, file)
                pil_image = Image.open(path)
                image_array = np.array(pil_image, "uint8")
                x_train.append(image_array)
                y_label.append(id)

    with open("model/labels.pickle", "wb") as f:
        pickle.dump(label_ids, f)

    # Train the recognizer and save the trained model.
    recognizer.train(np.array(x_train), np.array(y_label))
    recognizer.save("model/train.yml")



if __name__ == '__main__':
    train_classifier()