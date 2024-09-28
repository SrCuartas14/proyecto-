from gui.base_tab import BaseTab

class VentasTab(BaseTab):
    def __init__(self, parent, db_config):
        columns = ("ID", "id_mujer", "id_cliente", "fecha", "total")
        column_names = ["ID", "id_mujer", "id_cliente", "fecha", "total"]
        super().__init__(parent, db_config, "ventas", columns, column_names)