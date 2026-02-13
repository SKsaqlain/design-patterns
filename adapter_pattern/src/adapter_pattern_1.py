import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


# --- Adaptee ---
# The existing (legacy) class with an incompatible interface.
# Its method is `print_document()`, but the client expects `print()`.
class LegacyPrinter():
    def print_document(self):
        logger.info("Legacy Printer is printing a document")


# --- Target Interface ---
# The interface the client code expects all printers to follow.
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass


# --- Adapter ---
# Wraps the LegacyPrinter and translates `print()` calls into `print_document()`.
# This lets the client use the legacy printer without knowing its actual interface.
class PrinterAdapter(Printer):
    def __init__(self):
        # Compose the adaptee (LegacyPrinter) inside the adapter
        self.legacy_printer = LegacyPrinter()
        logger.info("PrinterAdapter created, wrapping LegacyPrinter")

    def print(self):
        # Delegate the call to the adaptee's incompatible method
        logger.info("Adapter translating print() → print_document()")
        self.legacy_printer.print_document()


# --- Client ---
# Works with any Printer — doesn't know or care about the legacy interface.
def client(printer: Printer):
    logger.info("Client calling print()")
    printer.print()


if __name__ == '__main__':
    logger.info("=== Adapter Pattern — Printer Example ===")
    # Client uses the adapter, which internally delegates to LegacyPrinter
    adapter = PrinterAdapter()
    client(adapter)