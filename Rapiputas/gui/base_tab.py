import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
from database.db_operations import insert_record, update_record, delete_record, load_data, search_by_id

class BaseTab(tk.Frame):
    def __init__(self, parent, db_config, table_name, columns, column_names):
        super().__init__(parent)
        self.db_config = db_config
        self.table_name = table_name
        self.columns = columns
        self.column_names = column_names
        self.create_widgets()

    def create_widgets(self):
        self.configure(bg='#87CEEB')  # Color de fondo vibrante

        # Frame para la imagen
        self.image_frame = tk.Frame(self, bg='#87CEEB')
        self.image_frame.pack(side=tk.TOP, padx=10, pady=10)

        # Label para mostrar la imagen
        self.image_label = tk.Label(self.image_frame, bg='#87CEEB')
        self.image_label.pack()

        # Marco para la información
        info_frame = tk.LabelFrame(self, text=f"Información de {self.table_name.capitalize()}", padx=10, pady=10,
                                   bg='#B0E0E6', font=('Arial', 12, 'bold'))
        info_frame.pack(padx=10, pady=10, fill=tk.X)

        # Entradas de información
        self.entries = []
        for i, column_name in enumerate(self.column_names):
            tk.Label(info_frame, text=f"{column_name}:", padx=5, pady=5, bg='#B0E0E6', font=('Arial', 10)).grid(row=i,
                                                                                                                column=0,
                                                                                                                sticky="e", padx=5)
            entry = tk.Entry(info_frame, width=30, justify='center', bg='white', fg='black', font=('Arial', 10))
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            self.entries.append(entry)

        # Botones de acción
        button_frame = tk.Frame(info_frame, bg='#B0E0E6')
        button_frame.grid(row=len(self.column_names), column=0, columnspan=2, pady=10)

        # Crear botones con colores originales
        buttons = [
            ("Cargar Imagen", self.load_image, 'blue'),
            ("Buscar ID", self.search_by_id, 'green'),
            ("Crear", self.create, 'green'),
            ("Actualizar", self.update, 'orange'),
            ("Eliminar", self.delete, 'red')
        ]

        for text, command, color in buttons:
            tk.Button(button_frame, text=text, command=command, bg=color, fg='white',
                      font=('Arial', 10)).pack(side=tk.LEFT, padx=5)

        # Tabla para mostrar los datos
        self.tree = ttk.Treeview(self, columns=self.columns, show="headings", height=5)
        for column in self.columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, anchor="center")  # Centrar los encabezados de la tabla
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Estilo para la tabla
        style = ttk.Style()
        style.configure("Treeview", background="white", foreground="black", rowheight=25, fieldbackground="white")
        style.configure("Treeview.Heading", background="#FFD700", foreground="black", font=('Arial', 10, 'bold'))
        style.map("Treeview.Heading", background=[('active', '#FFC107')])

        self.load_data()
        self.tree.bind('<<TreeviewSelect>>', self.on_select)

    def on_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            record = item['values']
            self.populate_fields(record)
            self.show_image(record[-1])  # Suponiendo que la imagen está en la última columna

    def show_image(self, image_path):
        if image_path and os.path.exists(image_path):
            try:
                img = Image.open(image_path)
                img = img.resize((150, 150), Image.LANCZOS)
                self.img_tk = ImageTk.PhotoImage(img)
                self.image_label.config(image=self.img_tk)
                self.image_label.image = self.img_tk
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar la imagen: {e}")

    def load_image(self):
        file_path = filedialog.askopenfilename(title="Seleccionar Imagen",
                                               filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
        if file_path:
            file_path = os.path.abspath(file_path)
            selected_item = self.tree.selection()
            if selected_item:
                current_values = list(self.tree.item(selected_item)['values'])
                updated_values = current_values[:-1] + [file_path]
                self.tree.item(selected_item, values=updated_values)
                self.show_image(file_path)

                self.update_image_in_db(current_values[0], file_path)
                messagebox.showinfo("Éxito", f"Imagen cargada: {file_path}")

    def update_image_in_db(self, record_id, image_path):
        update_record(self.db_config, self.table_name, ["imagen"], [image_path], record_id)

    def search_by_id(self):
        record_id = self.entries[0].get()
        if not record_id:
            messagebox.showwarning("Advertencia", "Por favor, ingrese un ID para buscar.")
            return

        record = search_by_id(self.db_config, self.table_name, record_id)
        if record:
            self.populate_fields(record[0])
            self.show_image(record[0][-1])
        else:
            messagebox.showinfo("Información", f"No se encontró un registro con ese ID en {self.table_name}.")

    def populate_fields(self, record):
        for i, value in enumerate(record):
            self.entries[i].delete(0, tk.END)
            self.entries[i].insert(0, value)

    def create(self):
        values = [entry.get() for entry in self.entries[1:]]
        if any(not value for value in values):
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos requeridos.")
            return

        insert_record(self.db_config, self.table_name, self.columns[1:], values)
        messagebox.showinfo("Éxito", f"Registro creado con éxito en {self.table_name}.")
        self.load_data()

    def update(self):
        record_id = self.entries[0].get()
        values = [entry.get() for entry in self.entries[1:]]
        if not record_id or any(not value for value in values):
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos requeridos.")
            return

        update_record(self.db_config, self.table_name, self.columns[1:], values, record_id)
        messagebox.showinfo("Éxito", f"Registro actualizado en {self.table_name}.")
        self.load_data()

    def delete(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un registro para eliminar.")
            return

        record_id = self.tree.item(selected_item)['values'][0]
        delete_record(self.db_config, self.table_name, record_id)
        messagebox.showinfo("Éxito", f"Registro eliminado de {self.table_name}.")
        self.load_data()

    def load_data(self):
        records = load_data(self.db_config, self.table_name)
        self.tree.delete(*self.tree.get_children())
        for record in records:
            self.tree.insert("", "end", values=record)