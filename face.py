from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def _init_(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_1b1=Lable(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_1b1.place(x=0,y=0,width=1530,height=45)
        

        # 1st image

        img_top=Image.open ()#imagelocation
        img_top=img_top.resize((650,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_1b1=Label(self.root,image=self.photoimg_top)
        f_1b1.place(x=0,y=55,width=650,height=700) 

        # 2nd image

        img_bottom=Image.open ()#imagelocation
        img_bottom=img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)   

        f_1b1=Label(self.root,image=self.photoimg_top)
        f_1b1.place(x=650,y=55,width=950,height=700)  

        #button
        b1_1=Button(f_lbl,text="Face Recognition",cursor="hand2",font=("times new roman",30,"bold"),bg="darkgreen",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)   
   
   #=========attendence=========
    def mark_attendance(self,i,r,n,d) with open("kiran.csv","r+",newline="\n") as f:
        myDataList=f.readlines()
        name_list=[]
        for line in myDataList:
            entry=line.split((",")) 
            name_list.append(entry{0})
        if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
            now=datetime.now()
            d1=now.strftime("%d/%m/%Y")
            dtString=now.strftime("%H:%M:%S")
            f.writelines(f"\n{i},{r},{n},{d},{dtstring},{d1},Present")

                                  

 



  #==================face Recognition=============

  def face_recog(self):
    def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf);
        gray_Image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

        coord=[]

        for (x,y,w,h) in features:
           cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
           id,predict=clf.predict(gray_image[y:y+h,x:x+w])
           confidence=int((100*(1-predict/300)))

           conn=mysql.connector.connect(host="localhost",username="root",password="Test@123" ,database="face_recognizer")
           my_cursor=conn.cursor()

           my_cursor.execute("select Name from student where Student_id="+str(id))
           i=my_cursor.fetchone()
           i="+".join(i) 

           my_cursor.execute("select Roll from student where Student_id="+str(id))
           r=my_cursor.fetchone()
           r="+".join(r)

           my_cursor.execute("select Dep from student where Student_id="+str(id))
           d=my_cursor.fetchone()
           d="+".join(d) 

           my_cursor.execute("select student_id from student where Student_id="+str(id))
           i=my_cursor.fetchone()
           i="+".join(i)
 


           if confidence>77:
              cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
              self.mark_attendance(i,r,n,d)
              
            else:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(img,f"Unknown Face{r}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

            coord=[x,y,w,y]
           
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
       cv2.imshow("welcome To Face recognition",img)

       if cv2.waitkey(1)==13:
           break
       video_cap.release()
       cv2.destroyAllwindows()
    


if __name__== "main":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()