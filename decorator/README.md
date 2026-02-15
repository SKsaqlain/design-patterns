# Decorator Design Pattern 🎀

## What is Decorator? 🎯

The **Decorator** pattern lets you attach new behavior to objects by wrapping them in other objects that add the behavior. Each decorator **has-a** reference to the wrapped object and **is-a** instance of the same interface — so decorators can be stacked infinitely like layers.

```
┌─────────────────────────────────────────────────┐
│              LoggingDecorator                    │
│  ┌───────────────────────────────────────────┐  │
│  │          UppercaseDecorator                │  │
│  │  ┌─────────────────────────────────────┐  │  │
│  │  │         FileDataSource              │  │  │
│  │  │         "fetching data"             │  │  │
│  │  └─────────────────────────────────────┘  │  │
│  │           → "FETCHING DATA"               │  │
│  └───────────────────────────────────────────┘  │
│         → logs before & after fetch              │
└─────────────────────────────────────────────────┘
```

---

## When to Use Decorator? ⚡

| Use Case | Example |
|----------|---------|
| **Add behavior without modifying classes** | Add logging to a data source without changing it |
| **Stack multiple behaviors** | Logging + uppercase + encryption on the same object |
| **Runtime flexibility** | Choose which decorators to apply at runtime |
| **Avoid class explosion** | Instead of `LoggedUppercaseDataSource`, `LoggedDataSource`, etc. — just stack decorators |
| **Cross-cutting concerns** | Logging, caching, validation applied uniformly |

### When NOT to Use 🚫
- When only one behavior is needed (just modify the class directly)
- When the decorator chain becomes too deep and hard to debug
- When a simple function wrapper or middleware would suffice

---

## Decorator vs Inheritance 📊

| Aspect | Inheritance | Decorator |
|--------|-------------|-----------|
| Adding behavior | Create a new subclass | Wrap with a decorator object |
| Combining behaviors | One subclass per combination (class explosion) | Stack decorators freely |
| Runtime flexibility | Fixed at compile time | Composed at runtime |
| Open/Closed | Violates (must modify hierarchy) | Follows (new decorator = new class) |
| Complexity | Simple for 1–2 variants | Better for many combinations |

---

## Basic Implementation 🛠️

### `decorator_1.py` — Coffee Shop

A minimal decorator example where toppings are stacked on a base coffee.

```python
# Component Interface — base for all coffees and decorators
class Coffee(ABC):
    def get_description(self) -> str: ...
    def get_cost(self) -> float: ...

# Concrete Component — the base object ($2.00)
class PlainCoffee(Coffee):
    def get_description(self): return "Plain Coffee"
    def get_cost(self): return 2.00

# Base Decorator — wraps a Coffee and delegates to it
class CoffeeDecorator(Coffee):
    def __init__(self, decorate_coffee: Coffee):
        self.decorate_coffee = decorate_coffee
    def get_description(self): return self.decorate_coffee.get_description()
    def get_cost(self): return self.decorate_coffee.get_cost()

# Concrete Decorators — each adds behavior on top
class Milk(CoffeeDecorator):
    def get_description(self): return self.decorate_coffee.get_description() + ', Milk'
    def get_cost(self): return self.decorate_coffee.get_cost() + 0.50

class Sugar(CoffeeDecorator):
    def get_description(self): return self.decorate_coffee.get_description() + ', Sugar'
    def get_cost(self): return self.decorate_coffee.get_cost() + 0.10

# Usage — stack decorators like layers
coffee = PlainCoffee()                   # $2.00
milk_coffee = Milk(coffee)               # $2.50
sugar_coffee = Sugar(milk_coffee)        # $2.60
print(sugar_coffee.get_description())    # Plain Coffee, Milk, Sugar
print(sugar_coffee.get_cost())           # 2.6
```

**Key Takeaway:** Each decorator wraps the previous one. The cost and description accumulate through the chain — no class needs to know about the others.

### Sample Output

```
12:45:42 | INFO | __main__              | === Decorator Pattern — Coffee Example ===
12:45:42 | INFO | __main__              | Base: Plain Coffee — $2.00
12:45:42 | INFO | __main__              | Wrapping [Plain Coffee] with Milk
12:45:42 | INFO | __main__              | After Milk: Plain Coffee, Milk — $2.50
12:45:42 | INFO | __main__              | Wrapping [Plain Coffee, Milk] with Sugar
12:45:42 | INFO | __main__              | After Sugar: Plain Coffee, Milk, Sugar — $2.60
```

---

## Real-World Example: DataSource Pipeline 🔧

See `example/` for a practical decorator pattern where a data source is progressively wrapped with transformation and logging layers.

### Structure

```
example/
├── main.py                  # Entry point — builds the decorator chain
├── data_source.py           # Component Interface (abstract)
├── file_data_source.py      # Concrete Component — raw file data
├── base_decorator.py        # Base Decorator — wraps and delegates
├── uppercase_decorator.py   # Concrete Decorator A — transforms to uppercase
└── logging_decorator.py     # Concrete Decorator B — logs before/after fetch
```

### How It Works

```python
# Component Interface — the contract for all data sources
class DataSource(ABC):
    @abstractmethod
    def fetch_data(self) -> str: ...

# Concrete Component — returns raw data
class FileDataSource(DataSource):
    def fetch_data(self) -> str:
        return "fetching data"

# Base Decorator — wraps a DataSource and delegates to it
class DataSourceDecorator(DataSource):
    def __init__(self, decorated_datasource: DataSource):
        self.decorated_datasource = decorated_datasource
    def fetch_data(self):
        return self.decorated_datasource.fetch_data()

# Concrete Decorator A — transforms data to uppercase
class UppercaseDecorator(DataSourceDecorator):
    def fetch_data(self):
        return self.decorated_datasource.fetch_data().upper()

# Concrete Decorator B — logs before and after fetch
class LoggingDecorator(DataSourceDecorator):
    def fetch_data(self):
        logger.info("Logging Fetch Action")
        data = self.decorated_datasource.fetch_data()
        logger.info("Data fetched: %s", data)
        return data

# Usage — stack decorators to build a pipeline
file_datasource = FileDataSource()             # raw: "fetching data"
uppercase = UppercaseDecorator(file_datasource) # → "FETCHING DATA"
log_decorator = LoggingDecorator(uppercase)     # → logs + "FETCHING DATA"
print(log_decorator.fetch_data())
```

### Decorator Chain

```
log_decorator.fetch_data()
    → logs "Logging Fetch Action"
    → uppercase.fetch_data()
        → file_datasource.fetch_data()
            → returns "fetching data"
        → returns "FETCHING DATA"  (uppercased)
    → logs "Data fetched: FETCHING DATA"
    → returns "FETCHING DATA"
```

### Sample Output

```
13:03:18 | INFO | __main__              | === Decorator Pattern — DataSource Example ===
13:03:18 | INFO | logging_decorator     | Logging Fetch Action
13:03:18 | INFO | logging_decorator     | Data fetched: FETCHING DATA
13:03:18 | INFO | __main__              | Final result: FETCHING DATA
```

---

## Design Principles at Play 📐

| Principle | How Decorator Applies |
|-----------|----------------------|
| **Open/Closed** | Add new behavior (e.g., `EncryptionDecorator`) without modifying existing classes |
| **Single Responsibility** | Each decorator handles one concern — logging, transformation, etc. |
| **Liskov Substitution** | Any decorator or component can be used wherever `DataSource` is expected |
| **Favor Composition** | Decorators use *has-a* (wrapping) instead of *is-a* (inheritance) to add behavior |

---

## Quick Comparison: Decorator vs Subclassing 📊

| Scenario | Subclassing | Decorator |
|----------|-------------|-----------|
| Logging only | `LoggedDataSource` | `LoggingDecorator(FileDataSource())` |
| Uppercase only | `UppercaseDataSource` | `UppercaseDecorator(FileDataSource())` |
| Logging + Uppercase | `LoggedUppercaseDataSource` | `LoggingDecorator(UppercaseDecorator(FileDataSource()))` |
| Logging + Uppercase + Encryption | `LoggedUppercaseEncryptedDataSource` | `LoggingDecorator(UppercaseDecorator(EncryptionDecorator(FileDataSource())))` |
| **Total classes needed (4 combos)** | **4 subclasses** | **3 decorators, compose freely** |

---

## Running the Examples ▶️

```bash
# Run the basic coffee decorator example
python decorator/src/decorator_1.py

# Run the data source pipeline example
cd decorator
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Decorator = Stackable Behavior** — Wrap objects with layers that each add one concern
2. **Same Interface** — Decorators implement the same interface as the component, so they're transparent to clients
3. **Composition Over Inheritance** — Stack behaviors at runtime instead of creating a subclass per combination
4. **Order Matters** — `Logging(Uppercase(File))` behaves differently from `Uppercase(Logging(File))`
5. **Easy to Extend** — New decorator = new class, zero changes to existing decorators or components
