from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title('Rock Paper Scissors Game')
root.config(bg='seashell3')

Label(root, text='Rock Paper Scissors', font='arial 20 bold', bg='seashell2').pack()

user_input = StringVar()
Label(root, text='Choose any one: rock, paper, scissors', font='arial 16 bold').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_input, bg='antiquewhite2').place(x=90, y=130)

# Computer choice
computer_pick = random.randint(1, 3)
match computer_pick:
    case 1:
        computer_pick = 'rock'
    case 2:
        computer_pick = 'paper'
    case _:
        computer_pick = 'scissors'

# Start the game
Result = StringVar()
def Play():
    user = user_input.get()
    if user == computer_pick:
        Result.set('tie, you both select same')
    elif user == 'rock' and computer_pick == 'paper':
        Result.set('you loose, computer picks paper')
    elif user == 'rock' and computer_pick == 'scissors':
        Result.set('you win, computer picks scissors')
    elif user == 'paper' and computer_pick == 'scissors':
        Result.set('you loose, computer picks scissors')
    elif user == 'paper' and computer_pick == 'rock':
        Result.set('you win, computer picks rock')
    elif user == 'scissor' and computer_pick == 'rock':
        Result.set('you loose, computer picks rock')
    elif user == 'scissor' and computer_pick == 'paper':
        Result.set('you win, computer picks rock')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

# Reset
def Reset():
    Result.set('')
    user_input.set('')

# Exit
def Exit():
    root.destroy()

Entry(root, font='arial 10 bold', textvariable=Result, bg='antiquewhite2', width=50,).place(x=25, y=250)
Button(root, font='arial 12 bold', text='Play', padx=5, bg='seashell4', command=Play).place(x=150, y=190)
Button(root, font='arial 12 bold', text='Reset', padx=5, bg='seashell4', command=Reset).place(x=70, y=310)
Button(root, font='arial 12 bold', text='Exit', padx=5, bg='seashell4', command=Exit).place(x=230, y=310)

root.mainloop()