import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

raiz = tk.Tk()
raiz.title("Sticky Notes")
raiz.geometry('200x200+50+50')

def change_color(objetivo):
    colors = askcolor(title="Tkinter Color Chooser")
    objetivo.configure(bg=colors[1])

def nuevanota():
    splash = tk.Tk()
    anchura = 800
    altura = 400
    B1 = ttk.Button(splash, text="Okay", command = splash.destroy)
    B1.pack()
    B2 = ttk.Button(splash, text="Color", command = lambda:
change_color(splash))
    B2.pack()
    T = tk.Text(splash, height = 5, width = 52,bg="white")
    T.pack()
    splash.geometry(f'{400}x{400}+{400}+{400}')
    splash.mainloop()

botonsalida = ttk.Button(raiz,text="Nueva nota",command=nuevanota)
botonsalida.pack(ipadx=5,ipady=5,expand=True)

try:
    #intenta importar la libreria de Windows
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
finally:
    raiz.mainloop()
