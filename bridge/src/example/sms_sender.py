from src.example.message_sender import MessageSender


# Concrete Implementor — delivers messages via SMS
class SMSSender(MessageSender):
    def send_message(self, to, body):
        print(f"Sending SMS to {to}: {body}")
