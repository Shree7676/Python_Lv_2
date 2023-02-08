from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Tic Tac Toe")
window.config(bg="blue")


BTN_LIST=[]
PLAYER="O"
COMPUTER="X"
PLAYER_POINTS=0
COMPUTER_POINTS=0
DRAW=0
ROUNDS=3

def status(btn):
    temp=0
    for x in range(3):
        #Rows
        if BTN_LIST[temp]["text"]==BTN_LIST[temp+1]["text"]==BTN_LIST[temp+2]["text"]==btn["text"]:
            summary(BTN_LIST[temp]["text"])
        temp+=3

        #Column
        if BTN_LIST[x]["text"]== BTN_LIST[x+3]["text"] == BTN_LIST[x+6]["text"] == btn["text"]:
            summary(BTN_LIST[x]["text"])
        
        # Diagonal
        if BTN_LIST[x]["text"]== BTN_LIST[4]["text"] == BTN_LIST[8-x]["text"] == btn["text"] and x!= 1: 
            summary(BTN_LIST[4]["text"])
    else:
        for btn in BTN_LIST:
            if spaceIsFree(btn):
                return
        summary("draw")

def summary(winner):
    global PLAYER_POINTS,DRAW,COMPUTER_POINTS,ROUNDS
    # check if played 3 times
    if winner=="O":
        Label(Player1Frame,text=1,bg="green",font="arial 20 bold").pack()
        Label(Player2Frame,text=0,bg="red",font="arial 20 bold").pack()
        PLAYER_POINTS+=1
        ROUNDS-=1
    elif winner=="X":
        Label(Player1Frame,text=0,bg="green",font="arial 20 bold").pack()
        Label(Player2Frame,text=1,bg="red",font="arial 20 bold").pack()
        COMPUTER_POINTS+=1
        ROUNDS-=1
    elif winner=="draw":
        Label(Player1Frame,text=0,bg="green",font="arial 20 bold").pack()
        Label(Player2Frame,text=0,bg="red",font="arial 20 bold").pack()
        DRAW+=1
        ROUNDS-=1
    for btn in BTN_LIST:
        btn["text"]=""
        btn.config(bg="white")
    if ROUNDS==0:
        if PLAYER_POINTS>COMPUTER_POINTS:
            messagebox.showinfo("Game Over"," {} is winner".format(PLAYER))
        elif PLAYER_POINTS<COMPUTER_POINTS:
            messagebox.showinfo("Game Over"," {} is winner".format(COMPUTER))
        else:
            messagebox.showinfo("Game Over", "It was a Tie Good play")
        quit() # add a messagebox to reset or to quit depending on input
    print(ROUNDS)

def status_minimax(btn):
    temp=0
    for x in range(3):
        #Rows
        if BTN_LIST[temp]["text"]==BTN_LIST[temp+1]["text"]==BTN_LIST[temp+2]["text"]==btn["text"]:
            return BTN_LIST[temp]["text"]
        temp+=3

        #Column
        if BTN_LIST[x]["text"]== BTN_LIST[x+3]["text"] == BTN_LIST[x+6]["text"] == btn["text"]:
            return BTN_LIST[x]["text"]
        
        # Diagonal
        if BTN_LIST[x]["text"]== BTN_LIST[4]["text"] == BTN_LIST[8-x]["text"] == btn["text"] and x!= 1: 
            return BTN_LIST[4]["text"]

    for btn in BTN_LIST:
        if spaceIsFree(btn):
            return
    return "Draw"

def spaceIsFree(position):
    if position["text"]!="X" and position["text"]!="O":
        return True
    return False

def changeplr(p,btn):
    global PLAYER
    if p=="X":
        PLAYER="O"
        btn.config(bg="red")
    elif p=="O":
        PLAYER="X"
        btn.config(bg="green")

def minimax(board, isMaximizing,btn):
    if status_minimax(btn)==PLAYER:
        return -1
    elif status_minimax(btn)==COMPUTER:
        return 1
    elif status_minimax(btn)=="Draw":
        return 0

    if isMaximizing:
        bestScore = -800
        for btn in BTN_LIST:
            if spaceIsFree(btn):
                btn["text"]=COMPUTER
                score=minimax(board,False,btn)
                btn["text"]=""
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for btn in BTN_LIST:
            if spaceIsFree(btn):
                btn["text"]=PLAYER
                score=minimax(board,True,btn)
                btn["text"]=""
                if (score < bestScore):
                    bestScore = score
        return bestScore


def computer_move():
    bestScore = -800
    bestMove = ""  # if player wants to go first then need to change
    for btn in BTN_LIST:
        if spaceIsFree(btn):
            btn["text"]=COMPUTER
            score=minimax(BTN_LIST,False,btn)
            btn["text"]=""
            if (score > bestScore):
                bestScore = score
                bestMove = btn
    if bestMove!="":
        bestMove["text"]=COMPUTER
        bestMove.config(bg="RED")
        status(bestMove)


def fnc(event):
    a=rvar.get()
    if a=="singleplayer" or a=="multiplayer":
        btn=event.widget
        if spaceIsFree(btn):
            btn["text"] = PLAYER
            if a=="multiplayer":
                changeplr(PLAYER,btn)  # better way is to have 2 players
                status(btn)
            else:
                btn.config(bg="green")
                computer_move()

        else:
            messagebox.showinfo("Alert","Please select valid position")
    else:
        messagebox.showinfo("Game Mode","Please select the game mode")

for x in range(3):
    for y in range(3):
        b=Button(window,width=22,height=8)
        b.config(command=lambda event=b:status(event))
        b.grid(row=x,column=y,pady=5,padx=5)
        b.bind("<Button-1>",fnc)
        BTN_LIST.append(b)

lFrame=LabelFrame(window,text="DASHBOARD",bg="light blue",bd=8,font="lucida 15 bold underline",foreground="purple")
lFrame.grid(row=0,rowspan=3,column=3,padx=5,pady=5)

rvar=StringVar()
rvar.set(None)
Radiobutton(lFrame,text="MULTI-PLAYER",font="lucida 10 bold",foreground="black",bg="light blue",value="multiplayer",variable=rvar).grid(row=0,column=0,columnspan=2)
Radiobutton(lFrame,text="SINGLE-PLAYER",font="lucida 10 bold",foreground="black",bg="light blue",value="singleplayer",variable=rvar).grid(row=1,column=0,columnspan=2)

Player1Frame=LabelFrame(lFrame,text="Player1",bg="green",font="lucida 10 bold underline",width=90,height=200,bd=4)
Player1Frame.propagate(False)
Player1Frame.grid(row=2,column=0,padx=5,pady=5)

Player2Frame=LabelFrame(lFrame,text="Player2",bg="red",font="lucida 10 bold underline",width=90,height=200,bd=4)
Player2Frame.propagate(False)
Player2Frame.grid(row=2,column=1,padx=5,pady=5)

window.mainloop()