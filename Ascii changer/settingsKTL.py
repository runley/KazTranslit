#imports
import functions as fn
from tkinter import *
from tkinter import ttk
try:
    from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename
except ImportError:
    from tkFileDialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename

def settingsKTL(): #settings toplevel to show the settings
    settingsKTL = Toplevel(bg = "#f16161")
    settingsKTL.title(' - Settings')

    #row 0
    logotxt = Label(settingsKTL, text="KazTranslit", bg="#f16161", fg="white",font="Bahnschrift 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #close top
    btn = Button(settingsKTL, command = lambda: fn.exit_btn(settingsKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    settingsKTL.iconbitmap('images/KTL_logo.ico')
    settingsKTL.resizable(0, 0)
