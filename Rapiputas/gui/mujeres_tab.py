import os
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import io
import sqlite3
from gui.base_tab import BaseTab


class MujeresTab(BaseTab):
    def __init__(self, parent, db_config):
        columns = ("ID", "Nombre", "Edad", "Coste", "Notas","imagen")
        column_names = ["ID", "Nombre", "Edad", "Coste", "Notas","imagen"]
        super().__init__(parent, db_config, "mujeres", columns, column_names)

    def create_widgets(self):
        super().create_widgets()

        # Agregar el botón "Solicitar Servicio"
        self.request_service_button = tk.Button(self, text="Solicitar Servicio", command=self.request_service,
                                                bg='orange', fg='white', font=('Arial', 10))
        self.request_service_button.pack(side=tk.TOP, pady=10)

        # Cargar registros al árbol
        self.load_images()

    def load_images(self):
        records = self.get_records_from_db()

        for record in records:
            id_, nombre, edad, coste, notas, imagen_bytes = record  # Cambia a imagen_bytes

            # Convertir bytes a imagen y luego a PhotoImage
            if imagen_bytes:
                image = Image.open(io.BytesIO(imagen_bytes))
                image.thumbnail((50, 50))  # Cambia el tamaño según tus necesidades
                photo = ImageTk.PhotoImage(image)
                self.tree.image_refs = getattr(self.tree, 'image_refs', [])
                self.tree.image_refs.append(photo)  # Mantener referencia para evitar la recolección de basura

                # Insertar solo los datos relevantes en el árbol, no incluir imagen en valores
                self.tree.insert("", "end", values=(id_, nombre, edad, coste, notas), image=photo)
            else:
                # Si no hay imagen, insertar solo los otros valores
                self.tree.insert("", "end", values=(id_, nombre, edad, coste, notas))

    def get_records_from_db(self):
        connection = None
        try:
            db_path = os.path.join(os.path.dirname(__file__), 'tu_base_de_datos.db')
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()

            cursor.execute(
                "SELECT ID, Nombre, Edad, Coste, Notas, imagen FROM mujeres")  # 'imagen' debería ser BLOB
            records = cursor.fetchall()

            return records
        except Exception as e:
            print(f"Error al obtener registros: {e}")
            return []
        finally:
            if connection:
                connection.close()

    def request_service(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un registro para solicitar el servicio.")
            return

        record = self.tree.item(selected_item)['values']
        messagebox.showinfo("Solicitud de Servicio",
                            f"Solicitud realizada para: {record[1]}")
