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