
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