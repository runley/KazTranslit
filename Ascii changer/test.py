import tkinter as tk
from tkinter import filedialog as fd 

def callback():
    name= fd.askopenfilename() 
    print(name)


def documentKTL(): #top level func to create a new window as Toplevel
    docKTL = tk.Toplevel(bg = "#f16161")
    docKTL.title('Document to Text - KTL')
    global directory
    global saveDirectory

    #row 0
    logotxt = tk.Label(callback, text="TransKazLit", bg="#f16161", fg="white",font="Bahnschrift 24 bold")
    logotxt.grid(row=0, column=0, padx=10, pady=5)

    #row 1
    btn = tk.Button(docKTL, text="Choose a file", command=askFile, font="none 14", bg="#EF4A4A", fg="white", width=12, height=1)
    btn.grid(row=1, column=0, padx=5, pady=5)
    consoleUI = Text(docKTL, height = 20, width = 50) #consoleUI element
    consoleUI.grid(row=1, column=1, pady = 5, padx = 5, columnspan=2, rowspan=5)

    
errmsg = 'Error!'

btn = tk.Button( text="Document to Text", command=documentKTL, font="none 14", bg="#EF4A4A", fg="white", width=20, height=5)
btn.pack(fill=tk.X)
        
tk.Button(text='Click to Open File', 
       command=callback).pack(fill=tk.X)
tk.mainloop()


