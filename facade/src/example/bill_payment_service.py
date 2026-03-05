class BillPaymentService:
    def __init__(self):
        pass

    def pay_bill(self,account_id,bill_id,amount):
        print(f"Paying bill :{bill_id} from account: {account_id} with amount: {amount}")