from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as con
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self,root):
        self.root = root 
        # initialize root
        # to set geometry
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\bg.png")
        # to set image size
        img4=img4.resize((1530,710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image= self.photoimg4)
        bg_img.place(x=0,y=50,width=1530,height=710)


        title_lbl7 = Button(self.root,text="Face Detection",font = ("times new roman",35,"bold"),bg="darkblue",fg="lightblue",cursor="hand2")
        title_lbl7.place(x=0,y=0,width=1530,height=45)
        b1_2 =Button(self.root,text="Face Detection",command=self.face_recog,font = ("times new roman",35,"bold"),bg="lightblue",fg="Black",cursor = "hand2")
        b1_2.place(x=0,y=300,width = 1530,height=60)

    def mark_attendance(self,i,r,n,d):
        with open("yash.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((",")) 
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn=con.connect(host = "localhost",user = "root",passwd = "Nakodaji@90",database = "face")
                my_cursor=conn.cursor()

                my_cursor.execute("select Student_id from student1 where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                

                my_cursor.execute("select Name from student1 where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student1 where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student1 where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>77:
                    cv2.putText(img,f"ID:{i}",(x,y-90),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-60),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-35),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{d}",(x,y-4),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,f"Unknown Face:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coor=[x,y,w,h]

            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==ord("a"):
                break
        video_cap.release()
        cv2.destroyAllWindows()

# to call main
if __name__ =="__main__":
    # to call root from toolkit
    root =Tk()
    obj = Face_Recognition(root)
    root.mainloop()