from tkinter import *
from tkinter import ttk
#-------------------
#functions
#-------------------
def StringChanger(stringinp,Buffer,alphabetDic): #magic code, works, dont touch
  bufferFile = open(Buffer,"a+")
  teststring = stringinp
  for i in alphabetDic:
    x = alphabetDic.get(i)
    teststring = teststring.replace(i,x)
  bufferFile.write(teststring)


def userInput(): #gets user input for further proccessing
  inputvar = input("enter filename:\n>")
  return inputvar


def askUser(userInput): #takes in userinput to convert to file object, returns file
  try:
    userFile = open(userInput,"r+") #tries to convert and find file
    return userFile
  except:
    print("error occured in functions.askUser()") #does not find file


def bufferCleaner(BufferLocation): #cleans buffer file
  tempBuffer = open(BufferLocation,"w")
  tempBuffer.close()


def exit_btn(name): # closes top levels by taking the name of the top level
        name.destroy()
        name.update()
#---------------
#window functions
#---------------
def documentKTL(): #top level func to create a new window as Toplevel
    docKTL = Toplevel(bg = "#f16161")
    docKTL.title('Document to Text - KTL')

    #row 0
    logotxt = Label(docKTL, text="TransKazLit", bg="#f16161", fg="white",font="none 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    lbl = Label(docKTL, text= "wololo", bg="#f16161", fg="white",font="none 14 bold")
    lbl.grid(row=1, column=0, pady=5, sticky=W)

    #row 2

    #close window
    btn = Button(docKTL, command = lambda: exit_btn(docKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    docKTL.iconbitmap('images/KTL_logo.ico')


def realtimeKTL():
    realKTL = Toplevel(bg = "#f16161")
    realKTL.title(' - Real-time')

    # Row 0
    # Photo
    logotxt = Label(realKTL, text="TransKazLit", bg="#f16161", fg="white",font="none 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    lbl = Label(realKTL, text = "Enter text here:")
    lbl.grid(row = 1, column= 0,)
    lbl = Label(realKTL, text = "Watch magic happen here:")

    #row 2
    txtbox = Text(realKTL, height = 20, width = 50)
    txtbox.grid(row=2, column=0, pady = 5, padx = 5)
    outbox = Text(realKTL, height = 20, width = 50)
    outbox.grid(row=2, column=1, pady = 5, padx = 5)

    #row 3

    #close top
    btn = Button(realKTL, command = lambda: exit_btn(realKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    realKTL.iconbitmap('images/KTL_logo.ico')


def settingsKTL():
    settingsKTL = Toplevel(bg = "#f16161")
    settingsKTL.title(' - Settings')

    #row 0
    logotxt = Label(settingsKTL, text="KazTranslit", bg="#f16161", fg="white",font="none 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #close top
    btn = Button(settingsKTL, command = lambda: exit_btn(settingsKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    settingsKTL.iconbitmap('images/KTL_logo.ico')


def manualKTL():
    manKTL = Toplevel(bg = "#f16161")
    manKTL.title(' - Manual')

    #row 0
    logotxt = Label(manKTL, text="KazTranslit", bg="#f16161", fg="white",font="none 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    lbl = Label(manKTL, text="This is the user manual.", bg="#f16161", fg="white",font="none 14 bold")
    lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

    #close top
    btn = Button(manKTL, command = lambda: exit_btn(manKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    manKTL.iconbitmap('images/KTL_logo.ico')


def faqKTL():
    faqKTL = Toplevel(bg = "#f16161")
    faqKTL.title(' - FAQ')

    #row 0
    logotxt = Label(faqKTL, text="KazTranslit", bg="#f16161", fg="white",font="none 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #close top
    btn = Button(faqKTL, command = lambda: exit_btn(faqKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    faqKTL.iconbitmap('images/KTL_logo.ico')


def contactKTL():
    contactKTL = Toplevel(bg = "#f16161")
    contactKTL.title(' - Contact')

    #row 0
    logotxt = Label(contactKTL, text="KazTranslit", bg="#f16161", fg="white",font="none 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5, sticky=W)

    #row 1
    lbl = Label(contactKTL, text="Contact me using the following methods:", bg="#f16161", fg="white",font="none 14 bold")
    lbl.grid(row=1, column=0, padx=10, pady=5, sticky=W)

    #row 2
    lbl = Label(contactKTL, text="Email: sultanbekov.02@outlook.com", bg="#f16161", fg="white",font="none 14")
    lbl.grid(row=2, column=0, padx=10, pady=5, sticky=W)

    #row  3
    lbl = Label(contactKTL, text="Instagram: @_runley", bg="#f16161", fg="white",font="none 14")
    lbl.grid(row=3, column=0, padx=10, pady=5, sticky=W)

    #close top
    btn = Button(contactKTL, command = lambda: exit_btn(contactKTL), text="close window", font="none 10", bg="#FF4C4C", width=10, height=3)
    btn.grid(row=10, column=0, padx=10, pady=5, sticky=W)

    #misc
    contactKTL.iconbitmap('images/KTL_logo.ico')
