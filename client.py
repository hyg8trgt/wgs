import socket
from tkinter import *
from threading import Thread
class gui:
    def __init__(self) :
        self.window=Tk()
        self.window.withdraw()
        self.login=Toplevel()
        self.login.title("chat app")
        self.login.configure(bg="orange",width=500,height=500)
        self.login.resizable(width=False,height=False)
        self.label=Label(self.login,text="login page",fg="red",bg="orange",font=("Calibari",30))
        self.label.place(relx=0.2,rely=0.2)
        self.tbox=Entry(self.login,text="",bd=2,width=25)
        self.tbox.place(relx=0.21,rely=0.4)
        self.button=Button(self.login,text="Submit",bg="gold",width=20,fg="brown",font=("Calibari",18),command=lambda:self.signin(self.tbox.get()))
        self.button.place(relx=0.21,rely=0.6)
        self.window.mainloop()
    def cw(self,name):
        self.name=name
        self.window.deiconify()
        self.window.title("chatapp")
        self.window.resizable(width=False,height=False)
        self.window.configure(bg="blue",width=500,height=500)
        self.username=Label(self.window,text=self.name,bg="gold",fg="brown",font=("Calibari",18))
        self.username.place(relx=0,rely=0,relwidth=1)
        self.ta=Text(self.window,width=10,height=3,bg="white",font=("Calibari",18),padx=5,pady=5)
        self.ta.place(relx=0,rely=0.08,relwidth=1,relheight=.7)
        self.labelbox=Label(self.window,height=80,bg="gray")
        self.labelbox.place(relx=0,rely=0.8,relwidth=1)
        self.messageentry=Entry(self.labelbox,bg="white",text="",bd=2,font=("Calibari",18))
        self.messageentry.place(relx=0,rely=0.008,relwidth=.75,relheight=0.09)
        self.button2=Button(self.labelbox,text="SEND",bg="gold",width=20,fg="brown",font=("Calibari",18))
        self.button2.place(relx=0.8234,rely=0.008,relwidth=.2,relheight=0.09)
        s=Scrollbar(self.ta)
        s.place(relheight=0.8,relwidth=0.112,relx=0.95,)
        s.config(command=self.ta.yview)
        self.ta.config(state=DISABLED,)
        self.ta.config(cursor="arrow",)
    def signin(self,name):
        self.login.destroy()
        self.cw(name)
    
chat=gui()