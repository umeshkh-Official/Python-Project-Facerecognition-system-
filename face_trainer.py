import cv2, os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create();
detector = cv2.CascadeClassifier(" haarcascade_frontalface_default.xml");
path = 'dataSet'

def getImagesWithID(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    IDs = []
    for imagePath in imagePaths:
        faceImage =  Image.open(imagePath).convert('L');
        faceNp = np.array(faceImage,'uint8')
        ID = int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("trainning",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces
IDs,faces= getImagesWithID(path)
recognizer.train(faces,IDs)
recognizer.save('trainner/training.yml')
cv2.destroyAllWindows()