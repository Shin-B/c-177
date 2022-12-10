from tkinter import *

root=Tk()
root.title("Project 177")
root.geometry("500x500")
root.configure(background='#e8b62c')

labelname=Label(root,text="Name:",background="#e8b62c")
labelname.place(relx=0.3,rely=0.1,anchor=CENTER)

inputname=Entry(root)
inputname.place(relx=0.6,rely=0.1,anchor=CENTER)

labelpassword=Label(root,text="Password: ",background="#e8b62c")
labelpassword.place(relx=0.3,rely=0.2,anchor=CENTER)

inputpwd=Entry(root)
inputpwd.place(relx=0.6,rely=0.2,anchor=CENTER)

labelcaptcha=Label(root,text="Captcha: ",background="#e8b62c")
labelcaptcha.place(relx=0.3,rely=0.3,anchor=CENTER)

inputcaptcha=Entry(root)
inputcaptcha.place(relx=0.6,rely=0.3,anchor=CENTER)

labelshowname=Label(root,background="#e8b62c")
labelshowname.place(relx=0.5,rely=0.7,anchor=CENTER)

labelshowpassword=Label(root,background="#e8b62c")
labelshowpassword.place(relx=0.5,rely=0.8,anchor=CENTER)

labelshowcaptcha=Label(root,background="#e8b62c")
labelshowcaptcha.place(relx=0.5,rely=0.9,anchor=CENTER)

class userDB:
    def __init__(self):
        self.__username="Shin-B"
        self.__password="123cat353$"
        self.captcha="098WET2"
    def showUser(self):
        labelshowname["text"]="Name: "+self.__username
        labelshowpassword["text"]="Password: "+self.__password
        labelshowcaptcha["text"]="Captcha: "+self.captcha
        
obj=userDB()

def addUser():
    global obj
    obj.username=inputname.get()
    obj.password=inputpwd.get()
    obj.captcha=inputcaptcha.get()
    
    print("details updated.")
    
button=Button(root,text="Update Login Details",command=addUser)
button.place(relx=0.3,rely=0.5,anchor=CENTER)

button2=Button(root,text="Show Profile",command=obj.showUser)
button2.place(relx=0.7,rely=0.5,anchor=CENTER)

root.mainloop() 
