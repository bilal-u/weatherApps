#
import tkinter as tk
from tkinter import ttk

# initialize variables //
balance = 0.0
drink_chosen = ""

# define functions

def Latte():
    global drink_chosen
    drink_chosen = "Latte"
    choose_drink.set("")
def Expresso():
    global drink_chosen
    drink_chosen = "Expresso"
    choose_drink.set("")

def Cappuccino():
    global drink_chosen
    drink_chosen = "Cappuccino"
    choose_drink.set("")

def make_drink():
    global drink_chosen
    global balance
    if drink_chosen != "":
        if drink_chosen == "Latte":
            if balance >= 2.50:
                balance = balance - 2.5
                message_box.set("Enjoy your Drink!")
                choose_drink.set(drink_chosen)
                balance_box.set('${:.2f}'.format(balance))
            else:
                message_box.set("Insufficient fund.")
        if drink_chosen == "Expresso":
            if balance >= 1.50:
                balance = balance - 1.5
                message_box.set("Enjoy your Drink!")
                choose_drink.set(drink_chosen)
                balance_box.set('${:.2f}'.format(balance))
            else:
                message_box.set("Insufficient fund.")
        if drink_chosen == "Cappuccino":
            if balance >= 3.00:
                balance = balance - 3.0
                message_box.set("Enjoy your Drink!")
                choose_drink.set(drink_chosen)
                balance_box.set('${:.2f}'.format(balance))
            else:
                message_box.set("Insufficient fund.")
    else:
         message_box.set("Please choose a drink!")

def add_two():
    global balance
    balance += 2
    balance_box.set('${:.2f}'.format(balance))
    
def add_one():
    global balance
    balance += 1
    balance_box.set('${:.2f}'.format(balance))
    
def add_quarter():
    global balance
    balance += 0.25
    balance_box.set('${:.2f}'.format(balance))

# Create the root window
root = tk.Tk()
root.title('Coffee Machine!')
root.geometry('500x300')
root.geometry('700x300')


# Create the main frame
frame_home = ttk.Frame(root)
frame_home.pack(fill=tk.BOTH, expand=True)


# Create a label
ttk.Label(frame_home, text="Coffee Maker").grid(row=0, column=2)

# create buttons
# 1st row 
button1=ttk.Button(frame_home, text="Latte($2.50)",command = lambda: Latte()).grid(row=1,column=0)
button2=ttk.Button(frame_home, text="Expresso($1.50)", command = lambda: Expresso()).grid(row=1,column=2,columnspan=2)
button3=ttk.Button(frame_home, text="Cappuccino($3.00)", command = lambda: Cappuccino()).grid(row=1,column=4,columnspan=2)
#button1.grid(row=1,column=0)

# 2nd row
add2=ttk.Button(frame_home, text="$2.00", command = lambda: add_two()).grid(row=2,column=0)

add1=ttk.Button(frame_home, text="$1.00", command = lambda: add_one()).grid(row=2,column=2)
add_25=ttk.Button(frame_home, text="$0.25", command = lambda: add_quarter()).grid(row=2,column=4)

# Create an entry box
balance_box = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=balance_box, state='readonly').grid(row=3,column=2)

choose_drink = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=choose_drink, state='readonly').grid(row=4,column=2)
#ttk.Button(frame_home, text='Save', command=submit_action).grid(column=0, row=3, columnspan=10)

# button make drink

button1=ttk.Button(frame_home, text="Make Drink",command = lambda: make_drink()).grid(row=5,column=2)

# Create an entry box
message_box = tk.StringVar()
ttk.Entry(frame_home, width=30, textvariable=message_box,state='readonly').grid(row=6,column=2)

root.mainloop()
