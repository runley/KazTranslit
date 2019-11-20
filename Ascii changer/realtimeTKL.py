from tkinter import *
from tkinter import ttk
import functions as fn

#functions
def close_realtimeTKL(): #kill func
    realtimeTKL.destroy()
    exit()

#def realtimeloop(): # gets textbox processes it and outputs
#    entered_text = textentry.get() #collects text from entry box
#    output.delete(0.0, END) #see what happens
#    #try:
#    newletter = entered_text
#    for i in kazalphabet:
#      x = kazalphabet.get(i)
#      newletter = newletter.replace(i,x)
#      output.insert(END, newletter)
#    #except:
#    #    errormsg = "There was a problem processing one or more of the entered words."
#    #    output.insert(END, errormsg)


kazalphabet = {"\u0410":"A","\u04d8":"\u00c4","\u0411":"B","\u0412":"V","\u0413":"G",
    "\u0492":"\u011e","\u0414":"D","\u0415":"E","\u0401":"YO","\u0416":"J","\u0417":"Z",
    "\u0418":"\u00cf","\u0419":"Y","\u041a":"K","\u049a":"Q","\u041b":"L","\u041c":"M",
    "\u041d":"N","\u04a2":"\u00d1","\u041e":"O","\u04e8":"\u00d6","\u041f":"P","\u0420":"R",
    "\u0421":"S","\u0422":"T","\u0423":"W","\u04b0":"U","\u04ae":"\u00dc","\u0424":"F","\u0425":"X",
    "\u04ba":"H","\u0426":"C","\u0427":"\u00c7","\u0428":"\u015e","\u0429":"\u015e\u00c7",
    "\u042a":"\"","\u042b":"I","\u0406":"I","\u042c":"\'","\u042d":"\u00c9","\u042e":"YU",
    "\u042f":"YA","\u0430":"a","\u04d9":"\u00e4","\u0431":"b","\u0432":"v","\u0433":"g",
    "\u0493":"\u011f","\u0434":"d","\u0435":"e","\u0451":"yo","\u0436":"j","\u0437":"z",
    "\u0438":"\u00ef","\u0439":"y","\u043a":"k","\u043b":"l","\u043c":"m","\u043d":"n",
    "\u04a3":"\u00f1","\u043e":"o","\u04e9":"\u00f6","\u043f":"p","\u0440":"r","\u0441":"s","\u0442":"t",
    "\u0443":"w","\u04b1":"u","\u04af":"\u00fc","\u0444":"f","\u0445":"x","\u04bb":"h",
    "\u0446":"c","\u0447":"\u00e7","\u0448":"\u015f","\u0449":"\u015f\u00e7","\u044a":"\"",
    "\u044b":"\u0131","\u0456":"i","\u044c":"\'","\u044d":"\u00e9","\u044e":"yu","\u044f":"ya"}

#main
realtimeTKL = Tk()
realtimeTKL.title("Real-Time Transliteration")
realtimeTKL.configure(background = "#f16161")

#row 0
#photo
logo = PhotoImage(file = "images\TK_logo.png")
Label(realtimeTKL, image=logo, bg="#f16161").grid(row = 0, column = 0, pady=5, sticky = W)

#row 1
Label(realtimeTKL, text = "\nReal-Time Transliteration", bg = "#f16161", fg = "white", font = "none 12 bold").grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

#row 2
#text entry box
textentry = Text(realtimeTKL, width = 50, height = 30, bg = "#df9999")
textentry.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)
textentry.configure(font=("none, 12 bold"))
textentry.insert(0.0,"Enter Text")

output = Text(realtimeTKL, width = 50, height = 30, wrap = WORD, background = "#df9999")
output.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)
output.configure(font=("none, 12 bold"))
#output.config(state=DISABLED)

#row 3
#Button(realtimeTKL, text = "Start", width = 6, command = realtimeloop).grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

#exit
Button(realtimeTKL, text = "EXIT", font = "none 10", bg="#FF4C4C", width = 20, height = 5, command = close_realtimeTKL).grid(row = 10, column = 0, padx = 10, pady = 5, sticky = W)


#realtimeloop()
realtimeTKL.iconbitmap('images\TK_logo.ico')
realtimeTKL.mainloop()
