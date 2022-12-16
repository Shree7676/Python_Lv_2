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
def chng_word():
    file=open("random word","r")
    data=file.read()
    que=random.choice(data.split(" "))
    a = ans.get()
    words.set(que)
    submit(que)

def submit(q):
    global ans

    a=ans.get()
    print(a)
    print(q)
    if a==q:
        print("1")
        ans.set("")


words=StringVar()
ans=StringVar()

txt=Label(root,textvariable=words,font="lucida 20 bold")
txt.pack()

enter=Entry(root,textvariable=ans,font="lucida 20 bold")
enter.pack()
enter.bind("<Return>",lambda event:chng_word())


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