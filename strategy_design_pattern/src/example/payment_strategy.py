import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# --- Strategy Interface ---
# Defines the contract all payment strategies must follow.
# Each strategy handles its own validation, fee calculation, and processing.
class PaymentStrategy(ABC):

    # Validate payment details before processing
    @abstractmethod
    def validate(self, amount: float) -> bool:
        pass

    # Calculate the transaction fee for this payment method
    @abstractmethod
    def calculate_fee(self, amount: float) -> float:
        pass

    # Process the actual payment
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# --- Concrete Strategy A ---
# Processes payments via credit card with a 2.9% transaction fee.
class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number: str, cardholder_name: str):
        self.card_number = card_number
        self.cardholder_name = cardholder_name
        logger.info("CreditCardPayment strategy created for %s", cardholder_name)

    def validate(self, amount: float) -> bool:
        # Card number must be 16 digits and amount must be positive
        if len(self.card_number) != 16 or not self.card_number.isdigit():
            logger.warning("Invalid card number")
            return False
        if amount <= 0:
            logger.warning("Amount must be positive")
            return False
        return True

    def calculate_fee(self, amount: float) -> float:
        # 2.9% processing fee
        return round(amount * 0.029, 2)

    def pay(self, amount: float) -> str:
        fee = self.calculate_fee(amount)
        total = round(amount + fee, 2)
        masked_card = f"****{self.card_number[-4:]}"
        logger.info("Charged $%.2f (fee: $%.2f) to card %s", total, fee, masked_card)
        return f"Credit Card payment of ${total} (includes ${fee} fee) charged to {masked_card}"


# --- Concrete Strategy B ---
# Processes payments via PayPal with a flat $0.30 + 2.2% fee.
class PayPalPayment(PaymentStrategy):

    def __init__(self, email: str):
        self.email = email
        logger.info("PayPalPayment strategy created for %s", email)

    def validate(self, amount: float) -> bool:
        # Email must contain @ and amount must be positive
        if "@" not in self.email:
            logger.warning("Invalid PayPal email")
            return False
        if amount <= 0:
            logger.warning("Amount must be positive")
            return False
        return True

    def calculate_fee(self, amount: float) -> float:
        # Flat $0.30 + 2.2% processing fee
        return round(0.30 + amount * 0.022, 2)

    def pay(self, amount: float) -> str:
        fee = self.calculate_fee(amount)
        total = round(amount + fee, 2)
        logger.info("Charged $%.2f (fee: $%.2f) via PayPal to %s", total, fee, self.email)
        return f"PayPal payment of ${total} (includes ${fee} fee) sent to {self.email}"


# --- Concrete Strategy C ---
# Processes payments via cryptocurrency with a 1.0% network fee.
class CryptoPayment(PaymentStrategy):

    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
        logger.info("CryptoPayment strategy created for wallet %s", wallet_address[:8] + "...")

    def validate(self, amount: float) -> bool:
        # Wallet address must be at least 26 characters and amount must be positive
        if len(self.wallet_address) < 26:
            logger.warning("Invalid wallet address")
            return False
        if amount <= 0:
            logger.warning("Amount must be positive")
            return False
        return True

    def calculate_fee(self, amount: float) -> float:
        # 1.0% network fee
        return round(amount * 0.01, 2)

    def pay(self, amount: float) -> str:
        fee = self.calculate_fee(amount)
        total = round(amount + fee, 2)
        short_wallet = f"{self.wallet_address[:8]}...{self.wallet_address[-4:]}"
        logger.info("Transferred $%.2f (fee: $%.2f) to wallet %s", total, fee, short_wallet)
        return f"Crypto payment of ${total} (includes ${fee} fee) sent to {short_wallet}"
