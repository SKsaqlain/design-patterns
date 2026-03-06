

from src.example.accounting_service import AccountService
from src.example.bill_payment_service import BillPaymentService
from src.example.transfer_service import TransferService


class Bank:
    def __init__(self):
        self.accounting_service=AccountService()
        self.transfer_service=TransferService()
        self.bill_payment_service=BillPaymentService()

    
    def get_account_details(self,account_id):
        self.accounting_service.getAccountDetails(account_id)
    
    def transfer_funds(self,from_account_id,to_account_id,amount):
        self.transfer_service.transfer_funds(from_account_id,to_account_id,amount)

    def pay_bill(self,account_id, bill_id, amount):
        self.bill_payment_service.pay_bill(account_id,bill_id,amount)
        