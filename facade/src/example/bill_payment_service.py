import logging

logger = logging.getLogger(__name__)


# Subsystem service — handles bill payments from an account
class BillPaymentService:
    def __init__(self):
        logger.info("BillPaymentService initialized")

    def pay_bill(self, account_id, bill_id, amount):
        logger.info(f"Paying bill {bill_id} from account {account_id} with amount ${amount}")
