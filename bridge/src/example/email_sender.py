from src.example.message_sender import MessageSender


# Concrete Implementor — delivers messages via email
class EmailSender(MessageSender):
    def send_message(self, to, body):
        print(f"Sending email to {to}: {body}")
