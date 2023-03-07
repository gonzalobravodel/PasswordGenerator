# lo primero es importar librerias
from tkinter import *
import tkinter as tk
import secrets
import string

#creamos la raiz para el frame principal

appWidget=tk.Tk() #inicio instancia de raiz 
appWidget.geometry("400x400")
appWidget.configure(background="black")
tk.Wm.wm_title(appWidget, "Password Generator")

mensaje = tk.Text(appWidget, background="white", width=25, height=10)
mensaje.pack(padx=10, pady=5)

#adding widgets
tk.Button(
	appWidget,
	text="Generate Password",
	font=("Cascadia Code",  20),
	bg="black",
	fg="green",
	command= lambda: mensaje.insert("insert", "".join((secrets.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(12)))+'\n'),
).pack(
	fill=tk.BOTH,
	expand=True,
)


appWidget.mainloop()