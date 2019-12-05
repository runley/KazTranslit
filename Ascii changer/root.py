from tkinter import *
from tkinter import ttk
import functions as fn
from subprocess import call

#functions
def close_root(): #kill func
    root.destroy()
    exit()

#Main:
root = Tk()
root.title("TKL")
root.configure(background = "#f16161")

#row 0
#photo
logo = PhotoImage(file = "Ascii changer\images\TK_logo.png")
Label(root, image=logo, bg="#f16161").grid(row = 0, column = 0, pady=5, sticky = W)

buttonframe = Frame(root).grid(row = 0, column = 1)
Button(buttonframe, text = "FAQ", command = fn.documentTKL, font = "none 12", bg="#df9999", width = 5, height = 1).grid(row = 0, column = 1, pady = 5, sticky = NW)
Button(buttonframe, text = "Manual", command = fn.documentTKL, font = "none 12", bg="#df9999", width = 5, height = 1).grid(row = 0, column = 2, pady = 5, sticky = NW)
Button(buttonframe, text = "Something", command = fn.documentTKL, font = "none 12", bg="#df9999", width = 5, height = 1).grid(row = 0, column = 3, pady = 5, sticky = NW)

#row 1
Label(root, text = "\nTransKazLit", bg = "#f16161", fg = "white", font = "none 12 bold").grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
Button(root, text = "Document to Text", command = fn.documentTKL, font = "none 12", bg="#df9999", width = 20, height = 5).grid(row = 1, column = 1, padx = 10, pady = 5, sticky = E)
Button(root, text = "Real Time Transliteration", command = fn.realtimeTKL, font = "none 12", bg="#df9999", width = 20, height = 5).grid(row = 1, column = 2, padx = 10, pady = 5, sticky = E)

#row 2
Button(root, text = "Settings", font = "none 12", bg="#df9999", width = 20, height = 5).grid(row = 2, column = 2, padx = 10, pady = 5, sticky = E)

#exit
Button(root, text = "EXIT", font = "none 10", bg="#FF4C4C", width = 20, height = 5, command = close_root).grid(row = 10, column = 0, padx = 10, pady = 5, sticky = W)

root.resizable(False, False)
root.iconbitmap('Ascii changer\images\TK_logo.ico')
root.mainloop()
