
from tkinter import *
from tkinter import messagebox
from random import randint

root = Tk()
root.title("Tic Tac Toe")
root.resizable(False,False)
root.config(bg="black")

Player = "X"
Other = "O"
buttons = []


def checkWin(turn):
    global buttons
    for i in range(3):
        if buttons[i*3]["text"] == turn and buttons[(i*3)+1]["text"] == turn and buttons[(i*3)+2]["text"] == turn:
            print(f"\n------------------------ WIN {turn} Row ------------------------\n")
            quit()
        if buttons[i]["text"] == turn and buttons[i+3]["text"] == turn and buttons[i+6]["text"] == turn:
            print(f"\n------------------------ WIN {turn} Column ------------------------\n")
            quit()

    if  (buttons[4]["text"] == turn and buttons[0]["text"] == turn and buttons[8]["text"] == turn) or (buttons[4]["text"] == turn and buttons[6]["text"] == turn and buttons[2]["text"] == turn):   
        print(f"\n------------------------ WIN {turn} Diaganol ------------------------\n")
        quit()
    if checkDraw():
        print("hiiiiii")
        quit()
    return False


def checkWin_mini(turn):
    global buttons
    for i in range(3):
        if buttons[i*3]["text"] == turn and buttons[(i*3)+1]["text"] == turn and buttons[(i*3)+2]["text"] == turn:
            print(f"\n------------------------ WIN {turn} Row ------------------------\n")
            return True
        if buttons[i]["text"] == turn and buttons[i+3]["text"] == turn and buttons[i+6]["text"] == turn:
            print(f"\n------------------------ WIN {turn} Column ------------------------\n")
            return True

    if  (buttons[4]["text"] == turn and buttons[0]["text"] == turn and buttons[8]["text"] == turn) or (buttons[4]["text"] == turn and buttons[6]["text"] == turn and buttons[2]["text"] == turn):   
        print(f"\n------------------------ WIN {turn} Diaganol ------------------------\n")
        return True

    return False


def checkDraw():
    for i in buttons:
        if i["text"] == "":
            print(i["text"])
            return False
    print("\n------------------------ DRAW ------------------------\n")
    return True


def miniMax(buttons, isMaximizing):
    if checkWin_mini(Player):
        return -1
    elif checkWin_mini(Other):
        return 1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -1000
        for button in buttons:
            if (button["text"] == Other) or (button["text"] == Player):
                continue
            button["text"] = Other
            score = miniMax(buttons, False)
            button["text"] = ""
            if score > bestScore:
                bestScore = score
        return bestScore

    else:
        bestScore = 1000
        for button in buttons:
            if (button["text"] == Other) or (button["text"] == Player):
                continue
            button["text"] = Other
            score = miniMax(buttons, True)
            button["text"] = ""
            if score < bestScore:
                bestScore = score
        return bestScore

def compTurn():

    bestScore = -1000
    bestMove = None
    for button in buttons:
        if (button["text"] == Other) or (button["text"] == Player):
            continue
        button["text"] = Other
        score = miniMax(buttons, True)
        button["text"] = ""
        if score > bestScore:
            bestMove = button
            bestScore = score
    if bestMove!=None:
        bestMove["text"] = Other
        checkWin(Other)
        checkDraw()

def nextTurn():
    if mb:
        compTurn()
    else:
        global Player
        global Other

        Player = "O" if Player == "X" else "X"
        Other = "X" if Player == "O" else "O"

def playerTurn(event):
    
    button = event.widget

    if button["text"] != Other and button["text"] != Player:
        button["text"] = Player
        checkWin(Player)
        checkDraw()
        nextTurn()

for row in range(3):
    for column in range(3):
        b = Button(root, width=7, height=3, font="Georgia 25", text="")
        b.propagate(0)
        b.grid(column=column, row=row, padx=2, pady=2)
        b.bind("<Button-1>", playerTurn)
        buttons.append(b)

mb = messagebox.askyesno("Gamemode", "Do you want to play SinglePlayer?")

root.mainloop()