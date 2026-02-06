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
└── singleton/
    ├── README.md
    └── src/
        ├── singleton_1.py    # @staticmethod approach
        ├── singleton_2.py    # __new__ approach
        ├── singleton_3.py    # @classmethod approach
        └── example/
            └── config.py     # Real-world config manager
```

---

## Getting Started ▶️

```bash
# Clone the repo
git clone <repo-url>
cd design-patterns

# Run any pattern example
python singleton/src/singleton_1.py
python singleton/src/example/config.py
```


## Requirements 🛠️

- Python 3.8+
- No external dependencies (uses only standard library)

---
