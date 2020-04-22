#imports
import functions as fn
from tkinter import *
from tkinter import ttk
try:
    from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename
except ImportError:
    from tkFileDialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename


def manualKTL():
    manKTL = Toplevel(bg = "#f16161")
    manKTL.title(' - Manual')

    #row 0
    logotxt = Label(manKTL, text="KazTranslit", bg="#f16161", fg="white",font="Bahnschrift 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    lbl = Label(manKTL, text="This is the user manual.", bg="#f16161", fg="white",font="none 14 bold")
    lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)
    #row 2
    lbl = Label(manKTL, text="real time KTL", bg="#f16161", fg="white",font="none 13 bold")
    lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)
    #row 3
    lbl = Label(manKTL, text="Input any letter in the Cyrillic alphabet to get a transliterated version of your text.\n for more information please check the FAQs.", bg="#f16161", fg="white",font="none 12")
    lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)
    #close top
    btn = Button(manKTL, command = lambda: exit_btn(manKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    manKTL.iconbitmap('images/KTL_logo.ico')
    manKTL.resizable(0, 0)


def faqKTL():
    faqKTL = Toplevel(bg = "#f16161")
    faqKTL.title(' - FAQ')

    #row 0
    logotxt = Label(faqKTL, text="KazTranslit", bg="#f16161", fg="white",font="Bahnschrift 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #close top
    btn = Button(faqKTL, command = lambda: exit_btn(faqKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    faqKTL.iconbitmap('images/KTL_logo.ico')
    faqKTL.resizable(0, 0)


def contactKTL():
    contactKTL = Toplevel(bg = "#f16161")
    contactKTL.title(' - Contact')

    #row 0
    logotxt = Label(contactKTL, text="KazTranslit", bg="#f16161", fg="white",font="Bahnschrift 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    lbl = Label(contactKTL, text="Contact me using the following methods:", bg="#f16161", fg="white",font="Bahnschrift 14 bold")
    lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

    #row 2
    lbl = Label(contactKTL, text="Email: sultanbekov.02@outlook.com", bg="#f16161", fg="white",font="Bahnschrift 14")
    lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

    #row  3
    lbl = Label(contactKTL, text="Instagram: @_runley", bg="#f16161", fg="white",font="Bahnschrift 14")
    lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

    #close top
    btn = Button(contactKTL, command = lambda: fn.exit_btn(contactKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    contactKTL.iconbitmap('images/KTL_logo.ico')
    contactKTL.resizable(0, 0)
