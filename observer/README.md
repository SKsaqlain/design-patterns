# Observer Design Pattern 👁️

## What is Observer? 🎯

The **Observer** pattern defines a **one-to-many** dependency between objects so that when one object (the **Subject**) changes state, all its dependents (the **Observers**) are notified and updated automatically.

```
┌──────────────────┐        notifies        ┌──────────────────┐
│     Subject       │ ─────────────────────▶ │   Observer 1     │
│                   │                        └──────────────────┘
│  - observers[]    │        notifies        ┌──────────────────┐
│  + attach()       │ ─────────────────────▶ │   Observer 2     │
│  + detach()       │                        └──────────────────┘
│  + notify()       │        notifies        ┌──────────────────┐
│                   │ ─────────────────────▶ │   Observer 3     │
└──────────────────┘                         └──────────────────┘
```

---

## When to Use Observer? ⚡

| Use Case | Example |
|----------|---------|
| **Event Systems** | UI button clicks notifying multiple handlers |
| **Pub/Sub Messaging** | Message brokers distributing messages to subscribers |
| **Data Binding** | Model changes automatically updating the view |
| **Notifications** | A sensor change alerting multiple monitoring dashboards |
| **Logging/Auditing** | Multiple loggers observing system events |

### When NOT to Use 🚫
- When there's only one observer (a simple callback is enough)
- When the update order between observers matters and is complex
- When observers and subjects are tightly coupled anyway

---

## Basic Implementation 🛠️

### `observer_1.py` — Simple Subject-Observer

A minimal observer pattern with a Subject that notifies all attached Observers.

```python
# Observer interface — defines the contract for receiving notifications
class ObserverInterface(ABC):
    @abstractmethod
    def update(self, message: str) -> None:
        pass

# Concrete observer — prints the received message
class Observer(ObserverInterface):
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received message {message}")

# Subject — maintains a list of observers and notifies them on changes
class Subject():
    def __init__(self, topic: str):
        self.topic = topic
        self.observers: List = []

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, message):
        for observer in self.observers:
            observer.update(message)

# Usage
ob1 = Observer('observer_1')
ob2 = Observer('observer_2')

subject = Subject('topic_1')
subject.attach_observer(ob1)
subject.attach_observer(ob2)

subject.notify_observers("Hello")   # Both observers receive "Hello"
subject.detach_observer(ob2)        # ob2 won't receive future messages
```

**Key Takeaway:** The Subject doesn't know what its observers do — it just calls `update()`. Observers can be added/removed at runtime.

---

## Real-World Example: Weather Broker 🌤️

See `example/` for an async pub/sub system built on the observer pattern, using `asyncio` for concurrent message delivery.

### Structure

```
example/
├── main.py          # Sets up broker, producer, consumers and runs demo
├── broker.py        # Abstract Broker + WeatherBroker (manages topics, queues, offsets)
├── producer.py      # Abstract Producer + TemperatureProducer (publishes to brokers)
└── consumer.py      # Abstract Consumer + WeatherAppConsumer (receives messages)
```

### How It Works

```python
# Consumer (Observer) — gets notified via update()
class Consumer(ABC):
    async def update(self, message: str): ...

# Broker (Subject) — manages topics, subscriptions, and message delivery
class Broker(ABC):
    async def publish(self, topic: str, message: str): ...
    async def broadcast(self, topic: str): ...
    async def subscribe(self, consumer: Consumer, topic: str): ...
    async def create_topic(self, topic: str): ...

# Producer — pushes messages to brokers, which fan out to consumers
class Producer(ABC):
    async def produce(self, message: str): ...
    async def register_with_topic(self, broker: Broker, topic: str): ...

# Usage
weather_broker = WeatherBroker(broker_name='weather_broker')
await weather_broker.create_topic('temperature_topic')

temp_producer = TemperatureProducer(producer_name='temp_producer')
await temp_producer.register_with_topic(broker=weather_broker, topic='temperature_topic')

weather_app = WeatherAppConsumer(name='weather_app', topic='temperature_topic')
await weather_broker.subscribe(weather_app, topic='temperature_topic')

await temp_producer.produce("{'temperature: 15, measurement: C'}")
# weather_app receives the message via broker broadcast
```

### Sample Output

```
12:52:09 | INFO  | broker   | [weather_broker] creating new topic 'temperature_topic'
12:52:09 | INFO  | producer | [temp_producer] registering with broker 'weather_broker' on topic 'temperature_topic'
12:52:09 | INFO  | broker   | [weather_broker] weather_app subscribed to 'temperature_topic' with offset 0
12:52:09 | INFO  | broker   | [weather_broker] news_app subscribed to 'temperature_topic' with offset 0
12:52:09 | INFO  | producer | [temp_producer] pushing message to 1 topic(s): ['temperature_topic']
12:52:09 | INFO  | broker   | [weather_broker] broadcasting topic 'temperature_topic' to 2 consumer(s)
12:52:09 | INFO  | consumer | [weather_app] received message from topic 'temperature_topic': {'temperature: 15'}
12:52:09 | INFO  | consumer | [news_app] received message from topic 'temperature_topic': {'temperature: 15'}
```

---

## Design Principles at Play 📐

| Principle | How Observer Applies |
|-----------|----------------------|
| **Loose Coupling** | Subject only knows observers implement `update()` — nothing about their internals |
| **Open/Closed** | Add new observers without modifying the subject or existing observers |
| **Dependency Inversion** | Subject depends on the `ObserverInterface` abstraction, not concrete classes |
| **Single Responsibility** | Subject handles notification, each observer handles its own reaction |

---

## Quick Comparison: Simple vs Broker-Based 📊

| Aspect | Simple (`observer_1.py`) | Broker-Based (`example/`) |
|--------|--------------------------|---------------------------|
| Communication | Subject -> Observer directly | Producer -> Broker -> Consumer |
| Async support | No (synchronous) | Yes (`asyncio`) |
| Topic management | Single topic per subject | Multiple topics per broker |
| Message persistence | No | Yes (message queue + offsets) |
| Concurrency | Sequential notification | Concurrent via `asyncio.gather` |

---

## Running the Examples ▶️

```bash
# Run the basic observer example
python observer/src/observer_1.py

# Run the async weather broker example
cd observer/src/example
python main.py
```

---

## Key Takeaways 💡

1. **Observer = Notify Many** — One subject broadcasts to all registered observers
2. **Loose Coupling** — Subject and observers are independent; they only share the `update()` contract
3. **Dynamic Subscriptions** — Observers can attach/detach at runtime
4. **Scalable** — The broker-based approach adds topics, message queues, and async delivery for production-like patterns
