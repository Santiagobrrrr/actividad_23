import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("600x600")

etiqueta1 = tk.Label(ventana, text="Ingrese el primer numero: ")
etiqueta1.pack(pady=5)

num1 = tk.Entry(ventana)
num1.pack(pady=5)

etiqueta2 = tk.Label(ventana, text="Ingrese el segundo numero: ")
etiqueta2.pack(pady=5)

num2 = tk.Entry(ventana)
num2.pack(pady=5)

total = tk.Label(ventana, text="Total: ")
total.pack(pady=5)

def suma():
    sum = float(num1.get()) + float(num2.get())
    total.config(text=f"Total de suma, {sum}")

def resta():
    rest = float(num1.get()) - float(num2.get())
    total.config(text=f"Total de suma, {rest}")

def multiplicacion():
    multi = float(num1.get()) * float(num2.get())
    total.config(text=f"Total de suma, {multi}")

def dividir():
    divi = float(num1.get()) / float(num2.get())
    total.config(text=f"Total de división, {divi}")

def limpiar():
    num1.delete(0, tk.END)
    etiqueta1.config(text="Ingrese el primer numero:")

    num2.delete(0, tk.END)
    etiqueta2.config(text="Ingrese el segundo numero:")

boton_suma = tk.Button(ventana, text="+", command=suma)
boton_suma.pack(pady=5)

boton_resta = tk.Button(ventana, text="-", command=resta)
boton_resta.pack(pady=5)

boton_multiplicar = tk.Button(ventana, text="*", command=multiplicacion)
boton_multiplicar.pack(pady=5)

boton_dividir = tk.Button(ventana, text="/", command=dividir)
boton_dividir.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Borrar numeros", command=limpiar)
boton_limpiar.pack(pady=5)

boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()