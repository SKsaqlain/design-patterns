import logging
from abc import ABC, abstractmethod

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


# --- Strategy Interface ---
# Defines the common interface for all sorting algorithms.
class SortingStrategy(ABC):

    @abstractmethod
    def sort(self, array):
        pass


# --- Concrete Strategy A ---
# Implements sorting using bubble sort algorithm.
class BubbleSort(SortingStrategy):

    def sort(self, array):
        logger.info("Sorting array using Bubble Sort strategy")


# --- Concrete Strategy B ---
# Implements sorting using quick sort algorithm.
class QuickSort(SortingStrategy):

    def sort(self, array):
        logger.info("Sorting array using Quick Sort strategy")


# --- Concrete Strategy C ---
# Implements sorting using counting sort algorithm.
class CountingSort(SortingStrategy):

    def sort(self, array):
        logger.info("Sorting array using Counting Sort strategy")


# --- Context ---
# Holds a reference to a strategy and delegates sorting to it.
# The strategy can be swapped at runtime without changing the context.
class Context():

    def __init__(self, sorting_strategy: SortingStrategy = None):
        self.sorting_strategy = sorting_strategy
        logger.info("Context created with %s", type(sorting_strategy).__name__ if sorting_strategy else "no strategy")

    # Swap the current strategy at runtime
    def update_strategy(self, new_strategy: SortingStrategy):
        logger.info("Switching strategy to %s", type(new_strategy).__name__)
        self.sorting_strategy = new_strategy

    # Delegate sorting to whichever strategy is currently set
    def sort(self, array):
        if self.sorting_strategy is None:
            logger.warning("No sorting strategy set")
            return
        self.sorting_strategy.sort(array=array)


if __name__ == '__main__':
    logger.info("=== Strategy Pattern — Sorting Example ===")

    array = list(range(10))

    # Start with BubbleSort strategy
    sorting_context = Context(BubbleSort())
    sorting_context.sort(array=array)

    # Swap to CountingSort at runtime — same context, different behavior
    sorting_context.update_strategy(CountingSort())
    sorting_context.sort(array=array)