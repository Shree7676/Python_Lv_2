from tkinter import *
from tkinter import messagebox

window=Tk()
window.title("Tic Tac Toe")
window.config(bg="blue")


BTN_LIST=[]
PLAYER="O"
COMPUTER="X"

def status(btn):
    temp=0
    for x in range(3):
        #Rows
        if BTN_LIST[temp]["text"]==BTN_LIST[temp+1]["text"]==BTN_LIST[temp+2]["text"]==btn["text"]:
            messagebox.showinfo("Game Over"," {} is winner".format(BTN_LIST[temp]["text"]))
            quit()
        temp+=3

        #Column
        if BTN_LIST[x]["text"]== BTN_LIST[x+3]["text"] == BTN_LIST[x+6]["text"] == btn["text"]:
            messagebox.showinfo("Game Over"," {} is winner".format(BTN_LIST[x]["text"]))
            quit()
        
        # Diagonal
        if BTN_LIST[x]["text"]== BTN_LIST[4]["text"] == BTN_LIST[8-x]["text"] == btn["text"] and x!= 1: 
            messagebox.showinfo("Game Over"," {} is winner".format(BTN_LIST[4]["text"]))
            quit()

    for btn in BTN_LIST:
        if spaceIsFree(btn):
            return
    messagebox.showinfo("Game Over", "It was a Tie Good play")
    quit()


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

def changeplr(p):
    global PLAYER
    if p=="X":
        PLAYER="O"
    elif p=="O":
        PLAYER="X"

def minimax(board, depth, isMaximizing,btn):
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
                score=minimax(board, depth + 1,False,btn)
                btn["text"]=""
                if (score > bestScore):
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for btn in BTN_LIST:
            if spaceIsFree(btn):
                btn["text"]=PLAYER
                score=minimax(board, depth + 1,True,btn)
                btn["text"]=""
                if (score < bestScore):
                    bestScore = score
        return bestScore
        

def computer_move():
    bestScore = -800
    bestMove = BTN_LIST[0]  # if player wants to go first then need to change
    for btn in BTN_LIST:
        if spaceIsFree(btn):
            btn["text"]=COMPUTER
            score=minimax(BTN_LIST,0,False,btn)
            btn["text"]=""
            if (score > bestScore):
                bestScore = score
                bestMove = btn
    bestMove["text"]=COMPUTER


def fnc(event):
    btn=event.widget
    if spaceIsFree(btn):
        btn["text"] = PLAYER
        # IF MULTIPLAYER():
        if MODE:
            changeplr(PLAYER)
        # ELSE >> COMPUTER MOVE
        else:
            computer_move()

    else:
        messagebox.showinfo("Alert","Please select valid position")

for x in range(3):
    for y in range(3):
        b=Button(window,width=22,height=8)
        b.config(command=lambda event=b:status(event))
        b.grid(row=x,column=y,pady=5,padx=5)
        b.bind("<Button-1>",fnc)
        BTN_LIST.append(b)
MODE=messagebox.askyesno("GAME MODE","DO YOU WANT TO PLAY MULTIPLAYER")

window.mainloop()