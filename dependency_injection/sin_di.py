class EmailSender:
    def send(self, message):
        print("Sending email:", message)


class OrderService:
    def __init__(self):
        self.email_sender = EmailSender()  # dependencia rígida

    def create_order(self):
        print("Order created")
        self.email_sender.send("Order confirmation")

# Ejemplo de uso
if __name__ == "__main__":
    service = OrderService()
    service.create_order()
    
"""
Problemas:

No puedes cambiar EmailSender

No puedes hacer mock en test

No puedes usar otro tipo de notificador
"""