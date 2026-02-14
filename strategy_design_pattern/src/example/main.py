import logging

from src.example.payment_strategy import CreditCardPayment, PayPalPayment, CryptoPayment
from src.example.payment_processor import PaymentProcessor

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("=== Strategy Pattern — Payment Processing Example ===")

    # --- Credit Card Payment ---
    logger.info("--- Credit Card ---")
    cc_strategy = CreditCardPayment(card_number="4111111111111234", cardholder_name="Alice")
    processor = PaymentProcessor(strategy=cc_strategy)
    result = processor.checkout(amount=100.00)
    logger.info("Result: %s", result)

    # --- Swap to PayPal at runtime ---
    logger.info("--- PayPal (runtime swap) ---")
    paypal_strategy = PayPalPayment(email="alice@example.com")
    processor.set_strategy(paypal_strategy)
    result = processor.checkout(amount=75.50)
    logger.info("Result: %s", result)

    # --- Swap to Crypto at runtime ---
    logger.info("--- Crypto (runtime swap) ---")
    crypto_strategy = CryptoPayment(wallet_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
    processor.set_strategy(crypto_strategy)
    result = processor.checkout(amount=250.00)
    logger.info("Result: %s", result)

    # --- Validation failure: invalid card ---
    logger.info("--- Validation Failure ---")
    bad_cc = CreditCardPayment(card_number="1234", cardholder_name="Bob")
    processor.set_strategy(bad_cc)
    result = processor.checkout(amount=50.00)
    logger.info("Result: %s", result)
