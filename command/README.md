# Command Design Pattern 🎮

## What is Command? 🎯

The **Command** pattern encapsulates a request as an object, letting you parameterize clients with different requests, queue them, log them, and support **undo/redo** operations. It decouples the **invoker** (who triggers the action) from the **receiver** (who performs it).

```
┌──────────────┐   set_command()   ┌──────────────┐   execute()   ┌──────────────┐
│   Client     │ ────────────────▶ │   Invoker    │ ────────────▶ │   Command    │
│              │                   │ (Remote /    │               │  (Interface) │
│              │                   │  Manager)    │               └──────┬───────┘
└──────────────┘                   └──────────────┘                      │
                                                                         ▼
                                                                ┌──────────────┐
                                                                │   Receiver   │
                                                                │ (TV / Editor)│
                                                                └──────────────┘
```

---

## When to Use Command? ⚡

| Use Case | Example |
|----------|---------|
| **Decouple invoker from receiver** | Remote control doesn't know about TV internals |
| **Undo/Redo support** | Text editor reversing insert/delete operations |
| **Queue or log requests** | Job scheduler, macro recording, transaction log |
| **Parameterize actions at runtime** | Swap commands on a button without changing the button |
| **Composite commands (macros)** | Execute a batch of commands as a single action |

### When NOT to Use 🚫
- When the action is simple and direct (just call the method)
- When there's no need for undo, queuing, or decoupling
- When adding command objects introduces unnecessary complexity

---

## Command vs Strategy 📊

| Aspect | Command | Strategy |
|--------|---------|----------|
| Intent | Encapsulate a **request** as an object | Encapsulate an **algorithm** as an object |
| Undo | Supports undo/redo naturally | No built-in undo concept |
| Receiver | Command holds a reference to a receiver | Strategy is the algorithm itself |
| History | Commands are often stored in a stack/queue | Strategies are swapped, not accumulated |

---

## Basic Implementation 🛠️

### `command_1.py` — Remote Control

A remote control (invoker) that sends commands to TV and Stereo (receivers) without knowing their internals.

```python
# Command interface — declares the execute method
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Receiver — TV with on/off and channel switching
class TV(Device):
    def turn_on(self):
        logger.info("Turning on TV")
    def change_channel(self):
        logger.info("Changing channel")

# Concrete Command — delegates to the receiver
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device
    def execute(self):
        self.device.turn_on()

# Invoker — holds a command and triggers it
class RemoteControl:
    def set_command(self, command: Command):
        self.command = command  # swap at runtime
    def press_button(self):
        self.command.execute()  # invoke without knowing the receiver

# Usage
remote = RemoteControl()
remote.set_command(TurnOnCommand(tv))
remote.press_button()
```

### Sample Output

```
2026-02-19 10:00:00 - INFO - Remote set to: TurnOnCommand
2026-02-19 10:00:00 - INFO - Turning on TV
2026-02-19 10:00:00 - INFO - Remote set to: AdjustVolumeCommand
2026-02-19 10:00:00 - INFO - Adjusting volume
2026-02-19 10:00:00 - INFO - Remote set to: ChangeChannelCommand
2026-02-19 10:00:00 - INFO - Changing channel
2026-02-19 10:00:00 - INFO - Remote set to: TurnOffCommand
2026-02-19 10:00:00 - INFO - Turning off TV
```

---

## Real-World Example: Text Editor with Undo/Redo 🔧

See `example/` for a practical command pattern where a text editor supports reversible insert and delete operations via undo/redo stacks.

### Structure

```
example/
├── main.py             # Entry point — demos insert, undo, redo, delete
├── command.py          # Command interface with execute() + undo()
├── text_editor.py      # Receiver — holds text, performs insert/delete
├── commands.py         # Concrete commands — InsertCommand, DeleteCommand
└── command_manager.py  # Invoker — manages undo/redo stacks
```

### How It Works

```python
# Command interface — adds undo alongside execute
class Command(ABC):
    @abstractmethod
    def execute(self): ...
    @abstractmethod
    def undo(self): ...

# Receiver — holds text and performs operations
class TextEditor:
    def insert(self, content):
        self.text += content
    def delete(self, count):
        removed = self.text[-count:]
        self.text = self.text[:-count]
        return removed

# Concrete Command — insert is reversible via delete
class InsertCommand(Command):
    def execute(self):
        self.editor.insert(self.content)
    def undo(self):
        self.editor.delete(len(self.content))

# Concrete Command — delete saves removed text for undo
class DeleteCommand(Command):
    def execute(self):
        self.deleted_text = self.editor.delete(self.count)
    def undo(self):
        self.editor.insert(self.deleted_text)

# Invoker — two stacks for undo/redo
class CommandManager:
    def execute(self, command):
        command.execute()
        self.undo_stack.append(command)
        self.redo_stack.clear()  # new action invalidates redo
    def undo(self):
        command = self.undo_stack.pop()
        command.undo()
        self.redo_stack.append(command)
    def redo(self):
        command = self.redo_stack.pop()
        command.execute()
        self.undo_stack.append(command)
```

### Sample Output

```
2026-02-19 10:00:00 - INFO - Inserted: 'Hello' → text is now: 'Hello'
2026-02-19 10:00:00 - INFO - Inserted: ' World' → text is now: 'Hello World'
2026-02-19 10:00:00 - INFO - Current text: 'Hello World'
2026-02-19 10:00:00 - INFO - Deleted: ' World' → text is now: 'Hello'
2026-02-19 10:00:00 - INFO - After undo: 'Hello'
2026-02-19 10:00:00 - INFO - Inserted: ' World' → text is now: 'Hello World'
2026-02-19 10:00:00 - INFO - After redo: 'Hello World'
2026-02-19 10:00:00 - INFO - Deleted: 'World' → text is now: 'Hello '
2026-02-19 10:00:00 - INFO - After delete: 'Hello '
2026-02-19 10:00:00 - INFO - Inserted: 'World' → text is now: 'Hello World'
2026-02-19 10:00:00 - INFO - After undo delete: 'Hello World'
2026-02-19 10:00:00 - INFO - Inserted: '!' → text is now: 'Hello World!'
2026-02-19 10:00:00 - INFO - Final text: 'Hello World!'
```

---

## Design Principles at Play 📐

| Principle | How Command Applies |
|-----------|---------------------|
| **Single Responsibility** | Each command encapsulates one action; the invoker only triggers |
| **Open/Closed** | Add new commands without modifying the invoker or receivers |
| **Dependency Inversion** | Invoker depends on the `Command` abstraction, not concrete receivers |
| **Interface Segregation** | `Command` interface is minimal — just `execute()` and `undo()` |

---

## Running the Examples ▶️

```bash
# Run the basic remote control example
python command/src/command_1.py

# Run the text editor undo/redo example
cd command
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Command = Action as Object** — Encapsulate what to do, who does it, and how to reverse it
2. **Undo/Redo via Stacks** — Each command saves enough state to reverse itself; two stacks manage history
3. **Invoker Is Decoupled** — The remote/manager doesn't know about TV, Stereo, or TextEditor internals
4. **Swap at Runtime** — Assign different commands to the same invoker button dynamically
5. **New Action = New Class** — Adding a command never touches existing code
