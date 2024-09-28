from gui.base_tab import BaseTab

class ClientesTab(BaseTab):
    def __init__(self, parent, db_config):
        columns = ("ID", "Nombre", "Telefono", "Email")
        column_names = ["ID", "Nombre", "Telefono", "Email"]
        super().__init__(parent, db_config, "clientes", columns, column_names)