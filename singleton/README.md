# Singleton Design Pattern 🔒

## What is Singleton? 🎯

The **Singleton** pattern ensures a class has **only one instance** and provides a global point of access to it. No matter how many times you try to create an object, you always get the same instance.

```
┌─────────────────────────────────────┐
│           SingletonClass            │
├─────────────────────────────────────┤
│  - _instance: SingletonClass        │
│  - _lock: Lock                      │
├─────────────────────────────────────┤
│  + get_instance(): SingletonClass   │
│  + __new__(): SingletonClass        │
└─────────────────────────────────────┘
         │
         ▼
    Only ONE instance
    shared everywhere
```

---

## When to Use Singleton? ⚡

| Use Case | Example |
|----------|---------|
| **Configuration Management** | App settings that should be consistent across the application |
| **Database Connections** | Connection pool that's expensive to create |
| **Logging** | Single logger instance for the entire app |
| **Caching** | Shared cache that all modules can access |
| **Thread Pools** | Managing a pool of worker threads |

### When NOT to Use 🚫
- When you need multiple instances with different states
- In unit tests (hard to mock/reset)
- When it makes code tightly coupled

---

## Implementations 🛠️

This folder contains **3 different approaches** to implement Singleton in Python:

### 1. Static Method Approach (`singleton_1.py`)

Uses `@staticmethod` with explicit `get_instance()` factory method.

```python
class SingletonDp():
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if SingletonDp._instance == None:
            with SingletonDp._lock:
                if SingletonDp._instance == None:
                    SingletonDp._instance = SingletonDp()
        return SingletonDp._instance

# Usage
s1 = SingletonDp.get_instance()
s2 = SingletonDp.get_instance()
print(s1 is s2)  # True
```

**Pros:** Explicit intent, clear API
**Cons:** Hardcoded class name, not subclass-friendly

---

### 2. `__new__` Method Approach (`singleton_2.py`)

Overrides `__new__` for transparent instantiation syntax.

```python
class SingletonDp():
    _instance = None
    _lock = threading.Lock()
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            with cls._lock:
                if cls._instance == None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, x, y):
        if not self._initialized:
            self._initialized = True
            print(x, y)

# Usage - looks like normal instantiation
c1 = SingletonDp(1, 2)  # Creates and initializes
c2 = SingletonDp(3, 4)  # Returns same instance, skips init
print(c1 is c2)  # True
```

**Pros:** Natural syntax, works with arguments
**Cons:** Needs `_initialized` guard since `__init__` runs every time

---

### 3. Class Method Approach (`singleton_3.py`)

Uses `@classmethod` for subclass-friendly implementation.

```python
class SingletonDp():
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def get_instance(cls, x, y):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = object.__new__(cls)
                    cls._instance.x = x
                    cls._instance.y = y
        return cls._instance

# Usage
c1 = SingletonDp.get_instance(1, 2)
c2 = SingletonDp.get_instance(3, 4)
print(c1 is c2)  # True
print(c1.x)      # 1 (first call's values)
```

**Pros:** Uses `cls` (subclass-friendly), clean initialization
**Cons:** Explicit factory method required

---

## Real-World Example: Config Manager 🔧

See `example/config.py` for a practical singleton using `@dataclass`:

```python
@dataclass(init=False)
class Config():
    env: str = "dev"
    debug: bool = False
    db_url: str = "sqlite:///app.db"
    extras: Dict[str, Any] = field(default_factory=dict)

    _instance: ClassVar[Optional["Config"]] = None
    _lock: ClassVar[Lock] = Lock()
    _initialized: ClassVar[bool] = False

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            with cls._lock:
                if cls._instance == None:
                    cls._instance = super().__new__(cls)
        return cls._instance

# Usage
config = Config()
config.set("env", "prod")

another_config = Config()
print(another_config.get("env"))  # "prod" - same instance!
```

---

## Thread Safety 🔐

All implementations use **double-checked locking**:

```python
if cls._instance == None:           # 1st check (fast path, no lock)
    with cls._lock:                  # Acquire lock
        if cls._instance == None:   # 2nd check (thread-safe)
            cls._instance = ...      # Create instance
```

**Why double-check?**
1. First check avoids lock overhead when instance exists (most calls)
2. Lock ensures only one thread creates the instance
3. Second check handles race condition where another thread created it while waiting

---

## Quick Comparison 📊

| Approach | Syntax | Subclass-Friendly | Init Runs |
|----------|--------|-------------------|-----------|
| `@staticmethod` | `Class.get_instance()` | No | Once |
| `__new__` | `Class(args)` | Yes | Every call* |
| `@classmethod` | `Class.get_instance(args)` | Yes | Once |

*Requires `_initialized` guard

---

## Running the Examples ▶️

```bash
# Run each implementation
python singleton/src/singleton_1.py
python singleton/src/singleton_2.py
python singleton/src/singleton_3.py
python singleton/src/example/config.py
```

---

## Key Takeaways 💡

1. **Singleton = One Instance** - All variables point to the same object
2. **Thread Safety Matters** - Use locks in multi-threaded environments
3. **`__init__` Gotcha** - It runs every time, use `_initialized` guard
4. **Choose Your Approach** - `@classmethod` for flexibility, `__new__` for natural syntax
