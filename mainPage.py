# from re import L
# from sys import winver
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import time as tm
import tkinter as tk
from numpy.lib.arraypad import pad
from numpy.lib.type_check import real
import pandas as pd
import matplotlib.pyplot as plt
from pandas import np
import tkinter.messagebox
import os
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder  # object for apriori
from PIL import Image as IMG, ImageDraw  # for text to image


filename = 'orders.csv'
columns = ['Date', 'Time', 'Name', 'Mobile Number', 'Product', 'Total Amount']
root = Tk()
root.title('Retail billing and Recommend')
root.geometry('1550x980')

root.configure(background="green")

row = 9
num = 1  # serial number
Product = []
Price = []
ItemsPurchased = []
global dataDict

amount = 0
user_values = []

# bg = PhotoImage(file="images/market.png")

# my_label = Label(root,image=bg)
# my_label.place(x=0,y=0,relwidth=1,relheight=1)

def time():  # function to display date and time
    global TM, DT, q
    DT = ""
    TM = ""
    time1 = q = tm.ctime(tm.time()).split(sep=' ')[-2]
    dateV = list(tm.localtime()[:3])
    q = q[:len(q)-3]
    for i in dateV:
        DT += str(i)
        DT += '/'
    DT = DT[:len(DT)-1]
    date = tk.Label(root, bg="green", text='Date: ' + DT +
                    '\tTime: '+str(q), font=("times new roman", 15), bd=3)
    date.place(x=1500, y=10)


time()

def Submit():

    dataDict = {}
    items = ""
    for ele in ItemsPurchased:
        items+=ele.rstrip()+","

    dataset = [DT, q, user_values[0],contact,items,amount]

    for i in columns:
        for j in dataset:
            if columns.index(i) == dataset.index(j):
                dataDict.update({i: str(j)})
    print(dataDict)
    if os.path.isfile('orders.csv'):
        fileD = pd.read_csv('orders.csv')
        fileD = fileD.append(dataDict, ignore_index=True)
    else:
        fileD = pd.DataFrame(dataDict, columns=columns, index=[0])

    fileD.to_csv(filename, index=False)


    top = tk.Toplevel()
    lab = tk.Label(top, text='Submitted Successfully!!!',
                   font=('Arial', 15), fg='green')
    lab.pack()
    top.mainloop()

def getCurrentUser():
    df = pd.read_csv("current_user.csv",usecols=[0,1,2])
    user_values.append(df.iloc[0,0])
    user_values.append(df.iloc[0,1])
    user_values.append(df.iloc[0,2])

    return user_values

def add():
    global amount
    global num
    global row
    global quantityE, productE, Product
    global currentProductAmount

    
    searchItem = search.get()

    current = str(cmb_quest.get())

    if(checkItem(searchItem)):

        if current == "Quantity":
            tkinter.messagebox.showinfo(
                "Quantity", "Please Select the Valid Quantity")
        else:
        
            currentProductAmount = int(getCurrentProductAmount(searchItem))
            totalCurrentProductAmount = int(current) * currentProductAmount

            amount += totalCurrentProductAmount

            # this var is used so that on submit it can pass and save and recommend
            # Product.append(productName)
            Price.append(totalCurrentProductAmount)
            ItemsPurchased.append(searchItem) 

            row += 25
            num += 1

            orderItem = Label(root, text=str(searchItem).upper() + "  1 x "+str(current) +
                              "--> "+str(totalCurrentProductAmount)+" Rs", font=("times new roman", 11, "bold"), bg="green")
            orderItem.place(x=1470, y=280+row)
            cmb_quest.current(0)
         

            total.config(text="Total Amount : "+str(amount)+" Rs")

    else:
        tkinter.messagebox.showinfo(
            "Item Not Found", "Please Select the Item from the Given List")


def getCurrentProductAmount(data):

    realPrice = ""
    start = False
    for ele in data:

        if(ele == '['):
            start = True

        elif(ele == 'R'):
            break
        elif start == True:
            realPrice += ele

    return int(realPrice)


def checkItem(data):
    for item in listP:
        if item.lower() == data.lower():
            return True
    return False


def update(data):

    # myList.delete(0,END)

    listbox.delete(0, END)

    for item in data:
        listbox.insert(END, item)


def check(e):

    # grab what was types
    typed = search.get()
    if typed == '':
        data = listP
    else:
        data = []
        for item in listP:
            if typed.lower() in item.lower():
                data.append(item)

    # update the list box with selected item
    update(data)


# def Printbill():
#     if(len(ItemsPurchased)==0):
#         tkinter.messagebox.showinfo("CartMessage","Cart is Empty")
#     elif(os.path.isfile('print.txt')):
#         os.remove('print.txt')
#     else:

#         with open('print.txt', 'a') as file:
#             file.write('\t\t Product Bill \t\t\n')
#             file.write('\t\t-----------------------\t\t\n')
#             file.write(f'Date : {DT}\t\t\t Time : {q}\n\n')
#             file.write('Product name\t\t\t\t\t\t Price\n')
        
#         i=0
#         for i,j in zip(ItemsPurchased,Price):
#             with open('print.txt','a') as file:
#                 file.write(f'{i}\t\t\t\t\t\t{j}\n')

#         with open('print.txt', 'a') as file:

#             file.write(f'\n\n\n Payable Amount:{amount} Rs \n')
            
#         os.startfile("print.txt",)  # print bill using printer


# update entry with list box
def fillout(e):

    search.delete(0, END)
    # add clicked item to entry box

    search.insert(0, listbox.get(ACTIVE))


def logout():
    os.remove("current_user.csv")
    root.withdraw();
    os.system("login.py")

def recommendItems():
    df = pd.read_csv('orders.csv')
    df1 = df['Product'].apply(lambda x: x.split(','))
    
    te = TransactionEncoder()
    te_ary = te.fit(df1).transform(df1)
    df1 = pd.DataFrame(te_ary, columns=te.columns_).drop('', axis=1)

    frequent_itemsets = apriori(df1, min_support=0.03, use_colnames=True)

    frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(
        lambda x: len(x))
    items = frequent_itemsets[(frequent_itemsets['length']>=2) &
                              (frequent_itemsets['support'] >= 0.04)]
    recP = items['itemsets']

    class SampleApp(tk.Tk):
        def __init__(self, *args, **kwargs):
            tk.Tk.__init__(self, *args, **kwargs)
            lb = tk.Listbox(self)
            for i in recP:
                lb.insert(tk.END, tuple(i))
            lb.bind("<Double-Button-1>", self.OnDouble)
            lb.pack(side="top", fill="both", expand=True)

        def OnDouble(self, event):
            widget = event.widget
            selection = widget.curselection()
            value = widget.get(selection[0])

            try:
                total = 0;
                for row in value:
                    total+=getCurrentProductAmount(row)
                
                img = IMG.new('RGB', (60, 30), color = (0,0,0))
                d = ImageDraw.Draw(img)
                d.text((10,10), "Rs."+str(total), fill=(255,255,255))
                img.save('images/recommend_price.png')
                list_file=os.scandir('images')
                item_list=[i.name for i in iter(list_file)]
                first,second='',''

                for i in item_list:
                    if str(value[0])==i[:len(str(value[0]))]:
                        first=i
                    if str(value[1])==i[:len(str(value[1]))]:
                        second=i
               
                for j in [first,second,'recommend_price.png']:
                    plt.subplot(1,3,[first,second,'recommend_price.png'].index(j)+1)
                    img=plt.imread('images/'+j)
                    plt.imshow(img)
                    plt.xlabel(j[:-4])
                    plt.xticks([])
                    plt.yticks([])
                    plt.autoscale()
                plt.show()
                if(len(value)<=2):
                    label=tk.Label(root,text=str(value[0])+'+'+str(value[1])+' = Rs.'+str(int(total)),font=('Tahoma',30),fg='white',bg='black')

                else:
                     label=tk.Label(root,text=str(value[0])+'+'+str(value[1])+"+"+str(value[2])+' = Rs.'+str(int(total)),font=('Tahoma',30),fg='white',bg='black')
            except Exception:
                roo = tk.Tk()
                roo.title('Offer for you...')
                label = tk.Label(roo, text='Something went wrong!!!', font=(
                    'Tahoma', 30), fg='white', bg='black')
                label.pack()
                roo.mainloop()

    if __name__ == "mainPage":
        app = SampleApp()
        app.title('Recommended products')
        app.mainloop()

# heading of WIndow
heading = Label(root, text="Grocery Recommendation System", font=(
    'sans-serif', 50), bg="green" ,fg="white").place(x=140, y=150)
num = 0

# where user will enter the input field
search = Entry(root, font=("Helvetica", 20))
search.place(x=150, y=390, width=1000)

# Listbox  where all the list items will be shown
listbox = Listbox(root, width=166, height=30)
listbox.place(x=150, y=450)

# Logout button
logout = Button(root, bg="green", text="Logout", command=logout, font=(
    "times new roman", 15), padx=5, pady=2, bd=0).place(x=1800, y=5)

cmb_quest = ttk.Combobox(root,font=("times new roman",15),state="readonly",justify=CENTER)
cmb_quest.place(x=1160, y=390,height=35,width=100)
cmb_quest['values']  = ("Quantity","1","2","3","4","5")
cmb_quest.current(0)

# list of food items
listP = list(set([str(i)
                  for(i) in pd.read_csv('priceList.csv')['Product']]))

# update the list item from start
update(listP)

# get the current user info 

getCurrentUser()
user_name = user_values[0]
surname = user_values[1]
contact = user_values[2]

user_name = Label(root,text="Username: "+str(user_name),font=("times new roman",15,"bold"),bg="green")
user_name.place(x=1300,y=5)


# orderList =
Ordersummary = Label(root, text="Orders Summary ", font=(
    "times new roman", 20, "bold"), bg="green").place(x=1480, y=200)

# horizontal line
hr = Label(root, bg="black",).place(x=1480, y=255, width=400, height=2)

# total Amount
total = Label(root, text="Total Amount : ", font=(
    "times new roman", 15, "bold"), bg="green")
total.place(x=1480, y=265)

hr = Label(root, bg="black",).place(x=1480, y=300, width=400, height=2)


# add button
add = Button(root, text="ADD",font=("times new roman",15), bg="gray", padx=80,
             command=add, bd=0,fg="white").place(x=1160, y=500)

# Print bill Button 

# print_bill = Button(root,text="Print Bill",font=("times new roman",15,"bold"),fg="white",bg="gray",command=Printbill,bd = 0,padx=65)
# print_bill.place(x=1160,y=560)


recommend = Button(root,text="Recommend",font=("times new roman",15,"bold"),fg="white",bg="gray",command=recommendItems,bd = 0,padx=50)
recommend.place(x=1160,y=620)

submit = Button(root,text="Submit",font=("times new roman",15,"bold"),fg="white",bg="gray",command=Submit,bd = 0,padx=73)
submit.place(x=1160,y=680)

# create a binding on the  listbox onclick

listbox.bind("<<ListboxSelect>>", fillout)

search.bind("<KeyRelease>", check)


# root.attributes("fullscreen",True)
root.mainloop()
