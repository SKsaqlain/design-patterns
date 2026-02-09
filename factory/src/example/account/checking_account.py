from src.example.account.bank_account import BankAccount, BankAccountFactory


# Concrete Product — implements BankAccount for checking accounts.
# Checking accounts have a lower interest rate (1.5%) since they're used for daily transactions.
class CheckingAccount(BankAccount):

    def get_account_type(self) -> str:
        return "Checking Account"

    # Same basic validation as saving — name must not be empty
    def validate_user_identity(self, name: str) -> bool:
        return len(name) > 0

    # Lower rate than saving accounts, reflecting the transactional nature
    def calculate_interest_rate(self) -> float:
        return 1.5

    # Validates first, then builds a confirmation message with the interest rate
    def register_account(self, name: str) -> str:
        if not self.validate_user_identity(name):
            return "Registration failed: invalid name"
        rate = self.calculate_interest_rate()
        return f"{self.get_account_type()} registered for '{name}' with {rate}% interest rate"


# Concrete Factory — creates CheckingAccount instances.
# Adding this factory required zero changes to Bank or BankAccountFactory.
class CheckingAccountFactory(BankAccountFactory):
    def create_bank_account(self) -> CheckingAccount:
        return CheckingAccount()