#! /usr/bin/python
import os
import subprocess as s
from tkinter import *
import tkinter as tk
import threading
temp = 0
def readTemp():
    global temp
    while True:
        cmd = ["sensors"]
        output = str(s.Popen( cmd, stdout=s.PIPE ).communicate()[0])
        dat = output.find("CPU")
        temp = float(output[dat+17:dat+21])
        if (temp >= 50) and (temp < 60):
            l.configure(fg = "orange")
        elif temp >= 60:
            l.configure(fg = "red")
        else:
            l.configure(fg = "green")

        os.system("sleep 1")
def labelUpdate(l):
    while True:
        l.configure(text = str(temp))
        os.system("sleep 1")

root = Tk()
root.geometry("63x30")
root.resizable(0,0)
root.title("TM")

l = Label(root, text = str(temp) )
l.config(font = ("Bahnschrift", 20), bg='#000', fg = "blue")
l.pack()
t = threading.Thread(target = readTemp)
t1 = threading.Thread(target = labelUpdate,args = (l,))
t.start()
t1.start()
root.wm_attributes('-topmost', 'True')
tk.mainloop()
