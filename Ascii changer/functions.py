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
    print("error occured in fn.askUser()") #does not find file


def bufferCleaner(BufferLocation): #cleans buffer file
  tempBuffer = open(BufferLocation,"w")
  tempBuffer.close()

#---------------
#window functions
#---------------
def documentTKL(): #top level func to create a new window as Toplevel
    docTKL = Toplevel(bg = "#f16161")
    docTKL.title('Document TKL')
    docTKL.wm_geometry("794x370")
    docTKL.iconbitmap('images\TK_logo.ico')
    #insert labels and stuff

def realtimeTKL(): #top level func to create a new window as Toplevel
    docTKL = Toplevel(bg = "#f16161")
    docTKL.title('Real-Time TKL')
    docTKL.wm_geometry("794x370")
    docTKL.iconbitmap('images\TK_logo.ico')
    #insert labels and stuff
