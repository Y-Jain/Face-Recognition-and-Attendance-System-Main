from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as con
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root 
        # initialize root
        # to set geometry
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl7 = Button(self.root,text="Train Data",font = ("times new roman",35,"bold"),bg="darkblue",fg="lightblue",cursor="hand2")
        title_lbl7.place(x=0,y=0,width=1530,height=45)
        b1_1 =Button(self.root,text="Train Data",command=self.train_classifier,font = ("times new roman",35,"bold"),bg="lightblue",fg="Black",cursor = "hand2")
        b1_1.place(x=0,y=50,width = 1530,height=60)
   
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') 
            # gray scale img
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)
        # classifier
        try:
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training dataset")
        except Exception as es:
                    messagebox.showerror("Error",f"Due to  : {str(es)}",parent=self.root)


# to call main
if __name__ =="__main__":
    # to call root from toolkit
    root =Tk()
    obj = Train(root)
    root.mainloop()