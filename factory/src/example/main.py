from src.example.account.bank_account import BankAccountFactory, BankAccount
from src.example.account.saving_account import SavingAccountFactory
from src.example.account.checking_account import CheckingAccountFactory
from src.example.account.business_account import BusinessAccountFactory


# Bank is the Client class in the Factory pattern.
# It depends only on the BankAccountFactory abstraction, not on
# any concrete account class — so it works with any account type.
class Bank:
    def __init__(self, account_factory: BankAccountFactory):
        # Delegates object creation to the injected factory
        self.account = account_factory.create_bank_account()

    def open_account(self, customer_name: str) -> str:
        # Uses the created account to register — doesn't care which type it is
        return self.account.register_account(customer_name)

    def get_account(self) -> BankAccount:
        return self.account


def main():
    print("=" * 50)
    print("  Factory Design Pattern — Bank Account Example")
    print("=" * 50)

    # --- Saving Account ---
    # Pass a SavingAccountFactory to Bank; it creates a SavingAccount internally
    print("\n--- Saving Account ---")
    bank = Bank(SavingAccountFactory())
    print(f"Account Type    : {bank.get_account().get_account_type()}")
    print(f"Interest Rate   : {bank.get_account().calculate_interest_rate()}%")
    print(f"Open Account    : {bank.open_account('Alice')}")

    # --- Checking Account ---
    # Swap the factory to CheckingAccountFactory — Bank code stays the same
    print("\n--- Checking Account ---")
    bank = Bank(CheckingAccountFactory())
    print(f"Account Type    : {bank.get_account().get_account_type()}")
    print(f"Interest Rate   : {bank.get_account().calculate_interest_rate()}%")
    print(f"Open Account    : {bank.open_account('Bob')}")

    # --- Business Account ---
    # Same pattern, different factory — produces a BusinessAccount
    print("\n--- Business Account ---")
    bank = Bank(BusinessAccountFactory())
    print(f"Account Type    : {bank.get_account().get_account_type()}")
    print(f"Interest Rate   : {bank.get_account().calculate_interest_rate()}%")
    print(f"Open Account    : {bank.open_account('Acme Corp')}")

    # --- Validation: empty name on Saving Account ---
    print("\n--- Validation: empty name ---")
    bank = Bank(SavingAccountFactory())
    print(f"Result          : {bank.open_account('')}")

    # --- Validation: short name on Business Account (min 3 chars) ---
    print("\n--- Validation: short business name ---")
    bank = Bank(BusinessAccountFactory())
    print(f"Result          : {bank.open_account('AB')}")

    # --- Swapping factories in a loop (core benefit of the pattern) ---
    # The exact same client code works with every factory — no if/else needed
    print("\n--- All Account Types (factory swap demo) ---")
    for factory in [SavingAccountFactory(), CheckingAccountFactory(), BusinessAccountFactory()]:
        bank = Bank(factory)
        account = bank.get_account()
        print(f"  {account.get_account_type():20s} | Interest: {account.calculate_interest_rate()}%")

    print("\n" + "=" * 50)


if __name__ == '__main__':
    main()
