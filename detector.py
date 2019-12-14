import cv2
from tkinter import messagebox

import mysql.connector
import numpy as np
from datetime import datetime
now=datetime.now()
formatted_date= now.strftime('%Y-%m-%d %H:%M:%S')

def getProfile(id):
    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="tiger",database="employee")
    cmd="SELECT *FROM emp WHERE ID=" +str(id)
    mycur = conn.cursor()
    mycur.execute(cmd)
    q=mycur
    profile= None
    for row in q:
        profile=row
    conn.close()
    return profile
def facedetecting():
    faceDetect  = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read("trainner//training.yml")
    id=0
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, img = cam.read();
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5);

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x + 2, y + 2), (x + w + 2, y + h + 2), (255, 0, 0), 2)
            id,conf = rec.predict(gray[y:y+h, x:x+w])
            profile=getProfile(id)
            #NAME = NameFind.ID2Name(id)

            cv2.putText(img, str(id), (x + 5, y + h +30), font, 1, (255, 255, 255), 1)
            #cv2.putText(img, str(NAME), (x + 5, y + h + 60), font, 1, (255, 255, 255), 1)
            cv2.putText(img, str(profile[1]), (x + 5, y + h + 60), font, 1, (255, 255, 255), 1)
            cv2.putText(img, str(profile[2]), (x + 5, y + h + 90), font, 1, (255, 255, 255), 1)
            cv2.imshow('camera', img)
            conn = mysql.connector.connect(host="127.0.0.1", user="root", password="tiger", database="employee")
            try:
                cmd2 = "INSERT INTO attend(id,name,datatime) VALUES("+str(id)+",'"+profile[1]+"','"+formatted_date+"')"
                mycur = conn.cursor()
                mycur.execute(cmd2)
                conn.commit()
                conn.close()
            except Exception:
                print("duplicate entry")
        if cv2.waitKey(10) & 0xFF == ord('q'): # Press 'ESC' for exiting video
            break


    cam.release()
    cv2.destroyAllWindows()
facedetecting()