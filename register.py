from os.path import getsize
from tkinter import *
from tkinter import ttk
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
        Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # Reigster Frame

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=300, y=100, width=700, height=500)

        if(os.path.isfile("current_user.csv") == True):
            self.root.destroy()
            import mainPage

        Label(frame1, text="REGISTER HERE ", font=(
            "times new roman", 20, "bold"), bg="white", fg="green").place(x=230, y=50)

        Label(frame1, text="FirstName", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=100)
        self.txt_first_name = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_first_name.place(x=100, y=130, width=250)

        # -------------------------

        Label(frame1, text="LastName", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=100)

        self.txt_last_name = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")

        self.txt_last_name.place(x=400, y=130, width=250)

        Label(frame1, text="Contact", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=160)
        self.txt_contact = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_contact.place(x=100, y=190, width=250)

        Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=160)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_email.place(x=400, y=190, width=250)

        Label(frame1, text="Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=220)
        self.txt_password = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_password.place(x=100, y=250, width=250)

        Label(frame1, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=220)
        self.txt_confirm_password = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_confirm_password.place(x=400, y=250, width=250)



        Label(frame1, text="Security Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=100, y=275)

        self.cmb_quest = ttk.Combobox(frame1,font=("times new roman",15),state="readonly",justify=CENTER,background="lightgray")

        self.cmb_quest['values']  = ("Select","PetName","Your Birth Place","Your Best Friend Name")

        self.cmb_quest.place(x=100,y=310,width=250)
        self.cmb_quest.current(0)




        

        Label(frame1, text="Confirm Password", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=220)
        self.txt_confirm_password = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_confirm_password.place(x=400, y=250, width=250)



        Label(frame1, text="Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=400, y=280)
        self.txt_answer = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=400, y=310, width=250)

        Button(frame1, text="Register ", font=("times new roman", 15, "bold"),
                              cursor="hand2", bg="lightgreen", activebackground="white", command=self.register_data).place(x=230, y=390, width=250, height=35)

        hr = Label(frame1, bg="lightgray").place(
            x=200, y=440, width=310, height=2)

        Button(frame1, text="Log In", font=("times new roman", 15, "bold"),
                           cursor="hand2", bg="white", bd=0, command=self.callNewScreen).place(x=230, y=450, width=250, height=35)


    def register_data(self):

            email_val = self.txt_email.get()
            password_val = self.txt_password.get()
            contact_val = self.txt_contact.get()
            first_name = self.txt_first_name.get()
            last_name = self.txt_last_name.get()
            confirm_password = self.txt_confirm_password.get()

            answer = self.txt_answer.get()
            selected_ques = self.cmb_quest.get()
        
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
            elif (len(answer)==0):
                tkinter.messagebox.showinfo(
                    'Error', "Please type the answer for selected Security Question")

            elif (str(selected_ques)=="Select"):
                tkinter.messagebox.showinfo(
                    'Error', "Please Select the Valid Security Question")

            else:
                f = open("users_db.csv",'r')
                reader = csv.reader(f)
                try:
                    for row in reader:
                        if(row[3]==str(email_val)):
                            tkinter.messagebox.showinfo("Error","User Already Registered Please Login !!")
                            break

                except IndexError:

                    with open('users_db.csv','a',newline=None) as file:
                        writer = csv.writer(file)
                        writer.writerow([first_name,last_name,contact_val,email_val,password_val,confirm_password,selected_ques,answer])

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
