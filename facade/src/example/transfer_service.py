class TransferService:
    def __init__(self):
        pass

    def transfer_funds(self,from_account_id, to_account_id,amount):
        print(f"Transferring amount:{amount} from : {from_account_id} to: {to_account_id}")