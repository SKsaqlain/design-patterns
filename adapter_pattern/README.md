# Adapter Design Pattern 🔌

## What is Adapter? 🎯

The **Adapter** pattern converts the interface of one class into another interface that clients expect. It lets classes work together that otherwise couldn't because of **incompatible interfaces** — like a power adapter that lets a US plug fit into a European socket.

```
┌─────────────────────────┐       ┌─────────────────────────┐
│        Client           │       │     Adapter (Target)    │
│                         │       │                         │
│ process_customer_data() │──────▶│   get_customer_data()   │
└─────────────────────────┘       └──────────┬──────────────┘
                                             │
                                   ┌─────────┴──────────┐
                                   ▼                    ▼
                          ┌──────────────┐    ┌──────────────────┐
                          │ NetSuite     │    │ BusinessCentral  │
                          │ Adapter      │    │ Adapter          │
                          └──────┬───────┘    └────────┬─────────┘
                                 │                     │
                                 ▼                     ▼
                          ┌──────────────┐    ┌──────────────────┐
                          │ NetSuiteApi  │    │BusinessCentralApi│
                          │  (Adaptee)   │    │   (Adaptee)      │
                          └──────────────┘    └──────────────────┘
```

---

## When to Use Adapter? ⚡

| Use Case | Example |
|----------|---------|
| **Incompatible interfaces** | Integrating a legacy system with new code |
| **Third-party API wrapping** | Normalizing responses from different CRM APIs |
| **Data format translation** | Converting XML responses to match a JSON-based system |
| **Replacing a service** | Swapping from one payment provider to another without changing client code |
| **Unified interface** | Making multiple APIs look the same to client code |

### When NOT to Use 🚫
- When interfaces are already compatible (just use the class directly)
- When you can modify the source code of the class you're adapting
- When the complexity of an adapter outweighs the benefit (one-off usage)

---

## Basic Implementation 🛠️

### `adapter_pattern_1.py` — Printer Adapter

A minimal adapter example where a `LegacyPrinter` has `print_document()` but the client expects `print()`.

```python
# Adaptee — existing class with incompatible interface
class LegacyPrinter():
    def print_document(self):
        print("Legacy Printer is printing a document")

# Target Interface — what the client expects
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

# Adapter — wraps the adaptee and translates the interface
class PrinterAdapter(Printer):
    def __init__(self):
        self.legacy_printer = LegacyPrinter()

    def print(self):
        self.legacy_printer.print_document()  # Delegates to adaptee

# Client — works with any Printer, doesn't know about LegacyPrinter
def client(printer: Printer):
    printer.print()

# Usage — client uses adapter, which internally calls LegacyPrinter
adapter = PrinterAdapter()
client(adapter)  # "Legacy Printer is printing a document"
```

**Key Takeaway:** The client calls `print()`, the adapter translates it to `print_document()` — the legacy class never changes.

---

## Real-World Example: CRM Integration 🌐

See `example/` for a practical adapter pattern that normalizes customer data from two different CRM systems (NetSuite and Business Central) into a unified `Customer` dataclass.

### Structure

```
example/
├── main.py                      # Entry point — demo with both CRM adapters
├── adapter.py                   # Target Interface (abstract)
├── customer.py                  # Unified data model (dataclass)
├── client.py                    # Client — works with any Adapter
├── net_suite_api.py             # Adaptee A — NetSuite CRM API
├── net_suite_adapter.py         # Adapter A — NetSuite → Customer
├── business_central_api.py      # Adaptee B — Business Central CRM API
└── business_central_adapter.py  # Adapter B — Business Central → Customer
```

### How It Works

```python
# Unified Data Model — what the client expects
@dataclass
class Customer():
    id: str
    full_name: str
    email: str
    status: str

# Target Interface — all adapters must implement this
class Adapter(ABC):
    @abstractmethod
    def get_customer_data(self) -> Customer: ...

# Adaptee A — NetSuite returns {customer_id, name, email, status}
class NetSuiteApi():
    def get_customer(self):
        return {"customer_id": "101", "name": "Alice", ...}

# Adapter A — translates NetSuite fields → Customer fields
class NetSuiteAdapter(Adapter):
    def __init__(self, net_suite_api):
        self.net_suite_api = net_suite_api

    def get_customer_data(self) -> Customer:
        data = self.net_suite_api.get_customer()
        return Customer(
            id=data["customer_id"],       # customer_id → id
            full_name=data["name"],       # name → full_name
            email=data["email"],
            status=data["status"]
        )

# Client — works with any adapter, doesn't know which CRM is behind it
class Client():
    def __init__(self, adapter: Adapter):
        self.adapter = adapter

    def process_customer_data(self):
        return self.adapter.get_customer_data()

# Usage — same Client code, different adapters for different CRMs
net_client = Client(adapter=NetSuiteAdapter(NetSuiteApi()))
print(net_client.process_customer_data())
# Customer(id='101', full_name='Alice', email='alice@example.com', status='ACTIVE')

bc_client = Client(adapter=BusinessCentralAdapter(BusinessCentralApi()))
print(bc_client.process_customer_data())
# Customer(id='201', full_name='Bob', email='bob@example.com', status='ACTIVE')
```

### Field Mapping

Each CRM API uses different field names. The adapters handle the translation:

| Customer Field | NetSuite API | Business Central API |
|---------------|-------------|---------------------|
| `id` | `customer_id` | `customerId` |
| `full_name` | `name` | `fullName` |
| `email` | `email` | `emailID` |
| `status` | `status` | `status` |

### Sample Output

```
21:00:00 | INFO | __main__              | === Adapter Pattern — CRM Integration Example ===
21:00:00 | INFO | __main__              | --- NetSuite ---
21:00:00 | INFO | net_suite_adapter     | NetSuiteAdapter created
21:00:00 | INFO | client                | Client created with NetSuiteAdapter
21:00:00 | INFO | client                | Client processing customer data
21:00:00 | INFO | net_suite_adapter     | Adapting NetSuite data → Customer
21:00:00 | INFO | net_suite_api         | Fetching customer data from NetSuite API
21:00:00 | INFO | __main__              | Result: Customer(id='101', full_name='Alice', email='alice@example.com', status='ACTIVE')
21:00:00 | INFO | __main__              | --- Business Central ---
21:00:00 | INFO | business_central_adapter | BusinessCentralAdapter created
21:00:00 | INFO | client                | Client created with BusinessCentralAdapter
21:00:00 | INFO | client                | Client processing customer data
21:00:00 | INFO | business_central_adapter | Adapting Business Central data → Customer
21:00:00 | INFO | business_central_api  | Fetching customer data from Business Central API
21:00:00 | INFO | __main__              | Result: Customer(id='201', full_name='Bob', email='bob@example.com', status='ACTIVE')
```

---

## Design Principles at Play 📐

| Principle | How Adapter Applies |
|-----------|---------------------|
| **Open/Closed** | Add a new CRM (e.g., Salesforce) by creating a new adapter — no existing code changes |
| **Dependency Inversion** | Client depends on `Adapter` abstraction, not on `NetSuiteApi` or `BusinessCentralApi` |
| **Single Responsibility** | Each adapter handles translation for one CRM only |
| **Liskov Substitution** | Any adapter (`NetSuiteAdapter`, `BusinessCentralAdapter`) can replace `Adapter` seamlessly |

---

## Quick Comparison: With vs Without Adapter 📊

| Aspect | Without Adapter | With Adapter |
|--------|----------------|--------------|
| Adding new CRM | Modify client with new `if/else` | Add new adapter class only |
| Client coupling | Knows all API field names | Knows only `Customer` dataclass |
| Open/Closed Principle | Violated | Followed |
| Code in client | `if crm == "netsuite": data["customer_id"]` | `adapter.get_customer_data()` |
| Testability | Hard to mock CRM APIs | Easy to inject mock adapters |

---

## Running the Examples ▶️

```bash
# Run the basic printer adapter example
python adapter_pattern/src/adapter_pattern_1.py

# Run the CRM integration example
cd adapter_pattern
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Adapter = Interface Translator** — Converts one interface into another the client expects
2. **Adaptee Never Changes** — The legacy/third-party class stays untouched
3. **Client Stays Clean** — It only knows the target interface, not the adaptee's details
4. **Easy to Extend** — New source system = new adapter, zero changes to client or existing adapters
