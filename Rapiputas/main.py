import tkinter as tk
from tkinter import ttk
from config import db_config
from gui.service_types_tab import ServiceTypesTab
from gui.mujeres_tab import MujeresTab
from gui.clientes_tab import ClientesTab
from gui.ventas_tab import VentasTab

if __name__ == "__main__":
    root = tk.Tk()
    root.title("RappiPutas")
    root.geometry("800x600")
    root.configure(bg='#87CEEB')  # Fondo del contenedor principal

    root.iconbitmap(r"C:\Users\311\PycharmProjects\pythonProject\favicon.ico")

    notebook = ttk.Notebook(root)
    notebook.add(ServiceTypesTab(notebook, db_config), text="Tipos de Servicio")
    notebook.add(MujeresTab(notebook, db_config), text="Mujeres")
    notebook.add(ClientesTab(notebook, db_config), text="Clientes")
    notebook.add(VentasTab(notebook, db_config), text="Ventas")
    notebook.pack(fill=tk.BOTH, expand=True)

    root.mainloop()