# Strategy Design Pattern 🎯

## What is Strategy? 🎯

The **Strategy** pattern defines a family of algorithms, encapsulates each one, and makes them **interchangeable**. It lets the algorithm vary independently from the clients that use it. Instead of hardcoding behavior with `if/else`, you inject the behavior as an object.

```
┌────────────────────────┐
│    PaymentProcessor    │       delegates to:
│       (Context)        │
├────────────────────────┤       ┌──────────────────┐
│ - strategy             │──────▶│ PaymentStrategy  │
│ + set_strategy()       │       │   (Interface)    │
│ + checkout()           │       ├──────────────────┤
└────────────────────────┘       │ + validate()     │
                                 │ + calculate_fee()│
                                 │ + pay()          │
                                 └────────┬─────────┘
                                          │
                              ┌───────────┼───────────┐
                              ▼           ▼           ▼
                        ┌──────────┐ ┌─────────┐ ┌─────────┐
                        │CreditCard│ │ PayPal  │ │ Crypto  │
                        │ Payment  │ │ Payment │ │ Payment │
                        └──────────┘ └─────────┘ └─────────┘
                          2.9% fee   $0.30+2.2%    1.0% fee
```

---

## When to Use Strategy? ⚡

| Use Case | Example |
|----------|---------|
| **Multiple algorithms** | Different sorting algorithms (bubble, quick, counting) |
| **Runtime behavior swapping** | User changes payment method at checkout |
| **Avoiding conditionals** | Replace `if/else` chains with strategy objects |
| **Algorithm isolation** | Each algorithm has its own validation, fee logic, and processing |
| **Testing** | Easily mock/swap strategies in unit tests |

### When NOT to Use 🚫
- When there's only one algorithm that will never change
- When the behavior differences are trivial (a simple `if/else` is fine)
- When adding strategy classes creates more complexity than it solves

---

## Strategy vs If/Else 📊

| Aspect | If/Else Approach | Strategy Pattern |
|--------|------------------|------------------|
| Adding new behavior | Modify existing code | Add a new strategy class |
| Open/Closed Principle | Violated | Followed |
| Code in context | `if method == "card": ...elif method == "paypal": ...` | `strategy.pay(amount)` |
| Runtime swapping | Awkward, error-prone | Built-in via `set_strategy()` |
| Testability | Hard to isolate | Each strategy testable independently |
| Single Responsibility | Context handles all logic | Each strategy handles its own logic |

---

## Basic Implementation 🛠️

### `strategy_1.py` — Sorting Strategy

A minimal strategy example where sorting algorithms are interchangeable at runtime.

```python
# Strategy Interface — defines the contract
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

# Concrete Strategies — each implements a different algorithm
class BubbleSort(SortingStrategy):
    def sort(self, array):
        print("Sorting using Bubble Sort")

class QuickSort(SortingStrategy):
    def sort(self, array):
        print("Sorting using Quick Sort")

class CountingSort(SortingStrategy):
    def sort(self, array):
        print("Sorting using Counting Sort")

# Context — holds a strategy and delegates to it
class Context():
    def __init__(self, sorting_strategy: SortingStrategy = None):
        self.sorting_strategy = sorting_strategy

    def update_strategy(self, new_strategy: SortingStrategy):
        self.sorting_strategy = new_strategy

    def sort(self, array):
        self.sorting_strategy.sort(array=array)

# Usage — swap strategies at runtime
sorting_context = Context(BubbleSort())
sorting_context.sort(array)             # Bubble Sort

sorting_context.update_strategy(CountingSort())
sorting_context.sort(array)             # Counting Sort
```

**Key Takeaway:** The `Context` never changes — only the strategy object it holds changes, and with it the behavior.

---

## Real-World Example: Payment Processing 💳

See `example/` for a practical strategy pattern where different payment methods each have their own validation, fee calculation, and processing logic.

### Structure

```
example/
├── main.py                # Entry point — demo with runtime strategy swapping
├── payment_strategy.py    # Strategy interface + CreditCard / PayPal / Crypto strategies
└── payment_processor.py   # Context — delegates checkout to the active strategy
```

### How It Works

```python
# Strategy Interface — contract for all payment methods
class PaymentStrategy(ABC):
    def validate(self, amount: float) -> bool: ...
    def calculate_fee(self, amount: float) -> float: ...
    def pay(self, amount: float) -> str: ...

# Concrete Strategy — Credit Card with 2.9% fee
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, cardholder_name: str):
        self.card_number = card_number
        self.cardholder_name = cardholder_name

    def validate(self, amount: float) -> bool:
        return len(self.card_number) == 16 and amount > 0

    def calculate_fee(self, amount: float) -> float:
        return round(amount * 0.029, 2)

    def pay(self, amount: float) -> str:
        fee = self.calculate_fee(amount)
        return f"Charged ${amount + fee} to ****{self.card_number[-4:]}"

# Context — delegates all payment operations to the active strategy
class PaymentProcessor():
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def checkout(self, amount: float) -> str:
        if not self.strategy.validate(amount):
            return "Payment failed: validation error"
        return self.strategy.pay(amount)

# Usage — start with credit card, swap to PayPal at runtime
processor = PaymentProcessor(CreditCardPayment("4111111111111234", "Alice"))
print(processor.checkout(100.00))  # Credit Card: $102.90

processor.set_strategy(PayPalPayment(email="alice@example.com"))
print(processor.checkout(75.50))   # PayPal: $77.46
```

### Fee Comparison

| Payment Method | Fee Structure | $100.00 Payment | Total Charged |
|---------------|---------------|-----------------|---------------|
| **Credit Card** | 2.9% | $2.90 | $102.90 |
| **PayPal** | $0.30 + 2.2% | $2.50 | $102.50 |
| **Crypto** | 1.0% | $1.00 | $101.00 |

### Sample Output

```
20:39:45 | INFO | __main__              | === Strategy Pattern — Payment Processing Example ===
20:39:45 | INFO | __main__              | --- Credit Card ---
20:39:45 | INFO | payment_strategy      | CreditCardPayment strategy created for Alice
20:39:45 | INFO | payment_processor     | PaymentProcessor created with CreditCardPayment
20:39:45 | INFO | payment_processor     | Processing checkout for $100.00
20:39:45 | INFO | payment_processor     | Fee: $2.90 | Total: $102.90
20:39:45 | INFO | payment_strategy      | Charged $102.90 (fee: $2.90) to card ****1234
20:39:45 | INFO | __main__              | Result: Credit Card payment of $102.9 (includes $2.9 fee) charged to ****1234
20:39:45 | INFO | __main__              | --- PayPal (runtime swap) ---
20:39:45 | INFO | payment_strategy      | PayPalPayment strategy created for alice@example.com
20:39:45 | INFO | payment_processor     | Switching payment strategy to PayPalPayment
20:39:45 | INFO | payment_processor     | Processing checkout for $75.50
20:39:45 | INFO | payment_processor     | Fee: $1.96 | Total: $77.46
20:39:45 | INFO | payment_strategy      | Charged $77.46 (fee: $1.96) via PayPal to alice@example.com
20:39:45 | INFO | __main__              | Result: PayPal payment of $77.46 (includes $1.96 fee) sent to alice@example.com
20:39:45 | INFO | __main__              | --- Crypto (runtime swap) ---
20:39:45 | INFO | payment_strategy      | CryptoPayment strategy created for wallet 1A1zP1eP...
20:39:45 | INFO | payment_processor     | Switching payment strategy to CryptoPayment
20:39:45 | INFO | payment_processor     | Processing checkout for $250.00
20:39:45 | INFO | payment_processor     | Fee: $2.50 | Total: $252.50
20:39:45 | INFO | payment_strategy      | Transferred $252.50 (fee: $2.50) to wallet 1A1zP1eP...vfNa
20:39:45 | INFO | __main__              | Result: Crypto payment of $252.5 (includes $2.5 fee) sent to 1A1zP1eP...vfNa
20:39:45 | INFO | __main__              | --- Validation Failure ---
20:39:45 | INFO | payment_strategy      | CreditCardPayment strategy created for Bob
20:39:45 | INFO | payment_processor     | Switching payment strategy to CreditCardPayment
20:39:45 | INFO | payment_processor     | Processing checkout for $50.00
20:39:45 | WARNING | payment_strategy   | Invalid card number
20:39:45 | INFO | __main__              | Result: Payment failed: validation error
```

---

## Design Principles at Play 📐

| Principle | How Strategy Applies |
|-----------|----------------------|
| **Open/Closed** | Add a new payment method (e.g., BankTransfer) without modifying `PaymentProcessor` or existing strategies |
| **Single Responsibility** | Each strategy encapsulates its own validation, fee calculation, and processing |
| **Dependency Inversion** | `PaymentProcessor` depends on `PaymentStrategy` abstraction, not on `CreditCardPayment` or `PayPalPayment` |
| **Liskov Substitution** | Any concrete strategy can replace `PaymentStrategy` without breaking the processor |
| **Favor Composition** | Context *has-a* strategy (composition) rather than *is-a* (inheritance) |

---

## Running the Examples ▶️

```bash
# Run the basic sorting strategy example
python strategy_design_pattern/src/strategy_1.py

# Run the payment processing example
cd strategy_design_pattern
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Strategy = Interchangeable Algorithms** — Encapsulate each behavior and swap at runtime
2. **Context Stays Clean** — It delegates to the strategy, never contains algorithm logic itself
3. **No If/Else Chains** — Each algorithm lives in its own class, not in a growing conditional
4. **Runtime Flexibility** — Swap strategies on the fly (e.g., user changes payment method at checkout)
5. **Easy to Extend** — New strategy = new class, zero changes to context or existing strategies
