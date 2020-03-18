# Import packages we know are here and won't mess anything up
import sys
try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    try:
        from Tkinter import *
        from Tkinter import ttk
    except ImportError:
        # If no versions of tkinter exist (most likely linux) provide a message
        if sys.version_info.major < 3:
            print("Error: Tkinter not found")
            print('For linux, you can install Tkinter by executing: "sudo apt-get install python-tk"')
            sys.exit(1)
        else:
            print("Error: tkinter not found")
            print('For linux, you can install tkinter by executing: "sudo apt-get install python3-tk"')
            sys.exit(1)

import functions as fn
from subprocess import call
# Functions but most of other funcs are in a methods.py in the same folder.

class Main:  # Main class.
    def __init__(self):
        root = self.root = Tk()  # Init for main window.
        root.title(" - Kaz TransLit")
        root.configure(background="#f16161")

        # Row 0
        # Photo
        logo = PhotoImage(file="images/KTL_logo.png")
        lbl = Label(root, image=logo, bg="#f16161").grid(row=0, column=0, pady=5, padx =0, sticky=NW)
        #btn frame
        btnframe = Frame(root, bg="#f16161")
        btnframe.grid(row=0, column=1,pady = 5, sticky=N) # Toolbar on top of the window.
        faq_btn = Button(btnframe, text="FAQ", command=fn.faqKTL, font="none 12",bg="#EF4A4A", width=10, height=1)
        faq_btn.grid(row=0, column=0, pady=5, padx = 10, sticky=NW)
        man_btn = Button(btnframe, text="Manual", command=fn.manualKTL, font="none 12",bg="#EF4A4A", width=10, height=1)
        man_btn.grid(row=0, column=1, pady=5, padx = 10, sticky=NW)
        cnt_btn = Button(btnframe, text="Contant Me", command=fn.contactKTL, font="none 12", bg="#EF4A4A", width=10, height=1)
        cnt_btn.grid(row=0, column=2, pady=5, padx = 10, sticky=NW)

        # Row 1
        lbl = Label(root, text="KazTransLit", bg="#f16161", fg="white", font="Bahnschrift 12 bold")
        lbl.grid(row=1, column=0, padx=10, pady=5, sticky=SW)
        btn = Button(root, text="Document to Text", command=fn.documentKTL, font="none 12", bg="#EF4A4A", width=20, height=5)
        btn.grid(row=1, column=1, padx=10, pady=5, sticky=E)
        btn = Button(root, text="Real Time Transliteration", command=fn.realtimeKTL, font="none 12", bg="#EF4A4A", width=20, height=5)
        btn.grid(row=1, column=2, padx=10, pady=5, sticky=E)

        # Row 2
        btn = Button(root, text="Settings", command = fn.settingsKTL, font="none 12", bg="#EF4A4A", width=20, height=5)
        btn.grid(row=2, column=2, padx=10, pady=5, sticky=E)
        lbl = Label(root, text="Transliteration on a whole 'nother level", bg="#f16161", fg="white", font="Bahnschrift 12")
        lbl.grid(row=2, column=0, padx=10, pady=5, sticky=N)
        # Exit
        btn = Button(root, text="EXIT", font="none 10", bg="#FF4C4C", width=20, height=5, command=self.close_root)
        btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

        root.resizable(0, 0)
        root.iconbitmap('images/KTL_logo.ico')
        root.mainloop()

    def close_root(self):  # Kill func.
        self.root.destroy()
        exit()
Main()

#colors
#EF4A4A 5% shade for f16161
#f16161 main color light red
#FF4C4C darker shade of f16161 for exit buttons
