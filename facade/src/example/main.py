import logging

from src.example.bank import Bank

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    bank = Bank()  # facade — client only interacts with this

    bank.get_account_details('123456789')  # delegates to AccountService
    bank.transfer_funds('123456789', '987654321', 100.00)  # delegates to TransferService
    bank.pay_bill('123456789', 'BILL001', 59.99)  # delegates to BillPaymentService
