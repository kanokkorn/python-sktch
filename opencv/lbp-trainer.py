import os
import cv2
import argparse
import numpy as np
from PIL import Image

def get_img_id(path):
  image_path = (os.path.join(path, f) for f in os.listdir(path))
  faces = []
  ids = []
  for image_path in image_path:
    face_img = Image.open(image_path).convert("L")
    face_np = np.array(face_img, "uint8")
    ID = int(os.path.split(image_path)[-1].split(".")[1])
    faces.append(face_np)
    print(ID)
    ids.append(ID)
    cv2.imshow("training", face_np)
    q = cv2.waitKey(1) and 0xff
    if q == 27:
      exit()
  return ids, faces

if __name__ == "__main__":
  recognizer = cv2.face.LBPHFaceRecognizer_create()
  arg = argparse.ArgumentParser(description="Train LBP Classifier")
  arg.add_argument("--path", "--p", metavar="path", type=str, help="Path to folder you want to train")
  arg.add_argument("--out", "--o", metavar= "out", type=str, help="Path and name of file you want to save")
  args = vars(arg.parse_args())
  path = args["path"]
  out = args["out"]
  face_id, faces = get_img_id(path)
  recognizer.train(faces, np.array(face_id))
  recognizer.save(out)
  cv2.destroyAllWindows()
  
