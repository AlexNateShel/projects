import os
from tkinter import * 
import tkinter as tk


def shutdown():
    os.system("shutdown /s")

def restart():
    os.system("shutdown /r")

def logout():
    os.system("shutdown /l")

# Create an instance of tkinter frame or window
root = Tk()
# Set the size of the tkinter window
root.geometry("700x350")
root.title("PC Controls")#give title to the window
head = Label(root, text="Shutdown, Restart and Logout Using Python", width=50, font=('Calibri 15'))
head.place(x=80, y=10)

# Creating Buttons
Button(root, text='Shutdown', command=shutdown, width=20, font=('Normal', 11), bg='Red').place(x=250, y=50)

Button(root, text='Restart', command=restart, width=20, font=('Normal', 11), bg='Red').place(x=250, y=100)

Button(root, text='Logout', command=logout, width=20,  font=('Normal', 11), bg='Red').place(x=250, y=150)


root.update()
root.mainloop()