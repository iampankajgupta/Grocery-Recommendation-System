from os.path import getsize
from tkinter import *
from tkinter import ttk
from PIL import Image
import tkinter.messagebox
import csv
import os
import pandas as pd
import re


class Forgot:
    def __init__(self, root):

        self.root = root
        self.root.title = ("Forgot Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Background Image

        self.bg = PhotoImage(file="images/market.png")
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # Reigster Frame

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=300, y=100, width=700, height=500)

        title = Label(frame1, text="FORGOT PASSWORD", font=(
            "times new roman", 20, "bold"), bg="white", fg="green").place(x=210, y=50)

        self.question = Label(frame1, text="Security Question", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=230, y=110)

        self.cmb_quest = ttk.Combobox(frame1,font=("times new roman",15),state="readonly",justify=CENTER,background="lightgray")

        self.cmb_quest['values']  = ("Select","PetName","Your Birth Place","Your Best Friend Name")

        self.cmb_quest.place(x=230,y=150,width=250)
        self.cmb_quest.current(0)


        answer = Label(frame1, text="Answer", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=230, y=200)
        self.txt_answer = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=230, y=230, width=250)

        # ------------------------- Contact
        email = Label(frame1, text="Email", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=230, y=260)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="lightgray")
        self.txt_email.place(x=230, y=290, width=250)

        # -------------------------

        Label(frame1, text=" New Password ", font=(
            "times new roman", 15, "bold"), bg="white", fg="gray").place(x=230, y=320)
        self.txt_new_password = Entry(frame1, show="*", font=(
            "times new roman", 15), bg="lightgray")
        self.txt_new_password.place(x=230, y=350, width=250)

        Button(frame1, text="CHANGE PASSWORD", font=("times new roman", 15, "bold"),
               cursor="hand2", bg="lightgreen", activebackground="white", command=self.change_password).place(x=230, y=400, width=250, height=35)

        hr = Label(frame1, bg="lightgray").place(
            x=210, y=442, width=330, height=2)

        Button(frame1, text="LOG IN ", font=("times new roman", 15, "bold"),
                            cursor="hand2", bg="lightgreen", command=self.callNewScreen).place(x=230, y=450, width=250, height=35)


# since i want to use the upper entry data var

    def change_password(self):

        security_question = self.cmb_quest.get()
        ans = self.txt_answer.get()

        email_val = self.txt_email.get()
        new_password = self.txt_new_password.get()


        print(security_question)


        email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if(email_val == "" or new_password == ""):
            tkinter.messagebox.showinfo('Error', "Please fill all the fields")
        elif (email_regex.match(email_val) == None):
            tkinter.messagebox.showinfo(
                'Error', "Please Enter valid email Address")
        elif (ans == ""):
            tkinter.messagebox.showinfo(
                'Error', "Answer Field is Empty")
        elif (security_question == "Select"):
            tkinter.messagebox.showinfo(
                'Error', "Please Select the valid Security Question")

        else:

            user_values = []
            updated_row = []
            try:
                with open('users_db.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)
                    for row in csv_reader:
                        if row[3] == email_val and row[6] == security_question and row[7] == ans:
                            updated_row.append(row)
                        else:
                            user_values.append(row)

                root.destroy()
                import login
            except IndexError:
                # if(len(updated_row) != 0):

                updated_row[4] = new_password
                updated_row[5] = new_password

                user_values.append(updated_row)

                print(user_values)
  
                    # f = open("user_db.csv", 'w+')
                    # f.close()

                    # with open('users_db.csv', 'w', newline='') as file:
                    #     writer = csv.writer(file)
                    #     writer.writerows(user_values)

                # else:

                    # tkinter.messagebox.showinfo(
                    #     'Login', 'User Not Exits')
        import forgot

    def callNewScreen(self):
        self.root.destroy()
        import login


root = Tk()
obj = Forgot(root)
root.resizable(0, 0)

root.mainloop()
