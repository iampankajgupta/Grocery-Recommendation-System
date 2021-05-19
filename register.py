from os.path import getsize
from tkinter import *
from PIL import Image
import tkinter.messagebox
import csv
import os
import pandas as pd
import re


class Register:
    def __init__(self, root):

        self.root = root
        self.root.title = ("Register Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Background Image

        self.bg = PhotoImage(file="images/market.png")
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        

        # Reigster Frame

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=300, y=100, width=700, height=500)


        if(os.path.isfile("current_user.csv")):
            self.root.destroy()
            import mainPage

        title = Label(frame1, text="REGISTER HERE ", font=(
            "times new roman", 20, "bold"), bg="white", fg="green").place(x=230, y=50)

        first_name = Label(frame1, text="FirstName", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=100)
        self.txt_first_name = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_first_name.place(x=100, y=130, width=250)

        # -------------------------

        last_name = Label(frame1, text="LastName", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=100)

        self.txt_last_name = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")

        self.txt_last_name.place(x=400, y=130, width=250)

        contact = Label(frame1, text="Contact", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=160)
        self.txt_contact = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=100, y=190, width=250)

        email = Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=160)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_email.place(x=400, y=190, width=250)

        password = Label(frame1, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=220)
        self.txt_password = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_password.place(x=100, y=250, width=250)

        confirm_password = Label(frame1, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=220)
        self.txt_confirm_password = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_confirm_password.place(x=400, y=250, width=250)

        btn_register = Button(frame1, text="Register ", font=("times new roman", 15, "bold"),
                              cursor="hand2", bg="lightgreen", activebackground="white", command=self.register_data).place(x=230, y=350, width=250, height=35)

        hr = Label(frame1, bg="lightgray").place(
            x=200, y=400, width=310, height=2)

        btn_login = Button(frame1, text="Log In", font=("times new roman", 15, "bold"),
                           cursor="hand2", bg="white", bd=0, command=self.callNewScreen).place(x=230, y=410, width=250, height=35)

# since i want to use the upper entry data var
    def register_data(self):

        email_val = self.txt_email.get()
        password_val = self.txt_password.get()
        contact_val = self.txt_contact.get()
        first_name = self.txt_first_name.get()
        last_name = self.txt_last_name.get()
        confirm_password = self.txt_confirm_password.get()

        x = 0
        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if(email_val == "" or password_val == "" or contact_val == "" or password_val == "" or confirm_password == "" or first_name == "" or last_name == ""):
            tkinter.messagebox.showinfo('Error', "Please fill all the fields")
        elif (email_regex.match(email_val) == None):
            tkinter.messagebox.showinfo(
                'Error', "Please Enter valid email Address")
        elif(str(password_val) != str(confirm_password)):
            tkinter.messagebox.showinfo(
                'Error', "Password and Confirm Password doesn't Match")
        elif(email_regex.match(email_val) == False):
            tkinter.messagebox.showinfo(
                'Error', "Please Enter Valid Email Address")
        elif (len(contact_val) != 10):
            tkinter.messagebox.showinfo(
                'Error', "Contact Should be 10 digit Number")
        else:
            # x=0;
            # with open('users_db.csv', 'r') as file:
            #     reader = csv.reader(file)
            #     for row in reader:
            #         print(row)
            #         if(str(row[3]) == str(email_val)):
            #             x=1
            #             tkinter.messagebox.showinfo(
            #                 'Error', "Email Address is Already Present Please Login ")
            #             break;
        
            # if(x!=1):
            with open ('current_user.csv','w') as file:
                writer = csv.writer(file)
                writer.writerow(["FirstName","LastName","PhoneNumber"])
                writer.writerow([first_name,last_name,contact_val])

            self.root.destroy()
            import mainPage


    def callNewScreen(self):
        self.root.destroy()
        import login


root = Tk()
obj = Register(root)
root.resizable(0, 0)

root.mainloop()
