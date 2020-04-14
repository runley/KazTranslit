from tkinter import *

defualtsize =12
acc_font_size = defualtsize

#def change(a=0):
 #   print( a) ## debug
  #  lbl.config(bg = "blue" if a & 1 else "purple")
   # lbl.after(400,change, a ^ 1 )

def updateFont(bool, size):
    lbl.config(font = "none {0}".format(size) if bool & True else "Bahnschrift {0}".format(size))


if __name__ == '__main__':
    win= Tk() 
    win.geometry("500x300")
    lbl = Label(win, text="KazTransLit", bg="#f16161", fg="white", font="Bahnschrift {0} bold".format(acc_font_size))
    lbl.grid(row=1, column=0, padx=10, pady=5, sticky=SW)

    lbl = Label(win, text="KazTransLit", bg="#f16161", fg="white", font="Bahnschrift {0} bold".format(acc_font_size))
    lbl.grid(row=2, column=0, padx=10, pady=5, sticky=SW)

    
    faq_btn = Button(win, text="FAQ", command=updateFont(False, 20), font="none {0}".format(acc_font_size),bg="#EF4A4A", width=10, height=1)
    faq_btn.grid(row=0, column=0, pady=5, padx = 10, sticky=NW)
