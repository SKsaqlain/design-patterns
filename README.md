# Design Patterns

A collection of design pattern implementations with detailed comments and real-world examples.

---

## What are Design Patterns? 🎯

Design patterns are **reusable solutions** to common problems in software design. They're not finished code, but templates for solving problems that can be adapted to your specific situation.

---

## SOLID Principles 🧱

SOLID is a set of five design principles that help make software **maintainable, flexible, and scalable**. These principles are closely tied to design patterns — most patterns exist to help you follow one or more SOLID principles.

| Letter | Principle | What It Means |
|--------|-----------|---------------|
| **S** | **Single Responsibility** | A class should have **one reason to change** — it does one job and does it well. |
| **O** | **Open/Closed** | Classes should be **open for extension** but **closed for modification** — add new behavior without changing existing code. |
| **L** | **Liskov Substitution** | Subclasses should be **substitutable** for their parent class — swapping a subclass in should not break the program. |
| **I** | **Interface Segregation** | Clients should not be forced to depend on **interfaces they don't use** — prefer smaller, focused interfaces over large ones. |
| **D** | **Dependency Inversion** | Depend on **abstractions, not concretions** — high-level modules should not depend on low-level modules, both should depend on abstractions. |


## Project Structure 📁

```
design-patterns/
├── README.md
├── .gitignore
├── singleton/
│   ├── README.md
│   └── src/
│       ├── singleton_1.py    # @staticmethod approach
│       ├── singleton_2.py    # __new__ approach
│       ├── singleton_3.py    # @classmethod approach
│       └── example/
│           └── config.py     # Real-world config manager
├── factory/
│   ├── README.md
│   └── src/
│       ├── factory_1.py      # Basic vehicle factory
│       └── example/
│           ├── main.py       # Bank client + demo runs
│           └── account/
│               ├── bank_account.py        # Abstract Product + Factory
│               ├── saving_account.py      # 4.5% interest
│               ├── checking_account.py    # 1.5% interest
│               └── business_account.py    # 3.0% interest
├── observer/
│   ├── README.md
│   └── src/
│       ├── observer_1.py     # Basic subject-observer
│       └── example/
│           ├── main.py       # Async weather broker demo
│           ├── broker.py     # Topic management + message queue
│           ├── producer.py   # Publishes to brokers
│           └── consumer.py   # Receives messages
├── abstract_factory/
│   ├── README.md
│   └── src/
│       ├── abstract_factory_1.py   # Regional car factory
│       └── example/
│           ├── main.py             # Cloud service demo
│           ├── cloud_service.py    # Abstract + AWS/GCP/Azure factories
│           ├── virtual_machine.py  # VM product family
│           ├── database.py         # Database product family
│           └── storage.py          # Storage product family
├── adapter_pattern/
│   ├── README.md
│   └── src/
│       ├── adapter_pattern_1.py    # Basic printer adapter
│       └── example/
│           ├── main.py             # CRM integration demo
│           ├── adapter.py          # Target interface (abstract)
│           ├── customer.py         # Unified data model (dataclass)
│           ├── client.py           # Client — works with any adapter
│           ├── net_suite_api.py    # Adaptee A — NetSuite CRM
│           ├── net_suite_adapter.py        # Adapter A — NetSuite → Customer
│           ├── business_central_api.py     # Adaptee B — Business Central CRM
│           └── business_central_adapter.py # Adapter B — Business Central → Customer
├── strategy_design_pattern/
│   ├── README.md
│   └── src/
│       ├── strategy_1.py           # Basic sorting strategy
│       └── example/
│           ├── main.py             # Payment processing demo
│           ├── payment_strategy.py # Strategy interface + CreditCard/PayPal/Crypto
│           └── payment_processor.py # Context — delegates to active strategy
├── decorator/
│   ├── README.md
│   └── src/
│       ├── decorator_1.py          # Basic coffee decorator
│       └── example/
│           ├── main.py             # DataSource pipeline demo
│           ├── data_source.py      # Component interface (abstract)
│           ├── file_data_source.py # Concrete component — raw file data
│           ├── base_decorator.py   # Base decorator — wraps and delegates
│           ├── uppercase_decorator.py  # Concrete decorator — uppercase transform
│           └── logging_decorator.py    # Concrete decorator — logs fetch calls
├── builder_pattern/
│   ├── README.md
│   └── src/
│       ├── builder_1.py            # Basic computer builder
│       └── example/
│           ├── main.py             # ML pipeline demo
│           ├── ml_pipeline.py      # Product + Builder + Concrete Builder + Director
│           ├── datasource.py       # Pipeline component — DataSource + S3
│           ├── preprocessing.py    # Pipeline component — Preprocessing + Normalize
│           ├── model.py            # Pipeline component — Model + LogisticRegression
│           └── evaluation.py       # Pipeline component — Evaluation + F1Score
├── object_pool/
│   ├── README.md
│   └── src/
│       ├── object_pool_1.py        # Basic synchronous connection pool
│       └── example/
│           ├── main.py             # Async pool demo with 5 tests
│           ├── object_pool.py      # Generic async ObjectPool (asyncio.Queue)
│           └── database_connection.py  # Pooled resource — SQLite connection
└── command/
    ├── README.md
    └── src/
        ├── command_1.py            # Basic remote control with devices
        └── example/
            ├── main.py             # Text editor undo/redo demo
            ├── command.py          # Command interface (execute + undo)
            ├── text_editor.py      # Receiver — text insert/delete
            ├── commands.py         # InsertCommand + DeleteCommand
            └── command_manager.py  # Invoker — undo/redo stacks
```

---

## Getting Started ▶️

```bash
# Clone the repo
git clone <repo-url>
cd design-patterns

# Run singleton examples
python singleton/src/singleton_1.py
python singleton/src/example/config.py

# Run factory examples
cd factory
python -m src.factory_1
python -m src.example.main

# Run observer examples
python observer/src/observer_1.py
cd observer/src/example && python main.py

# Run abstract factory examples
python abstract_factory/src/abstract_factory_1.py
cd abstract_factory && python -m src.example.main

# Run adapter pattern examples
python adapter_pattern/src/adapter_pattern_1.py
cd adapter_pattern && python -m src.example.main

# Run strategy pattern examples
python strategy_design_pattern/src/strategy_1.py
cd strategy_design_pattern && python -m src.example.main

# Run decorator pattern examples
python decorator/src/decorator_1.py
cd decorator && python -m src.example.main

# Run builder pattern examples
python builder_pattern/src/builder_1.py
cd builder_pattern && python -m src.example.main

# Run object pool examples
python object_pool/src/object_pool_1.py
cd object_pool && python -m src.example.main

# Run command pattern examples
python command/src/command_1.py
cd command && python -m src.example.main
```


## Requirements 🛠️

- Python 3.8+
- No external dependencies (uses only standard library)

---
