import logging

from src.example.accounting_service import AccountService
from src.example.bill_payment_service import BillPaymentService
from src.example.transfer_service import TransferService

logger = logging.getLogger(__name__)


# Facade — single entry point that delegates to subsystem services
class Bank:
    def __init__(self):
        self.accounting_service = AccountService()  # subsystem for account queries
        self.transfer_service = TransferService()  # subsystem for fund transfers
        self.bill_payment_service = BillPaymentService()  # subsystem for bill payments
        logger.info("Bank facade initialized")

    def get_account_details(self, account_id):
        logger.info(f"Bank: requesting account details for {account_id}")
        self.accounting_service.getAccountDetails(account_id)

    def transfer_funds(self, from_account_id, to_account_id, amount):
        logger.info(f"Bank: initiating transfer of ${amount}")
        self.transfer_service.transfer_funds(from_account_id, to_account_id, amount)

    def pay_bill(self, account_id, bill_id, amount):
        logger.info(f"Bank: initiating bill payment for {bill_id}")
        self.bill_payment_service.pay_bill(account_id, bill_id, amount)
