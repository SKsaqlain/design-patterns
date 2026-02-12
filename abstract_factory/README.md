# Abstract Factory Design Pattern 🏗️

## What is Abstract Factory? 🎯

The **Abstract Factory** pattern provides an interface for creating **families of related objects** without specifying their concrete classes. Unlike the regular Factory pattern (which creates one product), Abstract Factory creates a **matched set** of products that are designed to work together.

```
┌──────────────────────────┐
│   CloudServiceFactory    │        creates a family of:
│     (Abstract Factory)   │
├──────────────────────────┤       ┌──────────────┐
│ + get_virtual_machine()  │──────▶│ VirtualMachine│
│ + get_database()         │──────▶│ Database      │
│ + get_storage()          │──────▶│ Storage       │
└──────────┬───────────────┘       └──────────────┘
           │
     ┌─────┴──────┬──────────┐
     ▼            ▼          ▼
┌─────────┐ ┌─────────┐ ┌─────────┐
│   AWS   │ │   GCP   │ │  Azure  │
│ Factory │ │ Factory │ │ Factory │
└─────────┘ └─────────┘ └─────────┘
  creates:    creates:    creates:
  AWS_VM      GCP_VM      AZURE_VM
  AWS_DB      GCP_DB      AZURE_DB
  AWS_S3      GCP_Store   AZURE_Blob
```

---

## When to Use Abstract Factory? ⚡

| Use Case | Example |
|----------|---------|
| **Product families** | Cloud services (VM + DB + Storage) that must be from the same provider |
| **Platform independence** | UI widgets (Button + Checkbox + Menu) for Windows vs macOS |
| **Configuration-driven** | Swap entire service sets based on environment (dev/staging/prod) |
| **Cross-cutting consistency** | Regional products (car + specification) that must match |
| **Avoiding mix-and-match bugs** | Prevent creating an AWS VM with an Azure Database |

### When NOT to Use 🚫
- When you only have one product type (use regular Factory Method instead)
- When products don't need to be grouped as families
- When a simple constructor or builder would do

---

## Factory Method vs Abstract Factory 📊

| Aspect | Factory Method | Abstract Factory |
|--------|----------------|------------------|
| **Creates** | One product | A family of related products |
| **Methods** | One factory method | Multiple factory methods |
| **Goal** | Delegate creation of a single object | Ensure related objects are compatible |
| **Example** | `create_account()` → SavingAccount | `get_vm()` + `get_db()` + `get_storage()` → all AWS |
| **Subclasses** | Each factory creates one product type | Each factory creates an entire product set |
| **Mix-and-match** | N/A (single product) | Prevented by design |

**Key insight:** Factory Method is about *one product, many variants*. Abstract Factory is about *many products, grouped by family*.

---

## Basic Implementation 🛠️

### `abstract_factory_1.py` — Regional Car Factory

A minimal abstract factory with two product types (Car + Specification) grouped by region.

```python
# Abstract Products
class Car(ABC):
    def build_car(self) -> str: ...

class CarSpecification(ABC):
    def get_specification(self) -> str: ...

# Abstract Factory — creates a matched pair of products
class CarFactory(ABC):
    def create_car(self) -> Car: ...
    def create_specification(self) -> CarSpecification: ...

# Concrete Factory: North America — always Sedan + NA specs
class NorthAmericanCarFactory(CarFactory):
    def create_car(self) -> Car:
        return Sedan()
    def create_specification(self) -> CarSpecification:
        return NorthAmericanSpecification()

# Concrete Factory: Europe — always Hatchback + EU specs
class EuropeCarFactory(CarFactory):
    def create_car(self) -> Car:
        return Hatchback()
    def create_specification(self) -> CarSpecification:
        return EuropeSpecification()

# Usage — swap factory, get a matched pair
na_factory = NorthAmericanCarFactory()
print(na_factory.create_car().build_car())             # Building Sedan Car.
print(na_factory.create_specification().get_specification())  # NA safety specs

eu_factory = EuropeCarFactory()
print(eu_factory.create_car().build_car())             # Building Hatchback Car.
print(eu_factory.create_specification().get_specification())  # EU emissions specs
```

**Key Takeaway:** Each factory guarantees a **matched pair** — you can't accidentally get a Sedan with EU specs.

---

## Real-World Example: Cloud Service Provider 🌐

See `example/` for a practical abstract factory with 3 product types across 3 cloud providers.

### Structure

```
example/
├── main.py              # Client — iterates over factories, demo output
├── cloud_service.py     # Abstract Factory + AWS/GCP/Azure concrete factories
├── virtual_machine.py   # Abstract Product + AWS_VM / GCP_VM / AZURE_VM
├── database.py          # Abstract Product + AWS_Database / GCP_Database / AZURE_Database
└── storage.py           # Abstract Product + AWS_Storage / GCP_Storage / AZURE_Storage
```

### How It Works

```python
# Abstract Factory — declares creation methods for each product in the family
class CloudServiceFactory(ABC):
    def get_virtual_machine(self): ...
    def get_database(self): ...
    def get_storage(self): ...

# Concrete Factory — produces AWS services as a matched set
class AWSFactory(CloudServiceFactory):
    def get_virtual_machine(self):
        return AWS_VM()
    def get_database(self):
        return AWS_Database()
    def get_storage(self):
        return AWS_Storage()

# Client code — works with any factory, gets a consistent service set
factories = [AWSFactory(), GCPFactory(), AZUREFactory()]
for factory in factories:
    vm = factory.get_virtual_machine()
    vm.start_machine()
    db = factory.get_database()
    db.connect_to_db()
    storage = factory.get_storage()
    storage.connect_to_storage()
```

### Sample Output

```
20:26:35 | INFO | __main__              | === Abstract Factory — Cloud Service Example ===
20:26:35 | INFO | __main__              | --- AWS ---
20:26:35 | INFO | cloud_service         | [AWS] creating Virtual Machine
20:26:35 | INFO | virtual_machine       | Starting AWS Virtual Machine instance
20:26:35 | INFO | cloud_service         | [AWS] creating Database
20:26:35 | INFO | database              | Connecting to AWS Database
20:26:35 | INFO | cloud_service         | [AWS] creating Storage
20:26:35 | INFO | storage               | Connecting to AWS Storage
20:26:35 | INFO | __main__              | --- GCP ---
20:26:35 | INFO | cloud_service         | [GCP] creating Virtual Machine
20:26:35 | INFO | virtual_machine       | Starting GCP Virtual Machine instance
20:26:35 | INFO | cloud_service         | [GCP] creating Database
20:26:35 | INFO | database              | Connecting to GCP Database
20:26:35 | INFO | cloud_service         | [GCP] creating Storage
20:26:35 | INFO | storage               | Connecting to GCP Storage
20:26:35 | INFO | __main__              | --- Azure ---
20:26:35 | INFO | cloud_service         | [Azure] creating Virtual Machine
20:26:35 | INFO | virtual_machine       | Starting AZURE Virtual Machine instance
20:26:35 | INFO | cloud_service         | [Azure] creating Database
20:26:35 | INFO | database              | Connecting to AZURE Database
20:26:35 | INFO | cloud_service         | [Azure] creating Storage
20:26:35 | INFO | storage               | Connecting to AZURE Storage
```

---

## Design Principles at Play 📐

| Principle | How Abstract Factory Applies |
|-----------|------------------------------|
| **Open/Closed** | Add a new provider (e.g., DigitalOcean) without modifying existing factories or client code |
| **Dependency Inversion** | Client depends on `CloudServiceFactory` abstraction, not on `AWSFactory` or `GCP_VM` |
| **Single Responsibility** | Each factory handles creation for one provider only |
| **Consistency by Design** | Impossible to mix AWS VM with Azure Database — the factory guarantees a matched set |

---

## Running the Examples ▶️

```bash
# Run the basic car factory example
python abstract_factory/src/abstract_factory_1.py

# Run the cloud service example
cd abstract_factory
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Abstract Factory = Families of Products** — Creates matched sets, not individual objects
2. **Consistency Guaranteed** — Each factory produces products designed to work together
3. **Factory Method vs Abstract Factory** — One product vs many related products
4. **Easy to Extend** — New provider = new factory + new products, zero changes to client
