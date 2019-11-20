from tkinter import *
from tkinter import ttk
import functions as fn

#functions
def close_docTKL(): #kill func
    docTKZ.destroy()
    exit()

#main
docTKL = Tk()
docTKL.title("Document Transliteration")
docTKL.configure(background = "#f16161")

#row 0
#photo
logo = PhotoImage(file = "images\TK_logo.png")
Label(docTKL, image=logo, bg="#f16161").grid(row = 0, column = 0, pady=5, sticky = W)

#row 1
Label(docTKL, text = "\nTransKazLit", bg = "#f16161", fg = "white", font = "none 12 bold").grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

#row 2

#row 3


root.iconbitmap('images\TK_logo.ico')
docTKL.mainloop()
