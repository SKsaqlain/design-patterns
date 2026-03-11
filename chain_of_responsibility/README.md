# Chain of Responsibility Design Pattern

## What is the Chain of Responsibility Pattern?

The Chain of Responsibility pattern lets you **pass a request along a chain of handlers**. Each handler decides either to process the request or to pass it to the next handler in the chain. This decouples the sender of a request from its receivers.

---

## When to Use It?

| Scenario | Why Chain of Responsibility Helps |
|----------|-----------------------------------|
| Multiple objects can handle a request and the handler isn't known in advance | The chain finds the right handler automatically |
| You want to decouple the sender from the receiver | The sender only knows the first handler in the chain |
| The set of handlers or their order should be configurable at runtime | Handlers can be linked dynamically |
| A request should be handled by more than one handler (filter/pipeline style) | Each handler can process and forward |

---

## Chain of Responsibility vs Similar Patterns

| Feature | Chain of Responsibility | Command | Observer |
|---------|------------------------|---------|----------|
| **Intent** | Pass request along a chain until handled | Encapsulate a request as an object | Notify all subscribers of an event |
| **Flow** | Sequential — one handler at a time | Direct — invoker to command | Broadcast — one to many |
| **Coupling** | Sender knows only the first handler | Invoker knows the command interface | Subject knows the observer interface |
| **Handling** | At most one handler processes | Exactly one command executes | All observers are notified |

---

## Implementation — Support Ticket Escalation

```
  Request ──▶ Level1Handler ──▶ Level2Handler ──▶ Level3Handler
               (BASIC)          (INTERMEDIATE)     (CRITICAL)
```

A support ticket system where requests are escalated through three levels. Each handler checks if it can resolve the ticket based on priority; if not, it forwards the request to the next handler.

### Participants

- **Priority** — Enum defining ticket severity levels (BASIC, INTERMEDIATE, CRITICAL)
- **Request** — Carries the priority of the support ticket
- **SupportHandler** — Abstract handler declaring `handle_request()` and `set_next_handler()`
- **Level1/2/3SupportHandler** — Concrete handlers, each responsible for one priority level

**Run:**
```bash
python chain_of_responsibility/src/main.py
```

**Output:**
```
Level 1 Support handled the request
Level 2 Support handled the request
Level 3 Support handled the request
 Cannot handle request
```

---

## Project Structure

```
chain_of_responsibility/
├── README.md
└── src/
    └── main.py    # Support ticket escalation chain demo
```

---

## Design Principles

| Principle | How It's Applied |
|-----------|-----------------|
| **Single Responsibility** | Each handler only processes its own priority level |
| **Open/Closed** | New handlers can be added to the chain without modifying existing ones |
| **Loose Coupling** | The client only knows the first handler, not the entire chain |

---

## Key Takeaways

- Each handler in the chain either **handles the request or forwards it** to the next handler
- The client sends the request to the **first handler** without knowing which handler will process it
- Handlers can be **reordered, added, or removed** at runtime without changing client code
- If no handler can process the request, it falls through to a **default response** at the end of the chain
