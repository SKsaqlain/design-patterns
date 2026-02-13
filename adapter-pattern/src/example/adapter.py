from abc import ABC, abstractmethod


# --- Target Interface ---
# Defines the unified interface that all adapters must implement.
# Client code depends on this abstraction, not on any specific CRM API.
class Adapter(ABC):

    # Each adapter must translate its CRM's data into a common Customer format
    @abstractmethod
    def get_customer_data(self):
        pass