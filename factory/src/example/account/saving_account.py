from src.example.account.bank_account import BankAccount, BankAccountFactory


# Concrete Product — implements BankAccount for saving accounts.
# Saving accounts have the highest interest rate (4.5%) and basic name validation.
class SavingAccount(BankAccount):

    def get_account_type(self) -> str:
        return "Saving Account"

    # Only requirement: name must not be empty
    def validate_user_identity(self, name: str) -> bool:
        return len(name) > 0

    # Saving accounts offer a higher interest rate to encourage deposits
    def calculate_interest_rate(self) -> float:
        return 4.5

    # Validates first, then builds a confirmation message with the interest rate
    def register_account(self, name: str) -> str:
        if not self.validate_user_identity(name):
            return "Registration failed: invalid name"
        rate = self.calculate_interest_rate()
        return f"{self.get_account_type()} registered for '{name}' with {rate}% interest rate"


# Concrete Factory — creates SavingAccount instances.
# The client (Bank) never calls SavingAccount() directly; it goes through this factory.
class SavingAccountFactory(BankAccountFactory):
    def create_bank_account(self) -> SavingAccount:
        return SavingAccount()
