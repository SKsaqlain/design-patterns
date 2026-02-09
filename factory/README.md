# Factory Design Pattern 🏭

## What is Factory Method? 🎯

The **Factory Method** pattern defines an interface for creating objects, but lets **subclasses decide** which class to instantiate. Instead of calling `new` directly, the client delegates creation to a factory — decoupling the "what to create" from the "how to use it".

```
┌─────────────────────────────┐       ┌─────────────────────────────┐
│     BankAccountFactory      │       │        BankAccount          │
│         (Creator)           │       │        (Product)            │
├─────────────────────────────┤       ├─────────────────────────────┤
│ + create_bank_account()     │──────▶│ + get_account_type()        │
└──────────┬──────────────────┘       │ + calculate_interest_rate() │
           │                          │ + register_account()        │
     ┌─────┴──────┐                   └──────────┬──────────────────┘
     │            │                          ┌────┴─────┐
     ▼            ▼                          ▼          ▼
┌──────────┐ ┌──────────┐            ┌──────────┐ ┌──────────┐
│ Saving   │ │ Checking │            │ Saving   │ │ Checking │
│ Factory  │ │ Factory  │            │ Account  │ │ Account  │
└──────────┘ └──────────┘            └──────────┘ └──────────┘
```

---

## When to Use Factory Method? ⚡

| Use Case | Example |
|----------|---------|
| **Object type decided at runtime** | Different account types based on user input |
| **Decouple creation from usage** | Client code shouldn't know concrete classes |
| **Adding new types frequently** | New product types without modifying existing code |
| **Complex object construction** | Creation logic involves validation, setup steps |
| **Framework/library design** | Let users extend with their own implementations |

### When NOT to Use 🚫
- When there's only one type of object to create
- When creation logic is simple and unlikely to change
- When it adds unnecessary abstraction for a small project

---

## Basic Implementation 🛠️

### `factory_1.py` — Vehicle Factory

A minimal factory method example with `Car` and `Bike` products.

```python
# Abstract Product
class Vehical(ABC):
    @abstractmethod
    def get_vehical_type(self) -> str:
        pass

# Concrete Products
class Car(Vehical):
    def get_vehical_type(self) -> str:
        return "Car"

class Bike(Vehical):
    def get_vehical_type(self) -> str:
        return "Bike"

# Abstract Factory (Creator)
class VehicalFactory(ABC):
    @abstractmethod
    def create_vehical(self):
        pass

# Concrete Factories
class CarFactory(VehicalFactory):
    def create_vehical(self):
        return Car()

class BikeFactory(VehicalFactory):
    def create_vehical(self):
        return Bike()

# Client — depends only on the factory abstraction
class Client:
    def __init__(self, vehical_factory: VehicalFactory):
        self.vehical = vehical_factory.create_vehical()

# Usage — swap factories without changing client code
client = Client(CarFactory())
print(client.get_vehical().get_vehical_type())   # Car

client = Client(BikeFactory())
print(client.get_vehical().get_vehical_type())   # Bike
```

**Key Takeaway:** The `Client` never imports or references `Car` or `Bike` directly. It only knows about `VehicalFactory`.

---

## Real-World Example: Bank Accounts 🏦

See `example/` for a practical factory method with multiple account types, each having different interest rates and validation rules.

### Structure

```
example/
├── main.py                        # Client (Bank) + demo runs
└── account/
    ├── bank_account.py            # Abstract Product + Abstract Factory
    ├── saving_account.py          # 4.5% interest, basic validation
    ├── checking_account.py        # 1.5% interest, basic validation
    └── business_account.py        # 3.0% interest, stricter validation (min 3 chars)
```

### How It Works

```python
# Abstract Product — the contract all accounts follow
class BankAccount(ABC):
    def get_account_type(self) -> str: ...
    def validate_user_identity(self, name: str) -> bool: ...
    def calculate_interest_rate(self) -> float: ...
    def register_account(self, name: str) -> str: ...

# Abstract Factory — declares the factory method
class BankAccountFactory(ABC):
    def create_bank_account(self) -> BankAccount: ...

# Concrete Product — each account type has its own rules
class SavingAccount(BankAccount):
    def calculate_interest_rate(self) -> float:
        return 4.5  # Highest rate to encourage deposits

# Concrete Factory — creates the specific account
class SavingAccountFactory(BankAccountFactory):
    def create_bank_account(self) -> SavingAccount:
        return SavingAccount()

# Client — depends only on BankAccountFactory, not on any concrete account
class Bank:
    def __init__(self, account_factory: BankAccountFactory):
        self.account = account_factory.create_bank_account()

    def open_account(self, customer_name: str) -> str:
        return self.account.register_account(customer_name)

# Usage — same Bank code, different factories produce different accounts
bank = Bank(SavingAccountFactory())
print(bank.open_account("Alice"))
# Saving Account registered for 'Alice' with 4.5% interest rate

bank = Bank(BusinessAccountFactory())
print(bank.open_account("Acme Corp"))
# Business Account registered for 'Acme Corp' with 3.0% interest rate
```

### Sample Output

```
--- Saving Account ---
Account Type    : Saving Account
Interest Rate   : 4.5%
Open Account    : Saving Account registered for 'Alice' with 4.5% interest rate

--- Checking Account ---
Account Type    : Checking Account
Interest Rate   : 1.5%
Open Account    : Checking Account registered for 'Bob' with 1.5% interest rate

--- Business Account ---
Account Type    : Business Account
Interest Rate   : 3.0%
Open Account    : Business Account registered for 'Acme Corp' with 3.0% interest rate

--- Validation: empty name ---
Result          : Registration failed: invalid name

--- Validation: short business name ---
Result          : Registration failed: business name must be at least 3 characters
```

---

## Design Principles at Play 📐

| Principle | How Factory Method Applies |
|-----------|---------------------------|
| **Open/Closed** | Add new account types (e.g., `StudentAccount`) without modifying `Bank` or `BankAccountFactory` |
| **Dependency Inversion** | `Bank` depends on `BankAccountFactory` abstraction, not on `SavingAccount` / `CheckingAccount` |
| **Single Responsibility** | Each factory has one job — create its specific product |
| **Program to Interfaces** | Client code works with `BankAccount` and `BankAccountFactory`, never with concrete classes |

---

## Quick Comparison: Factory vs Direct Instantiation 📊

| Aspect | Direct (`if/else`) | Factory Method |
|--------|---------------------|----------------|
| Adding new types | Modify existing code | Add new classes only |
| Client coupling | Knows all concrete classes | Knows only the abstraction |
| Open/Closed Principle | Violated | Followed |
| Code in client | `if type == "saving": SavingAccount()` | `factory.create_bank_account()` |
| Testability | Hard to mock | Easy to inject mock factories |

---

## Running the Examples ▶️

```bash
# Run the basic vehicle factory example
cd factory
python -m src.factory_1

# Run the bank account example
cd factory
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Factory Method = Delegate Creation** — Subclasses decide what to instantiate
2. **Client Stays Clean** — It never references concrete product classes
3. **Easy to Extend** — New product + new factory = done, no existing code touched
4. **Swap at Runtime** — Pass a different factory to get a completely different product
