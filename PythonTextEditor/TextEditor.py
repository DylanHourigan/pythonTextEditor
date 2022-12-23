import sys
import os
from tkinter import *
from tkinter import filedialog

#Finds the directory path for files stored in the project. I used this for the inital directory when opening or saving text files.
dir_path = os.path.dirname(os.path.realpath(__file__))

#creates the window
root = Tk("Text Editor")
root.title("Text Editor")
root.iconbitmap("icon.ico")
root.configure(bg="#FFFFFF")

#creates the text box
text = Text(root)
text.pack(side="top", fill="both", expand=True)
text.configure(bg="#FFFFFF",fg="#000000")

#Save Button function
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

#open button function
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

#background color option menu function
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
        
#Save Button
button = Button(root, text="Save", command=saveAs)
button.pack(side="left")

#Open Button
button2 = Button(root, text="Open", command=openFile)
button2.pack(side="left")

#drop down box
clicked = StringVar()
clicked.set("White")

drop = OptionMenu(root, clicked, "White", "Black", "Blue", command= changeColour)
drop.pack(side="right")

#Exit Button
exitbutton = Button(root, text="Exit", command=root.destroy)
exitbutton.pack(side="left")


root.mainloop()