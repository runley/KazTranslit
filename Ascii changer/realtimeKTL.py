#imports
import functions as fn
from tkinter import *
from tkinter import ttk
try:
    from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename
except ImportError:
    from tkFileDialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename

def realtimeKTL(): #top level for realtime window + code to make the window work
    global txtboxbuffer
    realKTL = Toplevel(bg = "#f16161")
    realKTL.title(' - Real-time')

    # Row 0
    logotxt = Label(realKTL, text="TransKazLit", bg="#f16161", fg="white", font="Bahnschrift 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    lbl = Label(realKTL,bg="#f16161", text = "Enter text here:", fg = "white", font="Bahnschrift 15")
    lbl.grid(row = 1, column= 0,)
    lbl = Label(realKTL,bg="#f16161", text = "Watch magic happen here:", fg = "white", font="Bahnschrift 15")
    lbl.grid(row = 1, column= 1,)

    #row 2
    txtbox = Text(realKTL, height = 20, width = 50)
    txtbox.grid(row=2, column=0, pady = 5, padx = 5)
    outbox = Text(realKTL, height = 20, width = 50)
    outbox.grid(row=2, column=1, pady = 5, padx = 5)

    #update
    def updateout(event): # func to update outbox contents and processs txtbox
        print("pressed", event.char)
        txtboxbuffer = fn.realtimeChanger(txtbox.get("1.0", "end"), fn.kazalphabet)
        outbox.delete("1.0", "end")  # if you want to remove the old data
        outbox.insert(END,txtboxbuffer)
        print("txtboxbuffer contents are:", txtboxbuffer)

    txtbox.bind("<KeyRelease>", updateout)# bind all keys to updateout() func

    #close top
    btn = Button(realKTL, command = lambda: fn.exit_btn(realKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    realKTL.iconbitmap('images/KTL_logo.ico')
    realKTL.resizable(0, 0)
