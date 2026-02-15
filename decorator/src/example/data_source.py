from abc import ABC, abstractmethod


# --- Component Interface ---
# Defines the base interface for all data sources and their decorators.
class DataSource(ABC):

    # Subclasses must implement how data is fetched
    @abstractmethod
    def fetch_data(self) -> str:
        pass
