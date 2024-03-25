from tkinter import *
import random

def urmatoare_mutare(randuri, coloane):
    global jucator

    if buttons[randuri][coloane]['text'] == "" and verifica_castigator() is False:
        buttons[randuri][coloane]['text'] = jucator

        if verifica_castigator() is True:
            label.config(text=(jucator + " Castigator"))
        elif verifica_castigator() == "Egalitate":
            label.config(text="Egalitate")
        else:
            jucator = players[1] if jucator == players[0] else players[0]
            label.config(text=(jucator + " mutare"))

def verifica_castigator():
    for randuri in range(3):
        if buttons[randuri][0]['text'] == buttons[randuri][1]['text'] == buttons[randuri][2]['text'] != "":
            buttons[randuri][0].config(bg="green")
            buttons[randuri][1].config(bg="green")
            buttons[randuri][2].config(bg="green")
            return True

    for coloane in range(3):
        if buttons[0][coloane]['text'] == buttons[1][coloane]['text'] == buttons[2][coloane]['text'] != "":
            buttons[0][coloane].config(bg="green")
            buttons[1][coloane].config(bg="green")
            buttons[2][coloane].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    if not spatii_goale():
        for randuri in range(3):
            for coloane in range(3):
                buttons[randuri][coloane].config(bg="yellow")
        return "Egalitate"
    return False

def spatii_goale():
    for randuri in range(3):
        for coloane in range(3):
            if buttons[randuri][coloane]['text'] == "":
                return True
    return False

def joc_nou():
    global jucator

    jucator = random.choice(players)
    label.config(text=jucator + " mutare")

    for randuri in range(3):
        for coloane in range(3):
            buttons[randuri][coloane].config(text="", bg="#F0F0F0")

window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
jucator = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

label = Label(window, text=jucator + " mutare", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(window, text="restart", font=('consolas', 20), command=joc_nou)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for randuri in range(3):
    for coloane in range(3):
        buttons[randuri][coloane] = Button(frame, text="", font=('consolas', 40), width=5, height=2,command=lambda randuri=randuri, coloane=coloane: urmatoare_mutare(randuri, coloane))
        buttons[randuri][coloane].grid(row=randuri, column=coloane)

window.mainloop()
