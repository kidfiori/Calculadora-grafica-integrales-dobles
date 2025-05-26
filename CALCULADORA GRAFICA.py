import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, lambdify

# Variables globales necesarias para controlar el estado del gráfico y del botón de borrado
canvas_list = []
btn_borrar = None

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Gráficos 3D de Funciones de Múltiples Variables")
root.geometry("600x600")

# Contenedores de entrada y visualización
frame_input = tk.Frame(root)
frame_input.pack(pady=5)

frame_plot = tk.Frame(root)
frame_plot.pack(pady=5)

# Controles de entrada para la función y las coordenadas (x0, y0)
label_funcion = tk.Label(frame_input, text="Función en términos de x y y (ej. x**2 + y**2):")
label_funcion.pack(pady=5)
entry_funcion = tk.Entry(frame_input)
entry_funcion.pack(pady=5)

label_x0 = tk.Label(frame_input, text="Coordenada x0:")
label_x0.pack(pady=5)
entry_x0 = tk.Entry(frame_input)
entry_x0.pack(pady=5)

label_y0 = tk.Label(frame_input, text="Coordenada y0:")
label_y0.pack(pady=5)
entry_y0 = tk.Entry(frame_input)
entry_y0.pack(pady=5)

# Botones para mostrar el gráfico y limpiar la gráfica
btn_mostrar_funcion = tk.Button(frame_input, text="Mostrar Gráfico 3D", command=lambda: mostrar_funcion_3d())
btn_mostrar_funcion.pack(pady=10)

btn_borrar = tk.Button(frame_input, text="Borrar Gráfica", command=lambda: limpiar_grafico())
btn_borrar.pack(pady=10)

# Función que muestra el gráfico 3D y el plano tangente en el punto indicado
def mostrar_funcion_3d():
    limpiar_grafico()
    funcion = entry_funcion.get().replace("sen", "sin")
    x, y = symbols('x y')
    try:
        f_expr = eval(funcion)
        f = lambdify((x, y), f_expr)
        x_vals = np.linspace(-5, 5, 100)
        y_vals = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x_vals, y_vals)
        Z = f(X, Y)
        x0 = float(entry_x0.get())
        y0 = float(entry_y0.get())
        fx = diff(f_expr, x)
        fy = diff(f_expr, y)
        fx_val = float(fx.subs({x: x0, y: y0}))
        fy_val = float(fy.subs({x: x0, y: y0}))
        z0 = float(f(x0, y0))
        Zt = fx_val * (X - x0) + fy_val * (Y - y0) + z0
        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)
        ax.plot_surface(X, Y, Zt, cmap='coolwarm', alpha=0.5)
        ax.scatter(x0, y0, z0, color='red', s=50)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title(f"Función y Plano Tangente en ({x0}, {y0})")
        canvas = FigureCanvasTkAgg(fig, master=frame_plot)
        canvas.draw()
        canvas.get_tk_widget().pack()
        canvas_list.append(canvas)
        explanation = (
            f"Derivadas parciales:\n∂f/∂x = {fx_val}, ∂f/∂y = {fy_val}\n\n"
            f"Ecuación del plano tangente:\n"
            f"z = {z0} + {fx_val}*(x - {x0}) + {fy_val}*(y - {y0})"
        )
        messagebox.showinfo("Plano Tangente", explanation)
    except Exception as e:
        messagebox.showerror("Error", f"Error al graficar: {e}")

# Función que elimina los gráficos existentes de la interfaz
def limpiar_grafico():
    for canvas in canvas_list:
        canvas.get_tk_widget().pack_forget()
    canvas_list.clear()

# Ventana emergente con la pantalla de carga y autores
def show_loading_screen():
    loading_screen = tk.Toplevel(root)
    loading_screen.title("Cargando...")
    loading_screen.geometry("700x400")
    label_title = tk.Label(loading_screen, text="CALCULADORA GRÁFICA DE PLANOS TANGENTES", font=("Arial", 16))
    label_title.pack(pady=30)
    authors = tk.Label(loading_screen, text="Autores:\nJuan E Florido\nJuan D Bernal\nNelson D Loaiza\nDiego A Mora", font=("Arial", 12))
    authors.pack(pady=40)
    btn_continue = tk.Button(loading_screen, text="Continuar", command=loading_screen.destroy)
    btn_continue.pack(pady=20)

# Iniciar la pantalla de carga después de mostrar la ventana principal
root.after(100, show_loading_screen)

# Ejecutar la aplicación
root.mainloop()
