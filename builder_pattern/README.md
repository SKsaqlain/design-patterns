# Builder Design Pattern 🏗️

## What is Builder? 🎯

The **Builder** pattern separates the construction of a complex object from its representation. It lets you build an object **step by step**, where each step configures one part. A **Director** orchestrates the steps, and the **Builder** knows *what* to set at each step — so the client never touches the messy construction details.

```
┌─────────────────────────┐
│   MLModelTestDirector   │       orchestrates:
│       (Director)        │
├─────────────────────────┤       ┌────────────────────┐
│ + build_pipeline()      │──────▶│  MLPipelineBuilder │
└─────────────────────────┘       │    (Interface)     │
                                  ├────────────────────┤
                                  │ + add_data_source()│
                                  │ + add_preprocessing│
                                  │ + add_model()      │
                                  │ + add_evaluation() │
                                  │ + get_result()     │
                                  └────────┬───────────┘
                                           │
                                           ▼
                                  ┌────────────────────┐
                                  │    MLModelTest     │  builds:
                                  │ (Concrete Builder) │──────────▶ MLPipeline
                                  └────────────────────┘            (Product)
```

---

## When to Use Builder? ⚡

| Use Case | Example |
|----------|---------|
| **Complex object with many parts** | ML pipeline with data source, preprocessing, model, evaluation |
| **Step-by-step construction** | Each component must be configured independently |
| **Multiple representations** | Same build steps produce different products (gaming PC vs office PC) |
| **Isolate construction logic** | Client doesn't need to know how parts are assembled |
| **Readable construction** | Replace telescoping constructors with clear step methods |

### When NOT to Use 🚫
- When the object is simple (just use a constructor)
- When there's only one way to build the object
- When a factory method is sufficient (single-step creation)

---

## Builder vs Factory 📊

| Aspect | Factory | Builder |
|--------|---------|---------|
| Construction | One step — returns a finished product | Multi-step — builds piece by piece |
| Complexity | Simple objects with few parameters | Complex objects with many parts |
| Control | Factory decides the configuration | Client/Director controls the build order |
| Return point | Factory method returns the product | `get_result()` returns after all steps |
| Variants | Different subclasses = different products | Different builders = different configurations |

---

## Basic Implementation 🛠️

### `builder_1.py` — Computer Builder

A minimal builder example where a gaming computer is assembled step by step.

```python
# Product — the complex object being built
class Computer():
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu): self.cpu = cpu
    def set_ram(self, ram): self.ram = ram
    def set_storage(self, storage): self.storage = storage

# Builder Interface — declares the build steps
class ComputerBuilder(ABC):
    def build_cpu(self): ...
    def build_ram(self): ...
    def build_storage(self): ...
    def get_result(self) -> Computer: ...

# Concrete Builder — knows what values to set
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):    self.computer.set_cpu('Gaming CPU')
    def build_ram(self):    self.computer.set_ram('16GB DDR4')
    def build_storage(self): self.computer.set_storage('1TB SSD')
    def get_result(self):   return self.computer

# Director — orchestrates the build order
class ComputerDirector:
    def construct(self, builder: ComputerBuilder):
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()

# Usage — director builds, client retrieves the product
gaming_builder = GamingComputerBuilder()
director = ComputerDirector()
director.construct(gaming_builder)
gaming_computer = gaming_builder.get_result()
gaming_computer.display_info()
```

**Key Takeaway:** The client never calls `set_cpu()`, `set_ram()`, etc. directly — the director orchestrates the steps, and the builder fills in the specifics.

### Sample Output

```
Computer config:
CPU: Gaming CPU
RAM: 16GB DDR4
Storage: 1TB SSD
```

---

## Real-World Example: ML Pipeline 🔧

See `example/` for a practical builder pattern where an ML pipeline is assembled from interchangeable components — data source, preprocessing, model, and evaluation.

### Structure

```
example/
├── main.py             # Entry point — builds and displays the pipeline
├── ml_pipeline.py      # Product + Builder Interface + Concrete Builder + Director
├── datasource.py       # Pipeline component — DataSource abstract + S3
├── preprocessing.py    # Pipeline component — Preprocessing abstract + Normalize
├── model.py            # Pipeline component — Model abstract + LogisticRegression
└── evaluation.py       # Pipeline component — Evaluation abstract + F1Score
```

### How It Works

```python
# Product — the ML pipeline with four configurable parts
class MLPipeline():
    def __init__(self):
        self.data_source: DataSource = None
        self.preprocessing: Preprocessing = None
        self.model: Model = None
        self.evaluation: Evaluation = None

    def set_data_source(self, data_source): ...
    def set_preprocessing(self, preprocessing): ...
    def set_model(self, model): ...
    def set_evaluation(self, evaluation): ...
    def get_pipeline_config(self): ...

# Builder Interface — declares the steps to build an MLPipeline
class MLPipelineBuilder(ABC):
    def add_data_source(self): ...
    def add_preprocessing_step(self): ...
    def add_model(self): ...
    def add_evaluation_step(self): ...
    def get_result(self) -> MLPipeline: ...

# Concrete Builder — assembles an S3 + Normalize + LogisticRegression + F1Score pipeline
class MLModelTest(MLPipelineBuilder):
    def __init__(self):
        self.ml_pipeline = MLPipeline()

    def add_data_source(self):
        self.ml_pipeline.set_data_source(S3())

    def add_model(self):
        self.ml_pipeline.set_model(LogisticRegression())

    def get_result(self) -> MLPipeline:
        return self.ml_pipeline

# Director — orchestrates the build steps in order
class MLModelTestDirector():
    def build_pipeline(self, ml_pipeline_builder: MLPipelineBuilder):
        ml_pipeline_builder.add_data_source()
        ml_pipeline_builder.add_preprocessing_step()
        ml_pipeline_builder.add_model()
        ml_pipeline_builder.add_evaluation_step()

# Usage — director builds, client retrieves the finished pipeline
ml_builder = MLModelTest()
director = MLModelTestDirector()
director.build_pipeline(ml_builder)
ml_pipeline = ml_builder.get_result()
ml_pipeline.get_pipeline_config()
```

### Pipeline Components

| Component | Abstract Base | Concrete Implementation |
|-----------|--------------|------------------------|
| **Data Source** | `DataSource` | `S3` — reads from AWS S3 |
| **Preprocessing** | `Preprocessing` | `Normalize` — scales features to standard range |
| **Model** | `Model` | `LogisticRegression` — binary classifier |
| **Evaluation** | `Evaluation` | `F1Score` — precision–recall balance metric |

### Sample Output

```
21:26:28 | INFO | __main__              | === Builder Pattern — ML Pipeline Example ===
21:26:28 | INFO | src.example.ml_pipeline | Director: building ML pipeline
21:26:28 | INFO | src.example.ml_pipeline | Adding data source: S3
21:26:28 | INFO | src.example.ml_pipeline | Adding preprocessing: Normalize
21:26:28 | INFO | src.example.ml_pipeline | Adding model: LogisticRegression
21:26:28 | INFO | src.example.ml_pipeline | Adding evaluation: F1Score
21:26:28 | INFO | src.example.ml_pipeline | ML pipeline configuration: S3, Normalize, Logistic_Regression, F1_Score
```

---

## Design Principles at Play 📐

| Principle | How Builder Applies |
|-----------|---------------------|
| **Single Responsibility** | Each pipeline component (DataSource, Model, etc.) handles one concern; the builder handles assembly |
| **Open/Closed** | Add a new builder (e.g., `MLProductionPipeline`) without modifying existing builders or the director |
| **Dependency Inversion** | Director depends on `MLPipelineBuilder` abstraction, not on `MLModelTest` directly |
| **Liskov Substitution** | Any concrete builder can replace `MLPipelineBuilder` without breaking the director |
| **Interface Segregation** | Each component has its own focused interface (`DataSource`, `Model`, `Evaluation`) |

---

## Running the Examples ▶️

```bash
# Run the basic computer builder example
python builder_pattern/src/builder_1.py

# Run the ML pipeline example
cd builder_pattern
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Builder = Step-by-Step Construction** — Build complex objects one piece at a time instead of a giant constructor
2. **Director Controls Order** — The client doesn't need to know the correct sequence of build steps
3. **Same Process, Different Results** — Swap the concrete builder to get a different product configuration
4. **Product Stays Clean** — The product only has setters; all assembly logic lives in the builder
5. **Easy to Extend** — New builder = new class, zero changes to the director or existing builders
