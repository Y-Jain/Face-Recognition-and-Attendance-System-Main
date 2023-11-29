
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector as con
import cv2


class Student:
    def __init__(self,root):
        self.root = root 
        # initialize root
        # to set geometry
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # variable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

        img1=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI1.jpeg")
        # to set image size
        img1=img1.resize((500,430))
        # ANTIALIAS = to convert high level image to low level image
        # to store img in variable
        self.photoimg1 = ImageTk.PhotoImage(img1)

        first_lable1 = Label(self.root,image = self.photoimg1)
        first_lable1.place(x=0,y=0,width=550,height=130)
        
        img2=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI2.jpeg")
        # to set image size
        img2=img2.resize((500,130))
        # ANTIALIAS = to convert high level image to low level image
        self.photoimg2 = ImageTk.PhotoImage(img2)

        first_lable2 = Label(self.root,image = self.photoimg2)
        first_lable2.place(x=500,y=0,width=550,height=130)

        img3=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI3.jpeg")
        # to set image size
        img3=img3.resize((500,130))
        # ANTIALIAS = to convert high level image to low level image
        self.photoimg3 = ImageTk.PhotoImage(img3)

        first_lable3 = Label(self.root,image = self.photoimg3)
        first_lable3.place(x=1000,y=0,width=550,height=130)

        img4=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\AI7.jpg")
        # to set image size
        img4=img4.resize((1530,710))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root,image= self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font = ("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=100)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=5,y=70,width=1510,height=600)    

        # left Lable frame
        Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\student1.png")
        img_left=img_left.resize((720,150))
        self.photoimg_left =ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)
        # Current course information
        ccf=LabelFrame(Left_frame,bd=2,bg="white",relief = RIDGE,text="Current Course Information",font=("times new roman",15,"bold"),fg="darkgreen")
        ccf.place(x=5,y=135,width=720,height=120)
        # department
        d_lable=Label(ccf,text="Department",font=("times new roman",12,"bold"),fg="darkgreen")
        d_lable.grid(row=0,column=0,padx=10)

        d_combo=ttk.Combobox(ccf,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        d_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        # current position
        d_combo.current(0)
        d_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        C_lable=Label(ccf,text="Course",font=("times new roman",12,"bold"),fg="darkgreen")
        C_lable.grid(row=0,column=2,padx=10)

        C_combo=ttk.Combobox(ccf,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        C_combo["values"]=("Select Courses","FSDB","DS","BE","SE")
        # current position
        C_combo.current(0)
        C_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        y_lable=Label(ccf,text="Year",font=("times new roman",12,"bold"),fg="darkgreen")
        y_lable.grid(row=1,column=0,padx=10)

        y_combo=ttk.Combobox(ccf,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        y_combo["values"]=("Select Year","1","2","3","4")
        # current position
        y_combo.current(0)
        y_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        s_lable=Label(ccf,text="Semester",font=("times new roman",12,"bold"),fg="darkgreen")
        s_lable.grid(row=1,column=2,padx=10)

        s_combo=ttk.Combobox(ccf,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=15)
        s_combo["values"]=("Select Semester",1,2,3,4,5,6,7,8)
        # current position
        s_combo.current(0)
        s_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student Information
        ccf=LabelFrame(Left_frame,bd=2,bg="white",relief = RIDGE,text="Student Information",font=("times new roman",15,"bold"),fg="darkgreen")
        ccf.place(x=5,y=250,width=720,height=300)

        # sid_lable=Label(ccf,text="StudentID",font=("times new roman",12,"bold"),fg="darkgreen")
        # sid_lable.grid(row=1,column=2,padx=10,sticky=W)

        # student id
        studentID_label = Label(ccf,text="StudentID: ",font=("times new roman",12,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(ccf,width=20,textvariable=self.va_std_id,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student Name
        studentName_label = Label(ccf,text="Student Name: ",font=("times new roman",12,"bold"))
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(ccf,width=20,textvariable=self.var_std_name,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division
        class_div_label = Label(ccf,text="Class Division: ",font=("times new roman",12,"bold"))
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        # class_div_entry=ttk.Entry(ccf,width=20,textvariable=self.var_div,font=("times new roman",12,"bold"))
        # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        div_combo=ttk.Combobox(ccf,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=15)
        div_combo["values"]=('A','B','C')
        # current position
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Roll no.
        studentRoll_label = Label(ccf,text="Roll no.: ",font=("times new roman",12,"bold"))
        studentRoll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentRoll_entry=ttk.Entry(ccf,width=20,textvariable=self.var_roll,font=("times new roman",12,"bold"))
        studentRoll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label = Label(ccf,text="Gender: ",font=("times new roman",12,"bold"))
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        # gender_entry=ttk.Entry(ccf,width=20,textvariable=self.var_gender,font=("times new roman",12,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        gender_combo=ttk.Combobox(ccf,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=15)
        gender_combo["values"]=("Male","Female","Other")
        # current position
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)
        # DOB
        dob_label = Label(ccf,text="DOB: ",font=("times new roman",12,"bold"))
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(ccf,width=20,textvariable=self.var_dob,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label = Label(ccf,text="Email: ",font=("times new roman",12,"bold"))
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(ccf,width=20,textvariable=self.var_email,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone number
        phone_label = Label(ccf,text="Phone No.: ",font=("times new roman",12,"bold"))
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(ccf,width=20,textvariable=self.var_phone,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label = Label(ccf,text="Address: ",font=("times new roman",12,"bold"))
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(ccf,width=20,textvariable=self.var_address,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Teacher name
        teacher_label = Label(ccf,text="Teacher Name: ",font=("times new roman",12,"bold"))
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(ccf,width=20,textvariable=self.var_teacher,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(ccf,variable=self.var_radio1,text="Take photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        self.var_radio2=StringVar()
        radiobtn2=ttk.Radiobutton(ccf,variable=self.var_radio1,text="No photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        # buttons frame
        btn_frame=Frame(ccf,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=210,width=715,height=37)

        # save button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        # take_photo_btn=Button(btn_frame,text="Save",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # take_photo_btn.grid(row=1,column=0)

        # update_photo_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        # update_photo_btn.grid(row=1,column=1)

        btn_frame1=Frame(ccf,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=240,width=715,height=35)

        take_photo_btn=Button(btn_frame1,text="Take Photo",command=self.generate_dataset,width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame1,text="Update Photo",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)

    # Right Lable frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"),bg="white",fg="darkgreen")
        Right_frame.place(x=750,y=10,width=800,height=580)

        img_right=Image.open(r"C:\Users\HP\OneDrive\Desktop\face\images\student3.jpg")
        img_right=img_right.resize((720,130))
        self.photoimg_right =ImageTk.PhotoImage(img_right)

        f_lbl1=Label(Right_frame,image=self.photoimg_right)
        f_lbl1.place(x=5,y=0,width=720,height=130)

        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief = RIDGE,text="Search System",font=("times new roman",15,"bold"),fg="darkgreen")
        Search_frame.place(x=5,y=135,width=710,height=70)

        search_label = Label(Search_frame,text="Search By: ",font=("times new roman",12,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_lable=Label(Search_frame,text="Semester",font=("times new roman",12,"bold"),fg="darkgreen")
        search_lable.grid(row=1,column=2,padx=10)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        Search_entry=ttk.Entry(Search_frame,width=20,font=("times new roman",12,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(Search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        showAll_btn=Button(Search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=2,pady=10,sticky=W)

        # Table Frame
        Table_frame=Frame(Right_frame,bd=2,bg="white",relief = RIDGE)
        Table_frame.place(x=5,y=210,width=710,height=250)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(Table_frame,column=("Dep","course","Year","Semester","Student_id","Name","Division","Roll","Gender","Dob","Email","Phone","Address","Teacher","PhotoSample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        # To pack scroll bar
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # to show header
        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("Student_id",text="StudentId")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Division",text="Division")
        self.student_table.heading("Roll",text="Roll")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Dob",text="DOB")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone")
        self.student_table.heading("Address",text="Address")
        self.student_table.heading("Teacher",text="Teacher")
        self.student_table.heading("PhotoSample",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)

        # To set column width
        self.student_table.column("Dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Semester",width=100)
        self.student_table.column("Student_id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Division",width=100)
        self.student_table.column("Dob",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("PhotoSample",width=150)

        self.student_table.pack(fill=BOTH,expand = 1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # function
    # function Declaration
    def add_data(self):
            if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
                messagebox.showerror("Error", "All Fields Are Required")
            else:
                try:
                    conn=con.connect(host = "localhost",user = "root",passwd = "Nakodaji@90",database = "face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Insert into student1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.va_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get()
                    ))   
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success" , "Student details has been added",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to  : {str(es)}",parent=self.root)
                    
        # Fetch Data from database
    def fetch_data(self):
            conn=con.connect(host = "localhost",user = "root",passwd = "Nakodaji@90",database = "face")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student1")
            data=my_cursor.fetchall()
            
            if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()
        
        # Get Cursor
    def get_cursor(self,event=""):
            cursor_focus=self.student_table.focus()
            content=self.student_table.item(cursor_focus)
            data=content["values"] 
            self.var_dep.set(data[0]),
            self.var_course.set(data[1]),
            self.var_year.set(data[2]),
            self.var_semester.set(data[3]),
            self.va_std_id.set(data[4]),
            self.var_std_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_teacher.set(data[13]),
            self.var_radio1.set(data[14])

        # update
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
                messagebox.showerror("Error", "All Fields Are Required")
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update",parent=self.root)
                if Upadate>0:
                    conn=con.connect(host = "localhost",user = "root",passwd = "Nakodaji@90",database = "face")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student1 set Dep=%s,course=%s,Year=%s,Name=%s,Semester=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",(
                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                self.va_std_id.get(),
                                                                                                                                                                            ))
                else:
                     if not Upadate:
                          return
                messagebox.showinfo("Success","Student details successfully updated completed",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                   messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")

    # generate photo samples
    def generate_dataset(self):
         if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
                messagebox.showerror("Error", "All Fields Are Required")
         else:
              try:
                conn=con.connect(host = "localhost",user = "root",passwd = "Nakodaji@90",database = "face")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student1")
                myresult=my_cursor.fetchall()
                id = 0
                for x in myresult:
                     id+=1
                my_cursor.execute("update student1 set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s WHERE Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.va_std_id.get()==id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ========== Load predefined data on face frontals from opencv
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                     gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #  scaling factor = 1.3
                    # Minimum Neighbour = 5
                     for (x,y,w,h) in faces:
                          face_cropped=img[y:y+h,x:x+w]
                          return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                     ret,my_frame=cap.read()
                     if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        #  STORE
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Croppped Face",face)

                     if cv2.waitKey(1)==13 or int(img_id)==100:
                          break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completely")
              except Exception as es:
                    messagebox.showerror("Error",f"Due to  : {str(es)}",parent=self.root)

# to call main
if __name__ =="__main__":
    # to call root from toolkit
    root =Tk()
    obj = Student(root)
    root.mainloop()