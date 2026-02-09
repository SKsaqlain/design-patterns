# Design Patterns

A collection of design pattern implementations with detailed comments and real-world examples.

---

## What are Design Patterns? 🎯

Design patterns are **reusable solutions** to common problems in software design. They're not finished code, but templates for solving problems that can be adapted to your specific situation.



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
└── factory/
    ├── README.md
    └── src/
        ├── factory_1.py      # Basic vehicle factory
        └── example/
            ├── main.py       # Bank client + demo runs
            └── account/
                ├── bank_account.py        # Abstract Product + Factory
                ├── saving_account.py      # 4.5% interest
                ├── checking_account.py    # 1.5% interest
                └── business_account.py    # 3.0% interest
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
```


## Requirements 🛠️

- Python 3.8+
- No external dependencies (uses only standard library)

---
