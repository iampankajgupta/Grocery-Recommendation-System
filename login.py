from os.path import getsize
from tkinter import *
from PIL import Image
import tkinter.messagebox
import csv
import os
import pandas as pd
import re


class Login:
    def __init__(self, root):

        self.root = root
        self.root.title = ("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Background Image

        self.bg = PhotoImage(file="images/market.png")
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # Reigster Frame

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=300, y=100, width=700, height=500)

        title = Label(frame1, text="LOGIN", font=(
            "times new roman", 20, "bold"), bg="white", fg="green").place(x=300, y=50)

        # ------------------------- Contact
        email = Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=230, y=140)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_email.place(x=230, y=170, width=250)

        # -------------------------

        password = Label(frame1, text="Password ", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=230, y=210)
        self.txt_password = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_password.place(x=230, y=240, width=250)

        btn_login = Button(frame1, text="Log In", font=("times new roman", 15, "bold"),
                           cursor="hand2", bg="lightgreen", activebackground="white", command=self.login_data).place(x=230, y=300, width=250, height=35)

        hr = Label(frame1, bg="lightgray").place(
            x=210, y=410, width=310, height=2)

        btn_SignUp = Button(frame1, text="Sign Up ", font=("times new roman", 15, "bold"),
                            cursor="hand2", bg="lightgreen", command=self.callNewScreen).place(x=230, y=360, width=250, height=35)

        btn_forget = Button(frame1, text="Forget Password ?", font=("times new roman", 13),
                            bg="white", fg="#00759E", bd=0, command=self.forget_password).place(x=280, y=420)

# since i want to use the upper entry data var
    def login_data(self):

        email_val = self.txt_email.get()
        password_val = self.txt_password.get()

        x = 0
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if(email_val == "" or password_val == ""):
            tkinter.messagebox.showinfo('Error', "Please fill all the fields")
        elif (email_regex.match(email_val) == None):
            tkinter.messagebox.showinfo(
                'Error', "Please Enter valid email Address")
        else:

            global index
            global file_size
            with open('users_db.csv', 'r') as csv_file:

                csv_reader = csv.reader(csv_file)
                index = 2

                for row in csv_reader:
                    if(row[3]==""):
                        break
                    if str(row[3]) == str(email_val):
                        if(str(row[4]) == str(password_val)):
                            print("yaha aa gya hai")
                            with open('current_user.csv', 'w', newline='') as file:
                                writer = csv.writer(file)
                                writer.writerow(
                                    ["FirstName", "LastName", "PhoneNumber"])
                                writer.writerow(
                                    [str(row[0]), str(row[1]), str(row[2])])
                            x = 2
                            break
                        else:
                            x = 1
                            tkinter.messagebox.showinfo(
                                'Error', 'UserName and Password are not matching')
                            break
                    index = index + 1
                if x == 0:
                    print(str(email_val)+" "+str(password_val))
                    tkinter.messagebox.showinfo(
                        'Login', 'User Not Exits Please Register')

            if(os.path.isfile("current_user.csv") == True):
                root.destroy()
                import mainPage

    def validation(self, current_email, current_password):
        if(current_email == "" or current_password == ""):
            return False

    def forget_password(self):
        root.destroy()
        import forgot

    def callNewScreen(self):
        self.root.destroy()
        import register


root = Tk()
obj = Login(root)
root.resizable(0, 0)

root.mainloop()
