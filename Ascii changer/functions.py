#imports
from tkinter import *
from tkinter import ttk
try:
    from tkinter.filedialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename
except ImportError:
    from tkFileDialog import askopenfilename, askdirectory, askopenfilenames, asksaveasfilename
#use the ask dir and other shit above
#vars
global buff #buffer medium
global FileDir
global saveDir
global kazalphabet

#kazalphabet init
kazalphabet = {"А":"A","Ә":"Ä","Б":"B","В":"V","Г":"G","Ғ":"Ğ","Д":"D","Е":"E","Ё":"YO","Ж":"J","З":"Z","И":"Ï","Й":"Y","К":"K","Қ":"Q","Л":"L","М":"M","Н":"N","Ң":"Ñ","О":"O","Ө":"Ö","П":"P","Р":"R","С":"S","Т":"T","У":"W","Ұ":"U","Ү":"Ü","Ф":"F","Х":"X","Һ":"H","Ц":"C","Ч":"Ç","Ш":"Ş","Щ":"ŞÇ","Ъ":"\"","Ы":"I","І":"I","Ь":"\'","Э":"É","Ю":"YU","Я":"YA","а":"a","ә":"ä","б":"b","в":"v","г":"g","ғ":"ğ","д":"d","е":"e","ё":"yo","ж":"j","з":"z","и":"ï","й":"y","к":"k","қ":"q","л":"l","м":"m","н":"n","ң":"ñ","о":"o","ө":"ö","п":"p","р":"r","с":"s","т":"t","у":"w","ұ":"u","ү":"ü","ф":"f","х":"x","һ":"h","ц":"c","ч":"ç","ш":"ş","щ":"şç","ъ":"\"","ы":"ı","і":"i","ь":"\'","э":"é","ю":"yu","я":"ya"} #dictionary

#functions
def docChanger(stringinp,alphabetDic): #Document transliteration for loop
  bfile = open("Buffer.txt","w")
  procingstring = stringinp
  for letter in alphabetDic:
    letter_definition = alphabetDic.get(letter)
    procingstring = procingstring.replace(letter,letter_definition)
  bfile.write(procingstring)

def realtimeChanger(stringinp,alphabetDic): #real time transliteration for loop
    procingstring = stringinp
    for letter in alphabetDic:
      letter_definition = alphabetDic.get(letter)
      procingstring = procingstring.replace(letter,letter_definition)
    return procingstring

def askFile(): #gets user input for further proccessing
    FileDir = askopenfilename()
    with open(FileDir, "r", encoding='utf-8') as askedFile:
        procingstring = askedFile.read()
    docChanger(procingstring, kazalphabet)
    print(FileDir, "has been converted")

def askSave():
    try:
        saveDir = asksaveasfilename()
        return saveDir
        print(saveDir)
    except Exception as e:
        raise

def askUser(userInput): #takes in userinput to convert to file object, returns file
    try:
        userFile = open(userInput,"r+") #tries to convert and find file
        return userFile
    except:
        print("error occured in functions.askUser()")#does not find file

def bufferCleaner(BufferLocation): #cleans buffer file
    tempBuffer = open(BufferLocation,"w")
    tempBuffer.close()

def exit_btn(name): # closes top levels by taking the name of the top level
    name.destroy()
    name.update()
