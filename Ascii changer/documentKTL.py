#imports
import functions as fn
from tkinter import *
from tkinter import ttk
try:
    from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename
except ImportError:
    from tkFileDialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename



def documentKTL(): #top level func to create a new window as Toplevel
    docKTL = Toplevel(bg = "#f16161")
    docKTL.title('Document to Text - KTL')

    #row 0
    logotxt = Label(docKTL, text="TransKazLit", bg="#f16161", fg="white",font="Bahnschrift 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    btn = Button(docKTL, text="Choose a file", command=fn.askFile, font="none 14", bg="#EF4A4A", fg="white", width=12, height=1)
    btn.grid(row=1, column=0, padx=5, pady=5, sticky=SW)
    consoleUI = Text(docKTL, height = 20, width = 50) #consoleUI element
    consoleUI.grid(row=1, column=1, pady = 5, padx = 5, columnspan=2, rowspan=5)

    #row 2
    btn = Button(docKTL, text="Choose a save location", command=fn.askSave, font="none 14", bg="#EF4A4A", fg="white", width=20, height=1)
    btn.grid(row=2, column=0, padx=5, pady=5, sticky=NW)

    #row 3
    btn = Button(docKTL, text="Go", font="none 14", bg="#EF4A4A", fg="white", width=4, height=1)#add command= later at some point
    btn.grid(row=3, column=0, padx=5, pady=5, sticky=NW)

    #close window
    btn = Button(docKTL, command = lambda: fn.exit_btn(docKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    docKTL.iconbitmap('images/KTL_logo.ico')
    docKTL.resizable(0, 0)
