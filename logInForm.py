
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pymysql

class Register:
    def __init__(self,root):
        self.root = root 
        self.root.title("Registetion Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        # bg-image
        
        self.bg=ImageTk.PhotoImage(file="image/2.jpg")
        bg=Label(self.root,image=self.bg).place(x=150,y=0,relwidth=1,relheight=1)
        # leftimage
        self.left=ImageTk.PhotoImage(file="image/3.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        
    
        fname1= Frame(self.root,bg="white")
        fname1.place(x=480,y=100,width=700,height = 500)
        
        title= Label(fname1,text="Register Here",font=("times new roman",20,"bold"),bg="white", fg="green").place(x=50,y=30)
        
        self.var_fname=StringVar()


        fname= Label(fname1,text="First Name",font=("times new roman",15),bg="white", fg="gray").place(x=50,y=100)
        self.text_fname = Entry(fname1,font=("time new roman",15),bg ="lightgray",textvariable=self.var_fname)
        self.text_fname.place(x=50,y=130,width=250)

        lname= Label(fname1,text="Last Name",font=("times new roman",15),bg="white", fg="gray").place(x=370,y=100)
        self.text_lname = Entry(fname1,font=("time new roman",15),bg ="lightgray")
        self.text_lname.place(x=370,y=130,width=250) 

        contact= Label(fname1,text="Contact Number",font=("times new roman",15),bg="white", fg="gray").place(x=50,y=170)
        self.text_contact = Entry(fname1,font=("time new roman",15),bg ="lightgray")
        self.text_contact.place(x=50,y=200,width=250)

        email= Label(fname1,text="Email address",font=("times new roman",15),bg="white", fg="gray").place(x=370,y=170)
        self.text_email= Entry(fname1,font=("time new roman",15),bg ="lightgray")
        self.text_email.place(x=370,y=200,width=250)



        question= Label(fname1,text="Sequirity Queation",font=("times new roman",15),bg="white", fg="gray").place(x=50,y=240)
        self.cmb_question =ttk.Combobox(fname1,font=("time new roman",13),state="readonly",justify="center")
        self.cmb_question["values"] = ("Select","Your first pet name","Your birth place","Your best friend name")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)

        answer= Label(fname1,text="Answer",font=("times new roman",15),bg="white", fg="gray").place(x=370,y=240)
        self.text_answer= Entry(fname1,font=("time new roman",15),bg ="lightgray")
        self.text_answer.place(x=370,y=270,width=250)
        


        password= Label(fname1,text="Password",font=("times new roman",15),bg="white", fg="gray").place(x=50,y=310)
        self.text_password = Entry(fname1,font=("time new roman",15),bg ="lightgray")
        self.text_password.place(x=50,y=340,width=250)

         

        conpass= Label(fname1,text="Comfirm Password",font=("times new roman",15),bg="white", fg="gray").place(x=370,y=310)
        self.text_conpass= Entry(fname1,font=("time new roman",15),bg ="lightgray")
        self.text_conpass.place(x=370,y=340,width=250)


        
        self.var_chk = IntVar()
        self.chk=Checkbutton(fname1,text="I Agree The Terms & Condition",onvalue=1,offvalue=0,variable=self.var_chk,bg="white",font=("time new roman", 12))
        self.chk.place(x=50,y=380)
         
        # self.btn =ImageTk.PhotoImage(file="image/reg_btn.png")
        # btn = Button(fname1,image=self.btn,bd=0,cursor="hand2").place(x=50,y=420,)
  
        btn_ragister= Button(fname1,text="Register Now",font=("times new roman",20),bd=0,cursor="hand2",command=self.register_data,fg="white",bg="deepskyblue").place(x=50,y=420,width=180)

        singUp= Button(self.root,text="Sing In",font=("times new roman",20),bd=0,cursor="hand2",fg="green",bg="white").place(x=200,y=460,width=180)

    def clear(self):
        self.text_fname.delete(0,END)   
        self.text_lname.delete(0,END)   
        self.text_contact.delete(0,END)   
        self.text_email.delete(0,END)   
        self.text_password.delete(0,END)   
        self.text_conpass.delete(0,END)   
        self.text_answer.delete(0,END) 
        self.cmb_question.current(0)   


    def register_data(self):
        if self.text_fname.get()=="" or self.text_contact.get()=="" or self.text_email.get()=="" or self.cmb_question.get()=="select" or self.text_answer.get()==" " or self.text_password.get()=="" or self.text_conpass.get()=="":
                  messagebox.showerror("Error","All fields are required",parent = self.root)

        elif self.text_password.get() != self.text_conpass.get():
            messagebox.showerror("Error","pasword and comfirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please agree our terms & condition",parent=self.root)
        else:
            try:
                con = pymysql.connect(host="localhost",user = "root", passwd="",database="employee2")
                cur=con.cursor() 
                cur.execute("select * from employee where email=%s",self.text_email.get())
                row = cur.fetchone()
                # print(row)

                if row != None:
                    messagebox.showerror("Error","User already Exist,please try with another email",parent = self.root)  
                else:

                    cur.execute("Insert into employee (fname,lname,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.text_fname.get(),
                        self.text_lname.get(),
                        self.text_contact.get(),
                        self.text_email.get(),
                        self.cmb_question.get(),
                        self.text_answer.get(),
                        self.text_password.get(),))
                    con.commit()
                    con.close()    
                    messagebox.showerror("Error","Register Successful",parent = self.root)  
                    self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to : {str(es)}",parent = self.root)

                







        # self.text_lname.get(),
        # self.text_contact.get(),
        # self.text_email.get(),
        # self.cmb_question.get(),
        # self.text_answer.get(),
        # self.text_password.get(),
        # self.text_conpass.get())
        
        





root=Tk()
obj = Register(root)
root.mainloop()
