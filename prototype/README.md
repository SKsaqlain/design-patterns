# Prototype Design Pattern 🧬

## What is Prototype? 🎯

The **Prototype** pattern creates new objects by **cloning an existing instance** (the prototype) instead of building from scratch. This is useful when object creation is expensive or when you want copies with the same base state that can be independently customized.

```
┌──────────────┐   save/clone()    ┌──────────────────┐
│    Client     │ ───────────────▶ │   Prototype      │
│               │                  │   (Interface)     │
│               │  ◀────────────── ├──────────────────┤
│  uses clone   │   new instance   │ + save()          │
└──────────────┘                   │ + set_attributes()│
                                   │ + display()       │
                                   └────────┬──────────┘
                                            │ implemented by
                          ┌─────────────────┼─────────────────┐
                          ▼                 ▼                 ▼
                   ┌────────────┐   ┌────────────┐   ┌────────────┐
                   │   Mage     │   │  Warrior   │   │   Rogue    │
                   └────────────┘   └────────────┘   └────────────┘
```

---

## When to Use Prototype? ⚡

| Use Case | Example |
|----------|---------|
| **Expensive initialization** | Objects that load config, connect to resources, or parse data |
| **Many similar objects** | Game characters with shared base stats but different names |
| **Avoiding subclass explosion** | Clone and tweak instead of creating a new subclass per variant |
| **Snapshot / save state** | Save a player's profile at a checkpoint and restore later |
| **Runtime object creation** | Create objects whose type is determined at runtime |

### When NOT to Use 🚫
- When objects are simple and cheap to construct
- When objects have circular references that make cloning complex
- When a factory or builder already handles creation cleanly

---

## Prototype vs Factory vs Builder 📊

| Aspect | Prototype | Factory | Builder |
|--------|-----------|---------|---------|
| Creation | **Clones** an existing instance | Creates a **new** instance via method | Builds **step by step** |
| Source | Copies from a live object | Decides type internally | Assembles from parts |
| Use case | Many similar objects | Choose one type from a family | Complex multi-part objects |
| State | Clone inherits current state | Starts fresh | Configured incrementally |

---

## Basic Implementation 🛠️

### `prototype_1.py` — Shape Cloning

A minimal prototype example where shapes are cloned via a `clone()` method.

```python
# Prototype interface — declares clone and draw
class ShapePrototype(ABC):
    @abstractmethod
    def clone(self): ...
    @abstractmethod
    def draw(self): ...

# Concrete Prototype — creates a copy of itself
class CirclePrototype(ShapePrototype):
    def __init__(self, color: str):
        self.color = color

    def clone(self):
        return CirclePrototype(self.color)  # new instance with same state

    def draw(self):
        logger.info(f"Drawing a {self.color} Circle")

# Client — uses prototype without knowing the concrete class
class ShapeClient:
    def __init__(self, shape_prototype: ShapePrototype):
        self.shape_prototype = shape_prototype

    def create_shape(self):
        return self.shape_prototype.clone()

# Usage
red_circle = CirclePrototype('red')
client = ShapeClient(red_circle)
cloned = client.create_shape()
cloned.draw()
```

### Sample Output

```
2026-02-22 10:00:00 - INFO - Created CirclePrototype with color 'red'
2026-02-22 10:00:00 - INFO - Drawing a red Circle
2026-02-22 10:00:00 - INFO - Cloned CirclePrototype with color 'red'
2026-02-22 10:00:00 - INFO - Drawing a red Circle
```

---

## Real-World Example: Game Character Profiles 🔧

See `example/` for a practical prototype pattern where game character profiles (Mage, Warrior, Rogue) are cloned and customized independently.

### Structure

```
example/
├── main.py             # Entry point — 5 tests demonstrating clone behavior
├── player.py           # Prototype interface + Mage, Warrior, Rogue prototypes
└── player_client.py    # Client — clones profiles via the prototype interface
```

### How It Works

```python
# Prototype interface — base stats + save/set/display
class PlayerPrototype(ABC):
    def __init__(self):
        self.name = "XYZ@123"
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.magic = 3
        self.speed = 3
        self.level = 1

    @abstractmethod
    def save(self): ...  # clone the current state

    def set_attributes(self, params):
        for key, value in params.items():
            if hasattr(self, key):  # only set known attributes
                setattr(self, key, value)

# Concrete Prototype — Mage with magic-focused defaults
class MagePrototype(PlayerPrototype):
    def __init__(self, name, health=80, attack=5, defense=3, magic=15, speed=2):
        super().__init__()
        self.name = name
        self.health = health
        ...

    def save(self):
        return MagePrototype(  # clone all current values
            name=self.name, health=self.health, attack=self.attack,
            defense=self.defense, magic=self.magic, speed=self.speed,
        )

# Client — delegates cloning to the prototype
class PlayerClient:
    def __init__(self, player_prototype: PlayerPrototype):
        self.player_prototype = player_prototype

    def save_player_profile(self):
        return self.player_prototype.save()
```

### Character Defaults

| Type | HP | ATK | DEF | MAG | SPD | Strength |
|------|----|-----|-----|-----|-----|----------|
| **Mage** | 80 | 5 | 3 | 15 | 2 | High magic |
| **Warrior** | 150 | 15 | 12 | 2 | 3 | High health & defense |
| **Rogue** | 90 | 12 | 4 | 5 | 10 | High speed |

### Tests in `main.py`

| Test | What It Verifies |
|------|-----------------|
| **Test 1** | Create mage, customize stats via dict, clone preserves customized values |
| **Test 2** | Warrior clone retains default stats |
| **Test 3** | Clone is independent — modifying original doesn't affect clone |
| **Test 4** | `set_attributes` safely ignores unknown dict keys |
| **Test 5** | `PlayerClient` works polymorphically with all three types |

### Sample Output

```
2026-02-22 10:00:00 - INFO - === Test 1: Mage — create, customize, save ===
2026-02-22 10:00:00 - INFO - Created MagePrototype 'Gandalf'
2026-02-22 10:00:00 - INFO - Mage Player Profile | [Gandalf] HP:80 ATK:5 DEF:3 MAG:15 SPD:2 LVL:1
2026-02-22 10:00:00 - INFO - Mage Player Profile | [Gandalf] HP:60 ATK:60 DEF:80 MAG:90 SPD:20 LVL:1
2026-02-22 10:00:00 - INFO - Cloning MagePrototype 'Gandalf'
2026-02-22 10:00:00 - INFO - Saved player profile for 'Gandalf'
2026-02-22 10:00:00 - INFO - === Test 3: Rogue — clone independence ===
2026-02-22 10:00:00 - INFO - Test 3 passed: Clone is independent of original
2026-02-22 10:00:00 - INFO - Test 4 passed: Unknown keys safely ignored
2026-02-22 10:00:00 - INFO - Test 5 passed: Client cloned all three types
```

---

## Design Principles at Play 📐

| Principle | How Prototype Applies |
|-----------|----------------------|
| **Single Responsibility** | Each prototype handles its own cloning; the client just triggers it |
| **Open/Closed** | Add new character types (e.g., `ArcherPrototype`) without modifying client or existing prototypes |
| **Dependency Inversion** | `PlayerClient` depends on `PlayerPrototype` abstraction, not concrete types |
| **Liskov Substitution** | Any prototype subclass can replace `PlayerPrototype` without breaking the client |

---

## Running the Examples ▶️

```bash
# Run the basic shape cloning example
python prototype/src/prototype_1.py

# Run the game character profile example
cd prototype
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Prototype = Clone Over Construct** — Copy a live object instead of building from scratch
2. **Clone Is Independent** — Modifying the original after cloning doesn't affect the copy
3. **set_attributes for Customization** — Tweak a clone's stats without subclassing
4. **Client Stays Generic** — The client works with any prototype type through the abstract interface
5. **Save/Restore Pattern** — Naturally supports snapshotting and restoring object state
