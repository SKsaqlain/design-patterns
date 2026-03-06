import logging

logger = logging.getLogger(__name__)


# Subsystem service — handles account lookup operations
class AccountService:
    def __init__(self):
        logger.info("AccountService initialized")

    def getAccountDetails(self, account_id):
        logger.info(f"Fetching account details for account Id: {account_id}")
