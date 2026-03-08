# Bridge Design Pattern

## What is the Bridge Pattern?

The Bridge pattern **decouples an abstraction from its implementation** so that the two can vary independently. Instead of creating a tightly coupled class hierarchy, the pattern splits it into two separate hierarchies — one for the abstraction and one for the implementation — connected by a "bridge" (composition).

---

## When to Use It?

| Scenario | Why Bridge Helps |
|----------|-----------------|
| You want to avoid a class explosion from combining multiple dimensions (e.g., message type x delivery channel) | Each dimension grows independently |
| You need to swap implementations at runtime | The abstraction delegates to a pluggable implementor |
| Both the abstraction and implementation need to be extended independently | Changes in one hierarchy don't affect the other |
| You want to hide implementation details from the client | Client works only with the abstraction interface |

---

## Bridge vs Similar Patterns

| Feature | Bridge | Adapter | Strategy |
|---------|--------|---------|----------|
| **Intent** | Decouple abstraction from implementation | Make incompatible interfaces work together | Swap algorithms at runtime |
| **When designed** | Up-front (planned separation) | After the fact (retrofit) | When behavior varies |
| **Relationship** | Abstraction owns implementor | Adapter wraps adaptee | Context owns strategy |
| **Hierarchies** | Two parallel hierarchies | Single wrapper | Single strategy interface |

---

## Basic Implementation — Vehicle Manufacturing

```
  Abstraction           Implementor
  ┌──────────┐          ┌──────────┐
  │ Vehicle  │────────▶ │ Workshop │
  └────┬─────┘          └────┬─────┘
       │                     │
  ┌────┴─────┐          ┌────┴─────┐
  │   Car    │          │ Produce  │
  │   Bike   │          │ Assemble │
  └──────────┘          └──────────┘
```

A `Vehicle` (abstraction) holds references to `Workshop` objects (implementors). Each vehicle delegates its `manufacture()` call to the workshops, allowing any vehicle type to be combined with any workshop sequence.

**Run:**
```bash
python bridge/src/main.py
```

**Output:**
```
Car Produced And Assembled.
Bike Produced And Assembled.
```

---

## Real-World Example — Message Delivery System

A messaging system where **message types** (urgent, regular) and **delivery channels** (email, SMS) vary independently.

```
  Abstraction               Implementor
  ┌───────────────┐         ┌───────────────┐
  │   Message     │────────▶│ MessageSender │
  │  (abstract)   │         │  (abstract)   │
  └───────┬───────┘         └───────┬───────┘
          │                         │
  ┌───────┴───────┐         ┌──────┴────────┐
  │ UrgentMessage │         │  EmailSender  │
  │               │         │  SMSSender    │
  └───────────────┘         └───────────────┘
```

- **MessageSender** — Implementor interface defining `send_message(to, body)`
- **EmailSender / SMSSender** — Concrete implementors for each delivery channel
- **Message** — Abstraction that holds a reference to a `MessageSender`
- **UrgentMessage** — Refined abstraction that prepends `[URGENT]` before delegating

**Run:**
```bash
cd bridge && python -m src.example.main
```

**Output:**
```
Sending email to alice@example.com: [URGENT] Server is down!
Sending SMS to +1234567890: [URGENT] Server is down!
```

---

## Project Structure

```
bridge/
├── README.md
└── src/
    ├── main.py                # Basic vehicle manufacturing example
    └── example/
        ├── main.py            # Message delivery demo
        ├── message_sender.py  # Implementor interface (abstract)
        ├── email_sender.py    # Concrete Implementor — email delivery
        ├── sms_sender.py      # Concrete Implementor — SMS delivery
        └── message.py         # Abstraction + UrgentMessage refined abstraction
```

---

## Design Principles

| Principle | How It's Applied |
|-----------|-----------------|
| **Single Responsibility** | Message types handle formatting; senders handle delivery |
| **Open/Closed** | Add new message types or senders without modifying existing code |
| **Dependency Inversion** | `Message` depends on the `MessageSender` abstraction, not concrete senders |
| **Composition over Inheritance** | The bridge uses composition (`self.message_sender`) instead of deep inheritance |

---

## Key Takeaways

- The Bridge pattern prevents **class explosion** when you have multiple independent dimensions of variation
- The abstraction and implementor are connected through **composition**, not inheritance
- New abstractions and implementors can be added **independently** without affecting each other
- The implementor can be **swapped at runtime**, making the system flexible and testable
