import sys
import os
from tkinter import *
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Tk("Text Editor")
root.title = dir_path
text = Text(root)
text.grid()

def saveAs():
    global text
    t = text.get("1.0", "end-1c")
    saveLocation = filedialog.asksaveasfilename(initialdir= dir_path, title="Save Text File", filetypes= (("Text Files", "*.txt"),))
    file1=open(saveLocation,'w')
    file1.write(t)
    file1.close()

def openFile():
    openLocation = filedialog.askopenfilename(initialdir= dir_path, title="Open Text File", filetypes= (("Text Files", "*.txt"),))
    file1=open(openLocation,'r')
    text.insert("1.0", file1.read())


button = Button(root, text="Save", command=saveAs)
button.grid()
button2 = Button(root, text="Open", command=openFile)
button2.grid()
root.mainloop()