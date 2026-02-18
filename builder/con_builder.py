class Report:
    def __init__(self, title, author, content, footer=None, watermark=None):
        self.title = title
        self.author = author
        self.content = content
        self.footer = footer
        self.watermark = watermark

    def show(self):
        return f"{self.title} - {self.author}"


class ReportBuilder:
    def __init__(self):
        self._title = None
        self._author = None
        self._content = None
        self._footer = None
        self._watermark = None

    def title(self, title):
        self._title = title
        return self  # importante para encadenar

    def author(self, author):
        self._author = author
        return self

    def content(self, content):
        self._content = content
        return self

    def footer(self, footer):
        self._footer = footer
        return self

    def watermark(self, watermark):
        self._watermark = watermark
        return self

    def build(self):
        if not self._title:
            raise ValueError("Title is required")
        if not self._author:
            raise ValueError("Author is required")
        if not self._content:
            raise ValueError("Content is required")

        return Report(
            self._title,
            self._author,
            self._content,
            self._footer,
            self._watermark,
        )

report = (
    ReportBuilder()
    .title("Ventas 2024")
    .author("Cesar")
    .content("Contenido importante")
    .watermark("CONFIDENTIAL")
    .build()
)

print(report.show())

"""
🎯 ¿Qué ganamos realmente?

✅ Código más legible
✅ No dependemos del orden de parámetros
✅ Podemos validar antes de construir
✅ Podemos hacer objetos inmutables después
✅ Es ideal cuando hay muchos parámetros opcionales

"""

