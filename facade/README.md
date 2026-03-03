# Facade Design Pattern 🏛️

## What is Facade? 🎯

The **Facade** pattern provides a **simplified interface** to a complex subsystem. Instead of forcing clients to interact with multiple classes and their details, the facade exposes a single, easy-to-use entry point that delegates to the underlying components.

```
┌──────────────┐                  ┌──────────────────┐
│    Client     │  simple call    │     Facade       │
│               │ ──────────────▶ │  (HotelKeeper)   │
│               │                 ├──────────────────┤
│               │                 │ + getVegMenu()   │
│               │                 │ + getNonVegMenu()│
│               │                 │ + getGeneralMenu()│
└──────────────┘                 └────────┬─────────┘
                                          │ delegates to
                        ┌─────────────────┼─────────────────┐
                        ▼                 ▼                 ▼
                 ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
                 │ VegRestaurant│ │NonVegRestaurant│ │GeneralRestaurant│
                 └──────┬───────┘ └──────┬───────┘ └──────┬───────┘
                        ▼                ▼                 ▼
                    VegMenu         NonVegMenu           Both
```

---

## When to Use Facade? ⚡

| Use Case | Example |
|----------|---------|
| **Simplify complex subsystems** | Hotel keeper hides restaurant and menu creation details |
| **Reduce client dependencies** | Client only knows the facade, not the subsystem classes |
| **Provide a default workflow** | Common operations wrapped in a single method call |
| **Layer your architecture** | Facade as an entry point to a service layer or SDK |
| **Legacy system wrapper** | Clean API over messy or poorly designed internals |

### When NOT to Use 🚫
- When the subsystem is already simple (facade adds unnecessary indirection)
- When clients genuinely need fine-grained control over subsystem components
- When the facade becomes a "god class" doing too much

---

## Facade vs Adapter vs Proxy 📊

| Aspect | Facade | Adapter | Proxy |
|--------|--------|---------|-------|
| Intent | **Simplify** a complex subsystem | **Convert** one interface to another | **Control access** to an object |
| Direction | Wraps **multiple** classes | Wraps **one** incompatible class | Wraps **one** compatible class |
| Client knows | Only the facade | Only the target interface | Same interface as the real object |
| Complexity | Reduces complexity for the client | Bridges incompatible interfaces | Adds behavior (lazy load, logging, etc.) |

---

## Implementation 🛠️

### `facade_1.py` — Hotel Menu System

A hotel keeper (facade) that hides the complexity of multiple restaurant types and their menus behind simple method calls.

```python
# Subsystem interface — different restaurant types
class Hotel(ABC):
    @abstractmethod
    def get_menus(self): ...

class VegRestaurant(Hotel):
    def get_menus(self):
        return VegMenu()

class NonVegRestaurant(Hotel):
    def get_menus(self):
        return NonVegMenu()

class GeneralRestaurant(Hotel):
    def get_menus(self):
        return Both()

# Menu objects — created by the subsystem
class VegMenu:
    def __init__(self): print("Vegan Menu")

class NonVegMenu:
    def __init__(self): print("Non Vegan Menu")

class Both:
    def __init__(self): print("General Menu")

# Facade — single entry point for the client
class HotelKeeperImpl(HotelKeeper):
    def getVegMenu(self):
        return VegRestaurant().get_menus()      # hides restaurant creation

    def getNonVegMenu(self):
        return NonVegRestaurant().get_menus()    # hides restaurant creation

    def getGeneralMenu(self):
        return GeneralRestaurant().get_menus()   # hides restaurant creation

# Client — only interacts with the facade
keeper = HotelKeeperImpl()
keeper.getVegMenu()
keeper.getNonVegMenu()
keeper.getGeneralMenu()
```

### Sample Output

```
Vegan Menu
Non Vegan Menu
General Menu
```

**Key point:** The client never creates `VegRestaurant`, `NonVegRestaurant`, or any menu class directly — the facade handles all of that.

---

## Structure

```
facade/
├── README.md
└── src/
    └── facade_1.py    # Hotel keeper facade with restaurant subsystem
```

---

## Design Principles at Play 📐

| Principle | How Facade Applies |
|-----------|-------------------|
| **Single Responsibility** | Each restaurant handles its own menu; the facade only orchestrates |
| **Open/Closed** | Add new restaurant types without changing the client |
| **Dependency Inversion** | Client depends on the `HotelKeeper` abstraction, not concrete restaurants |
| **Least Knowledge (Law of Demeter)** | Client talks only to the facade, not to subsystem internals |

---

## Running the Example ▶️

```bash
python facade/src/facade_1.py
```

---

## Key Takeaways 💡

1. **Facade = Simplified API** — One entry point hides a complex subsystem
2. **Client Stays Simple** — No need to know about restaurants, menus, or their relationships
3. **Subsystem Unchanged** — The facade wraps existing classes without modifying them
4. **Not a Restriction** — Clients can still access the subsystem directly if they need to
5. **Common in Practice** — SDKs, ORMs, and framework APIs are all facades over complex internals
