class EmailSender:
    def send(self, message):
        print("Sending email:", message)
        
class OrderService:
    def __init__(self, email_sender):
        self.email_sender = email_sender

    def create_order(self):
        print("Order created")
        self.email_sender.send("Order confirmation")

email_sender = EmailSender()
order_service = OrderService(email_sender)

order_service.create_order()

"""
🧠 ¿Qué hace realmente DI?

Permite:

Cambiar implementación sin tocar código

Mejor testing

Mejor mantenimiento

Mejor arquitectura

Menos acoplamiento
"""