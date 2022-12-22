import sys
import os
from tkinter import *
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Tk("Text Editor")
root.title("Text Editor")
root.iconbitmap("icon.ico")
text = Text(root)
text.pack(side="top", fill="both", expand=True)

def saveAs():
    global text
    t = text.get("1.0", "end-1c")

    try:
        saveLocation = filedialog.asksaveasfilename(initialdir= dir_path, title="Save Text File", filetypes= (("Text Files", "*.txt"),))
        file1 = open(saveLocation, 'w')
        file1.write(t)
    except Exception as e:
        # handle the exception
        print("An error occurred:", e)
    finally:
        # close the file regardless of whether an exception occurred
        file1.close()

def openFile():
    try:
        openLocation = filedialog.askopenfilename(initialdir= dir_path, title="Open Text File", filetypes= (("Text Files", "*.txt"),))
        file1 = open(openLocation, 'r')
        text.insert("1.0", file1.read())
    except Exception as e:
        # handle the exception
        print("An error occurred:", e)
    finally:
        # close the file regardless of whether an exception occurred
        file1.close()


button = Button(root, text="Save", command=saveAs)
button.pack(side="left")
button2 = Button(root, text="Open", command=openFile)
button2.pack(side="left")
exitbutton = Button(root, text="Exit", command=root.destroy)
exitbutton.pack(side="left")
root.mainloop()