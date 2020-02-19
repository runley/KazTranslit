from tkinter import *
from tkinter import ttk
import functions as fn
from subprocess import call
# Functions but most of other funcs are in a methods.py in the same folder.

class Main:  # Main class.
    def __init__(self):
        root = self.root = Tk()  # Init for main window.
        root.title("KTL - Kaz TransLit")
        root.configure(background="#f16161")

        # Row 0
        # Photo
        logo = PhotoImage(file="images/TK_logo.png")
        lbl = Label(root, image=logo, bg="#f16161").grid(row=0, column=0, pady=5, sticky=W)

        btnframe = Frame(root, bg="#f16161") #btn frame
        btnframe.grid(row=0, column=1) # Toolbar on top of the window.
        faq_btn = Button(btnframe, text="FAQ", command=fn.faqKTL, font="none 12",bg="#df9999", width=10, height=1)
        faq_btn.grid(row=0, column=0, pady=5, padx = 10, sticky=NW)
        man_btn = Button(btnframe, text="Manual", command=fn.manualKTL, font="none 12",bg="#df9999", width=10, height=1)
        man_btn.grid(row=0, column=1, pady=5, padx = 10, sticky=NW)
        cnt_btn = Button(btnframe, text="Contant Me", command=fn.contactKTL, font="none 12", bg="#df9999", width=10, height=1)
        cnt_btn.grid(row=0, column=2, pady=5, padx = 10, sticky=NW)
        # Row 1
        logotxt = Label(root, text="KazTransLit", bg="#f16161", fg="white", font="none 12 bold")
        logotxt.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        btn = Button(root, text="Document to Text", command=fn.documentKTL, font="none 12", bg="#df9999", width=20, height=5)
        btn.grid(row=1, column=1, padx=10, pady=5, sticky=E)
        btn = Button(root, text="Real Time Transliteration", command=fn.realtimeKTL, font="none 12", bg="#df9999", width=20, height=5)
        btn.grid(row=1, column=2, padx=10, pady=5, sticky=E)
        # Row 2
        btn = Button(root, text="Settings", command = fn.settingsKTL, font="none 12", bg="#df9999", width=20, height=5)
        btn.grid(row=2, column=2, padx=10, pady=5, sticky=E)
        # Exit
        btn = Button(root, text="EXIT", font="none 10", bg="#FF4C4C", width=20, height=5, command=self.close_root)
        btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

        root.resizable(1, 1)
        root.iconbitmap('images/TK_logo.ico')
        root.mainloop()

    def close_root(self):  # Kill func.
        self.root.destroy()
        exit()

Main()
