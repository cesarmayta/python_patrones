from abc import ABC, abstractmethod

class Exporter(ABC):
    @abstractmethod
    def export(self, data):
        pass

class JsonExporter(Exporter):
    def export(self, data):
        return "JSON:" + str(data)


class CsvExporter(Exporter):
    def export(self, data):
        return "CSV:" + str(data)

def exporter_factory(format_type):
    format_type = format_type.lower()

    if format_type == "json":
        return JsonExporter()
    elif format_type == "csv":
        return CsvExporter()
    else:
        raise ValueError("Formato no soportado")


def export_data(format_type, data):
    exporter = exporter_factory(format_type)
    return exporter.export(data)


print(export_data("csv", {"id": 2}))

"""
🎯 Ventajas reales en backend

En un sistema grande:

Puedes registrar implementaciones dinámicamente

Puedes inyectar dependencias

Puedes cambiar implementación sin tocar código cliente

Es testeable

Es escalable
"""
