

from src.example.bank import Bank


if __name__=='__main__':
    bank=Bank()
    bank.get_account_details('123456789')
    bank.transfer_funds('123456789','987654321',100.00)
    bank.pay_bill('123456789','BILL001',59.99)