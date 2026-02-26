# Lazy Loading Design Pattern 💤

## What is Lazy Loading? 🎯

**Lazy Loading** defers the creation or initialization of an object until it is **actually needed**. Instead of paying the cost upfront, the object is created on first access — saving memory and startup time when the object may never be used at all.

```
┌──────────────┐   get_data()   ┌─────────────────────┐
│    Client     │ ────────────▶ │      Proxy          │
│               │               │  (Lazy Wrapper)     │
│               │               ├─────────────────────┤
│               │               │  data = None        │
│               │               │                     │
│               │               │  if data is None:   │
│               │               │    data = RealImpl()│ ──▶ expensive creation
│               │               │  return data        │
└──────────────┘                └─────────────────────┘
```

---

## When to Use Lazy Loading? ⚡

| Use Case | Example |
|----------|---------|
| **Expensive initialization** | Database connections, file parsing, network calls |
| **Rarely accessed data** | Employee list only viewed on demand |
| **Improve startup time** | Defer heavy setup until the feature is actually used |
| **Memory optimization** | Don't allocate large objects unless needed |
| **Conditional usage** | Object may never be needed depending on user flow |

### When NOT to Use 🚫
- When the object is always needed immediately
- When lazy init adds complexity without saving meaningful resources
- When thread safety concerns make deferred creation risky without synchronization

---

## Lazy Loading vs Eager Loading 📊

| Aspect | Lazy Loading | Eager Loading |
|--------|-------------|---------------|
| When created | On **first access** | At **startup / construction** |
| Startup cost | Low — deferred | High — paid upfront |
| First-access cost | Higher — includes init | None — already ready |
| Memory | Allocated only if needed | Allocated regardless |
| Complexity | Needs null-check / proxy | Simpler — just construct |

---

## Implementation 1: Lazy Registry 🛠️

### `lazy_loading_1.py` — Car Type Registry

A static registry that creates `Car` instances on demand. Each car type is instantiated only when first requested and cached for reuse.

```python
class CarType(Enum):
    none = 1
    Audi = 2
    BMW = 3

class Car:
    types: Dict[CarType, 'Car'] = {}  # shared registry

    @staticmethod
    def get_car_by_type_name(type: CarType):
        if type not in Car.types:      # lazy — create only on first request
            car = Car(type)
            Car.types[type] = car
        else:
            car = Car.types[type]      # reuse cached instance
        return car

# Usage
Car.get_car_by_type_name(CarType.BMW)   # creates BMW
Car.show_all()                           # 1 instance
Car.get_car_by_type_name(CarType.Audi)  # creates Audi
Car.show_all()                           # 2 instances
```

### Sample Output

```
Number of instances made = 1
BMW
Number of instances made = 2
BMW
Audi
```

---

## Implementation 2: Virtual Proxy 🔧

### `lazy_loading_2.py` — Company Contact List

A proxy that wraps the real `ContactListImpl` and defers its creation until `get_employee_list()` is first called. The `Company` object holds the proxy, so the expensive employee list is never loaded unless explicitly requested.

```python
# Abstract interface
class ContactList(ABC):
    @abstractmethod
    def get_employee_list(self) -> List[Employee]: ...

# Real implementation — builds the full list immediately
class ContactListImpl(ContactList):
    def get_employee_list(self):
        return self._get_emp_list()  # simulates expensive fetch

# Proxy — delays creation of real impl until first access
class ContactListProxyImpl(ContactList):
    def __init__(self):
        self.contact_list = None  # not yet created

    def get_employee_list(self) -> List[Employee]:
        if self.contact_list is None:         # lazy check
            self.contact_list = ContactListImpl()  # create on first call
        return self.contact_list.get_employee_list()

# Client — uses proxy without knowing it's lazy
class Company:
    def __init__(self, ..., contact_list: ContactList):
        self.contact_list = contact_list  # injected as proxy

# Usage — employees not loaded until explicitly requested
contact_list = ContactListProxyImpl()
company = Company('Acme', '123 St', 'xxx', contact_list)
print(company.get_company_name())         # no employee load yet
emp_list = company.get_contact_list().get_employee_list()  # triggers lazy load
```

### Sample Output

```
Company Name: Company_name
Company Address: company_location
Company Contact No: xxx-xxx-xxxx
Requesting for contact list
Fetching list of employees
Employee Name: Lokesh, Employee Designation: SE, Employee Salary: 2565.55
Employee Name: Kushagra, Employee Designation: Manager, Employee Salary: 22574
Employee Name: Susmit, Employee Designation: G4, Employee Salary: 3256.77
Employee Name: Vikram, Employee Designation: SSE, Employee Salary: 4875.54
Employee Name: Achint, Employee Designation: SE, Employee Salary: 2847.01
```

---

## Structure

```
lazy_loading/
├── README.md
└── src/
    ├── lazy_loading_1.py    # Lazy registry — Car type created on first request
    └── lazy_loading_2.py    # Virtual proxy — ContactList loaded on first access
```

---

## Design Principles at Play 📐

| Principle | How Lazy Loading Applies |
|-----------|-------------------------|
| **Single Responsibility** | Proxy handles lazy init; real implementation handles business logic |
| **Open/Closed** | Swap proxy for eager loading without changing the client |
| **Dependency Inversion** | Client depends on `ContactList` abstraction, unaware of proxy vs real |
| **Interface Segregation** | Proxy and real impl share the same focused interface |

---

## Running the Examples ▶️

```bash
# Run the lazy registry example
python lazy_loading/src/lazy_loading_1.py

# Run the virtual proxy example
python lazy_loading/src/lazy_loading_2.py
```

---

## Key Takeaways 💡

1. **Defer Until Needed** — Don't create expensive objects until they're actually accessed
2. **Proxy Pattern** — A proxy wraps the real object and controls when it gets created
3. **Cache After First Load** — Once created, the real object is reused on subsequent calls
4. **Transparent to Client** — The client uses the same interface whether it's a proxy or the real thing
5. **Trade-off** — Saves startup cost but adds a small overhead on first access
