class JsonExporter:
    def export(self, data):
        return "JSON:" + str(data)


class CsvExporter:
    def export(self, data):
        return "CSV:" + str(data)

def export_data(format_type, data):
    if format_type == "json":
        exporter = JsonExporter()
    elif format_type == "csv":
        exporter = CsvExporter()
    else:
        raise ValueError("Formato no soportado")

    return exporter.export(data)


print(export_data("json", {"id": 1}))

"""
❌ ¿Cuál es el problema?

Cada vez que agregas un formato nuevo, tienes que modificar esta función.

Si hay 10 lugares en el sistema que crean exportadores, todos tendrán if/elif.

Se rompe el principio Open/Closed.

Mezclas lógica de negocio con lógica de creación.
"""