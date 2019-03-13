# from func import *
import sqlite3
# import tkinter
import tkinter.Tk as Tk

conn = sqlite3.connection("chess.db")

root = Tk()
root.title('Bowling Average Calculator')
root.geometry('275x175')
app = Application(root)
app.mainloop()
