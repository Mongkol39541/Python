import numpy as np
from PIL import Image
import os, cv2

class CreateModel:
    def train_classifier(train_folder, crate_file):
        path = [os.path.join (train_folder, f) for f in os.listdir(train_folder)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            faces.append(imageNp)
            ids.append(id)
        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("data_Model/" + crate_file + ".xml")

#train_folder = str(input("Select folder of train : "))
#crate_file = str(input("Createname of Model : "))
#CreateModel.train_classifier(train_folder, crate_file)