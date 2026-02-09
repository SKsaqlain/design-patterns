from src.example.account.bank_account import BankAccount, BankAccountFactory


# Concrete Product — implements BankAccount for business accounts.
# Business accounts have stricter validation (min 3-char name) and a moderate interest rate (3.0%).
class BusinessAccount(BankAccount):

    def get_account_type(self) -> str:
        return "Business Account"

    # Stricter than personal accounts — business name must be at least 3 characters
    def validate_user_identity(self, name: str) -> bool:
        return len(name) >= 3

    # Mid-range rate — higher than checking, lower than saving
    def calculate_interest_rate(self) -> float:
        return 3.0

    # Custom error message reflecting the stricter business name requirement
    def register_account(self, name: str) -> str:
        if not self.validate_user_identity(name):
            return "Registration failed: business name must be at least 3 characters"
        rate = self.calculate_interest_rate()
        return f"{self.get_account_type()} registered for '{name}' with {rate}% interest rate"


# Concrete Factory — creates BusinessAccount instances.
# Demonstrates Open/Closed Principle: we added a new account type
# without modifying any existing code.
class BusinessAccountFactory(BankAccountFactory):
    def create_bank_account(self) -> BusinessAccount:
        return BusinessAccount()