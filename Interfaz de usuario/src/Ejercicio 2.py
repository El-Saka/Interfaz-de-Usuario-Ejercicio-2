import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Configurar el titulo de la ventana
root.title("Interfaz Sencilla")

# Creear el label
label = tk.Label(root, text="Selecciona un elemento: ")

# Crear la lista de elementos seleccionables
opciones = ["Opcion 1", "Opcion 2", "Opcion 3"]
lista = tk.Listbox(root)
for opcion in opciones:
    lista.insert(tk.END, opcion)

#Empaquetar los widgets en la ventana
label.pack()
lista.pack()

# Arrancar el bucle de eventos
root.mainloop()