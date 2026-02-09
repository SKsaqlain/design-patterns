from abc import ABC, abstractmethod


# Product Interface — defines the contract that all concrete accounts must follow.
# Any new account type (e.g., StudentAccount) just needs to implement these 4 methods.
class BankAccount(ABC):

    # Returns the human-readable name of the account type
    @abstractmethod
    def get_account_type(self) -> str:
        pass

    # Validates whether the given customer name meets this account's requirements
    @abstractmethod
    def validate_user_identity(self, name: str) -> bool:
        pass

    # Returns the annual interest rate specific to this account type
    @abstractmethod
    def calculate_interest_rate(self) -> float:
        pass

    # Orchestrates validation + registration, returns a status message
    @abstractmethod
    def register_account(self, name: str) -> str:
        pass


# Factory Interface (Creator) — declares the factory method that subclasses override.
# Each concrete factory decides which BankAccount subclass to instantiate.
class BankAccountFactory(ABC):

    # Factory method — subclasses return the specific account type they are responsible for
    @abstractmethod
    def create_bank_account(self) -> BankAccount:
        pass