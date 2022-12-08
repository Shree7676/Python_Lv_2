# Home work

"""
Chirag had created a program in python to check the typing speed.
But he wants to improve his program and wants to make it much better in terms of GUI.
Write a program in python to create a GUI application to find the typing speed with accuracy.
"""
from tkinter import *
import time
import random

WORDS=50

root=Tk()
root.title("Typing Speed")
root.geometry("900x900")

TR=LabelFrame(root,text="Track record",font="lucida 20 bold",height=750,width=250,pady=10,padx=5)
TR.place(x=550)
TR.propagate(0)
Psg=LabelFrame(root,text="Passage",font="lucida 20 bold",height=300,width=550,pady=5,padx=10)
Psg.propagate(0)
Psg.place(x=0,y=0)
Typ=LabelFrame(root,text="Type Here",font="lucida 20 bold",height=550,width=550,pady=5,padx=10)
Typ.place(x=0,y=300)

txt = ""


def pasg():
    global txt,txtvar
    if "unpack"=="input":
        inp=input("Please paste your passage")   #radio btn
        for x in range(len(txt)):
            if x%5==0:
                txt = txt + inp + "\n"
            else:
                txt = txt + inp + " "
    else:
        file = open("random word", "r")
        a = file.read()
        for x in range(WORDS):
            r = random.choice(a.split(" "))
            if x%5==0:
                txt = txt + r + "\n"
            else:
                txt = txt + r + " "
    txtvar.set(txt)



txtvar=StringVar()
txtvar.set(txt)
display_txt=Label(Psg,textvariable=txtvar,font="arial 10 bold")
display_txt.pack()
b=Button(TR,text="Change Text",command=pasg)
b.pack(side=BOTTOM,anchor="e")
pasg()
root.mainloop()


"""
Himanshi wants to create a guess the number game. 
The game should generate a random number and then the user has to 
guess the number in minimum chance. Each time user will guess an incorrect number, 
the score will be decreased by one point out of a hundred. Also, after each incorrect 
guess the game will give one hint like: TRY SMALLER NUMBER or TRY BIGGER NUMBER. 
Create a GUI program for the same.
The sample run of the program is given below:
Guess the number: 30
TRY BIGGER NUMBER
Guess the number: 80
TRY SMALLER NUMBER
Guess the number: 70
TRY BIGGER NUMBER
Guess the number: 74
YOU GOT IT! in 3 extra attempts
YOUR SCORE: 97
"""