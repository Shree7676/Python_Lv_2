#Class work

"""
Ayman and his other friends planned to play cricket.
They tossed a coin to decide between batting and balling.
Ayman got an idea to create a virtual coin in python GUI programming.
He created a GUI program with a button toss and each time he clicks the button
he gets a random side of the coin. Create the same program and toss the coin.
"""
from tkinter import *
import random

root=Tk()
root.title("Toss")
root.geometry("200x200")
root.config(bg="light blue")

head=PhotoImage(file="Head.png")
tail=PhotoImage(file="Tail.png")
toss=PhotoImage(file="Toss.png")
list=[head,tail]

a=Label(root,image=toss,bg="light blue")
a.pack(padx=10,pady=10)

def Toss():
    global a,list,head,tail
    result=random.choice(list)
    a.config(image=result)

Button(root,text="TOSS",font="lucida 10 bold",command=Toss).pack(padx=10,pady=10)
root.mainloop()

"""
Shaurya plays tic tac toe ( X O ) on the last page of his notebook. 
One day he thought to create a board for this game using the python Tkinter module. 
He was able to create the board successfully and played the game with his friends as well. 
Write a program to create a python GUI ( X O ) board and play with your friends.
"""

from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Tic Tac Toe")
root.config(bg="light blue")

player="X"
def update(event):
    global player

    a=event.widget
    if event.widget["text"]=="":a.config(text=player)
    if player=="X":
        player="Y"
    elif player=="Y":
        player="X"

    check_status()
count=0    # to check tie condition if > then 9 tie
def check_status():
    global count
    count+=1
    if count==9:
        game_over("Tie")

    #diagonal   048   246
    if list[0]["text"]==list[4]["text"]==list[8]["text"]!="":
        list[0].config(bg="green")
        list[4].config(bg="green")
        list[8].config(bg="green")
        game_over(list[4]["text"])
    elif list[2]["text"]==list[4]["text"]==list[6]["text"]!="":
        list[2].config(bg="green")
        list[4].config(bg="green")
        list[6].config(bg="green")
        game_over(list[4]["text"])

    start_rows=0
    start_column=0
    for x in range(3):
    # rows       012   345     678
        if list[start_rows]["text"] == list[start_rows+1]["text"] == list[start_rows+2]["text"] != "":
            list[start_rows].config(bg="green")
            list[start_rows+1].config(bg="green")
            list[start_rows+2].config(bg="green")
            game_over(list[start_rows]["text"])
    #column      036   147     258
        elif list[start_column]["text"] == list[start_column + 3]["text"] == list[start_column + 6]["text"] != "":
            list[start_rows].config(bg="green")
            list[start_rows+3].config(bg="green")
            list[start_rows+6].config(bg="green")
            game_over(list[start_column]["text"])
        start_rows += 3
        start_column += 1

def game_over(txt):
    global count
    if txt!="Tie":a=messagebox.askquestion(f"{txt} won the match","Want to replay?")
    else:
        a=messagebox.askquestion("Its tie ","Do you want to restart?")
    if a=="yes":
        count=0
        create_btn()
    else:
        root.quit()

list=[] #a list which stores variable name
def create_btn():
    r = c = 1
    for x in range(1,10):
        list.append(Button(root)) #variables are getting stored
        #latest appended btn ... its in flow so btn created then config,bind...& then repeat with next new btn
        list[x-1].config(text="",height=10,width=20,font="lucida 10 bold",bg="light blue")
        list[x-1].bind("<Button-1>",update)
        list[x-1].grid(row=r,column=c)
        c+=1
        if c==4 and r==1:
            c,r=1,2
        elif c==4 and r==2:
            c,r=1,3
create_btn()
root.mainloop()