from gui.base_tab import BaseTab

class ServiceTypesTab(BaseTab):
    def __init__(self, parent, db_config):
        columns = ("ID", "Descripcion", "Coste")
        column_names = ["ID", "Descripcion", "Coste"]
        super().__init__(parent, db_config, "tipo_servicio", columns, column_names)