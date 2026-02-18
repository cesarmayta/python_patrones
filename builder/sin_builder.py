class Report:
    def __init__(self, title, author, content, footer=None, watermark=None):
        self.title = title
        self.author = author
        self.content = content
        self.footer = footer
        self.watermark = watermark
        
    def show(self):
        return f"{self.title} - {self.author}"

report = Report(
    "Ventas 2024",
    "Cesar",
    "Contenido...",
    None,
    "CONFIDENTIAL"
)

print(report.show())


"""
❌ ¿Cuál es el problema?

No sabes qué parámetro es cuál.

Si hay 10 parámetros opcionales, se vuelve ilegible.

Puedes equivocarte fácilmente en el orden.

El constructor empieza a crecer demasiado.

Si mañana agregas más campos, se vuelve inmanejable.

"""