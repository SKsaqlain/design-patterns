from src.example.email_sender import EmailSender
from src.example.sms_sender import SMSSender
from src.example.message import UrgentMessage


if __name__ == '__main__':
    # Bridge an urgent message with email delivery
    email_msg = UrgentMessage(EmailSender())  # abstraction + implementor
    email_msg.send('alice@example.com', 'Server is down!')

    # Bridge the same abstraction with SMS delivery
    sms_msg = UrgentMessage(SMSSender())  # swap implementor at runtime
    sms_msg.send('+1234567890', 'Server is down!')
