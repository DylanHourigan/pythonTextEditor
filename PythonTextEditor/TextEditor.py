import sys
import os
from tkinter import *
from tkinter import filedialog

dir_path = os.path.dirname(os.path.realpath(__file__))
root = Tk("Text Editor")
root.title("Text Editor")
root.iconbitmap("icon.ico")
root.configure(bg="#FFFFFF")
text = Text(root)
text.pack(side="top", fill="both", expand=True)
text.configure(bg="#FFFFFF",fg="#000000")

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
def backgroundWhite():
    root.configure(bg="#FFFFFF")
    text.configure(fg="#FFFFFF")
def backgroundBlack():
    root.configure(bg="#000000")
    text.configure(fg="#FFFFFF")
def backgroundBlue():
    root.configure(bg="#001899")
    text.configure(fg="#FFFFFF")

def changeColour(colour):
    if(colour == "White"):
        root.configure(bg="#FFFFFF")
        text.configure(bg="#FFFFFF")
        text.configure(fg="#000000")
    elif(colour == "Black"):
        root.configure(bg="#000000")
        text.configure(bg="#000000")
        text.configure(fg="#FFFFFF")
    elif(colour == "Blue"):
        root.configure(bg="#001899")
        text.configure(bg="#001899")
        text.configure(fg="#FFFFFF")
    else:
        root.configure(bg="#FFFFFF",fg="#000000")
        

button = Button(root, text="Save", command=saveAs)
button.pack(side="left")
button2 = Button(root, text="Open", command=openFile)
button2.pack(side="left")

#drop down box
clicked = StringVar()
clicked.set("White")

drop = OptionMenu(root, clicked, "White", "Black", "Blue", command= changeColour)
drop.pack(side="right")

# background = Menubutton(root, text="Background Colour")
# menu=Menu(root, tearoff=0)
# background.config(menu=menu)
# whitebg = IntVar()
# blackbg = IntVar()
# bluebg = IntVar()
# menu.add(label="White", command=backgroundWhite, itemType="checkbutton")
# menu.add(label="Black", command=backgroundBlack, itemType="checkbutton")
# menu.add(label="Blue", command=backgroundBlue, itemType="checkbutton")
# background.pack(side="left")

exitbutton = Button(root, text="Exit", command=root.destroy)
exitbutton.pack(side="left")
root.mainloop()