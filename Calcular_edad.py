import tkinter as tk
from tkinter import messagebox
import time
import threading

def calcular_edad():
    edad = entrada.get()
    if not edad.isdigit():
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")
        return
    
    boton.config(state=tk.DISABLED)  # Deshabilitar botón mientras "calcula"
    progreso["value"] = 0  # Reiniciar barra de progreso
    ventana.update()  # Actualizar ventana
    
    for i in range(11):  # 10 segundos en total (incrementos de 1 cada segundo)
        progreso["value"] = i * 10  # Incrementar progreso en 10% por segundo
        ventana.update()  
        time.sleep(1)
    
    messagebox.showinfo("Resultado", "Edad calculada.")  # Mostrar mensaje
    boton.config(state=tk.NORMAL)  # Rehabilitar botón

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora de Edad")
ventana.geometry("300x200")

tk.Label(ventana, text="Ingresa tu edad:").pack(pady=5)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

progreso = tk.ttk.Progressbar(ventana, length=200, mode="determinate")
progreso.pack(pady=10)

boton = tk.Button(ventana, text="Calcular", command=lambda: threading.Thread(target=calcular_edad).start())
boton.pack(pady=10)

ventana.mainloop()
