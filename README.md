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
└── adapter_pattern/
    ├── README.md
    └── src/
        ├── adapter_pattern_1.py    # Basic printer adapter
        └── example/
            ├── main.py             # CRM integration demo
            ├── adapter.py          # Target interface (abstract)
            ├── customer.py         # Unified data model (dataclass)
            ├── client.py           # Client — works with any adapter
            ├── net_suite_api.py    # Adaptee A — NetSuite CRM
            ├── net_suite_adapter.py        # Adapter A — NetSuite → Customer
            ├── business_central_api.py     # Adaptee B — Business Central CRM
            └── business_central_adapter.py # Adapter B — Business Central → Customer
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
```


## Requirements 🛠️

- Python 3.8+
- No external dependencies (uses only standard library)

---
