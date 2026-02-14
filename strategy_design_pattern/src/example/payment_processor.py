import logging

from src.example.payment_strategy import PaymentStrategy

logger = logging.getLogger(__name__)


# --- Context ---
# Holds a payment strategy and delegates all payment operations to it.
# The strategy can be swapped at runtime (e.g., user changes payment method at checkout).
class PaymentProcessor():

    def __init__(self, strategy: PaymentStrategy):
        # Set the initial payment strategy
        self.strategy = strategy
        logger.info("PaymentProcessor created with %s", type(strategy).__name__)

    # Swap the payment strategy at runtime
    def set_strategy(self, strategy: PaymentStrategy):
        logger.info("Switching payment strategy to %s", type(strategy).__name__)
        self.strategy = strategy

    # Validate, calculate fee, and process payment — all delegated to the strategy
    def checkout(self, amount: float) -> str:
        logger.info("Processing checkout for $%.2f", amount)

        # Step 1: Validate payment details
        if not self.strategy.validate(amount):
            return "Payment failed: validation error"

        # Step 2: Show fee breakdown
        fee = self.strategy.calculate_fee(amount)
        logger.info("Fee: $%.2f | Total: $%.2f", fee, round(amount + fee, 2))

        # Step 3: Process the payment
        return self.strategy.pay(amount)
