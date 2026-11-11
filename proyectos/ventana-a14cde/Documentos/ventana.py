import tkinter as Tk
from tkinter import messagebox

# crear el objeto ventana
kevin = Tk.Tk()
kevin.title("ventanas")

kevin.geometry("300x300+540+200")

lblTitulo = Tk.Label(kevin, text="ventanas")
lblTitulo.grid(row=0, column=1)

lblNombre = Tk.Label(kevin, text="Nombre")
lblNombre.grid(row=1, column=0)

txtNombre = Tk.Entry(kevin)
txtNombre.grid(row=1, column=1)

def mostrar_nombre():
    nombre = txtNombre.get().strip()
    if not nombre:
        messagebox.showwarning("Nombre", "Escribe un nombre para continuar.")
        return
    messagebox.showinfo("Saludo", "Hola, " + nombre)

btnCalcular = Tk.Button(kevin, text="Saludar", command=mostrar_nombre)
btnCalcular.grid(row=2, column=1, pady=12)

kevin.mainloop()