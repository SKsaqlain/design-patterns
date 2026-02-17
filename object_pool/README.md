# Object Pool Design Pattern 🏊

## What is Object Pool? 🎯

The **Object Pool** pattern manages a set of **pre-initialized, reusable objects** instead of creating and destroying them on demand. Clients **acquire** an object from the pool, use it, and **release** it back — avoiding the cost of repeated creation for expensive resources like database connections, threads, or sockets.

```
┌──────────────┐        acquire()         ┌──────────────────┐
│    Client    │ ──────────────────────▶  │    ObjectPool    │
│              │                          ├──────────────────┤
│              │  ◀────────────────────   │ - available [ ]  │
│  uses object │        release()         │ - max_size       │
└──────────────┘                          │ + acquire()      │
                                          │ + release()      │
                                          │ + close_all()    │
                                          └────────┬─────────┘
                                                   │ manages
                                          ┌────────▼─────────┐
                                          │  PooledObject    │
                                          │ (e.g. DB Conn)   │
                                          └──────────────────┘
```

---

## When to Use Object Pool? ⚡

| Use Case | Example |
|----------|---------|
| **Expensive object creation** | Database connections, network sockets, thread spawning |
| **Frequent acquire/release cycles** | Web server handling many short-lived requests |
| **Limited resources** | Connection limits, license seats, GPU memory slots |
| **Predictable demand** | Pre-allocate a known number of workers at startup |

### When NOT to Use 🚫
- When object creation is cheap (simple data classes, lightweight structs)
- When objects can't be reused (each use requires a fresh instance)
- When pool management overhead exceeds creation cost

---

## Object Pool vs Factory 📊

| Aspect | Factory | Object Pool |
|--------|---------|-------------|
| Lifecycle | Creates a **new** object every time | **Reuses** existing objects |
| Cost | Pays creation cost on each call | Pays creation cost once at init |
| Ownership | Caller owns the object | Pool owns the object; caller borrows it |
| Cleanup | Caller is responsible | Pool handles cleanup via `close_all()` |

---

## Basic Implementation 🛠️

### `object_pool_1.py` — Connection Pool

A synchronous pool that pre-creates `DatabaseConnection` objects and manages them via a list and dictionary.

```python
class DatabaseConnection:
    _connection_id = 0  # class-level counter shared across all instances

    def __init__(self):
        DatabaseConnection._connection_id += 1
        self.connection_id = DatabaseConnection._connection_id
        self.is_in_use = False

    def run(self, query):
        logger.info(f"Running query via connection #{self.connection_id}: {query}")


class ConnectionPool:
    def __init__(self, max_size):
        self.max_size = max_size
        self.available = []        # connections ready to be handed out
        self.in_use = dict()       # maps connection_id -> connection in use
        self.initialize_pool()     # pre-create all connections

    def get_db_connection(self):
        if len(self.in_use) < self.max_size:
            conn = self.available.pop(0)
            conn.is_in_use = True
            self.in_use[conn.connection_id] = conn
            return conn
        else:
            raise RuntimeError("No more connections available")

    def release(self, connection_id):
        conn = self.in_use[connection_id]
        conn.is_in_use = False
        self.available.append(conn)
        del self.in_use[connection_id]

# Usage
pool = ConnectionPool(2)
conn = pool.get_db_connection()
conn.run("SELECT * FROM users")
pool.release(conn.connection_id)
```

### Sample Output

```
2026-02-17 21:00:00 - INFO - Initializing connection pool with max size 2
2026-02-17 21:00:00 - INFO - Created DatabaseConnection #1
2026-02-17 21:00:00 - INFO - Created DatabaseConnection #2
2026-02-17 21:00:00 - INFO - Acquired connection #1 from pool
2026-02-17 21:00:00 - INFO - Running query via connection #1: SELECT * FROM users
2026-02-17 21:00:00 - INFO - Released connection #1 back to pool
```

---

## Real-World Example: Async SQLite Connection Pool 🔧

See `example/` for a practical async object pool using `asyncio.Queue` to manage SQLite database connections.

### Structure

```
example/
├── main.py                 # Entry point — runs 5 tests against the pool
├── object_pool.py          # Generic async ObjectPool (factory + asyncio.Queue)
└── database_connection.py  # Pooled resource — wraps sqlite3 connection
```

### How It Works

```python
# Generic async pool — works with any async factory
class ObjectPool:
    def __init__(self, object_factory, pool_size):
        self.object_factory = object_factory  # async callable that creates objects
        self.pool = asyncio.Queue(maxsize=pool_size)  # FIFO queue of available objects

    async def initialize(self):
        for _ in range(self.pool_size):
            obj = await self.object_factory()  # await the factory
            await self.pool.put(obj)

    async def acquire(self):
        return await self.pool.get()  # blocks if pool is empty

    async def release(self, obj):
        await self.pool.put(obj)  # return object for reuse

    async def close_all(self):
        while not self.pool.empty():
            obj = await self.pool.get()
            await obj.close_connection()

# Factory function
async def create_db_connection():
    return DatabaseConnection("object_pool.db")

# Usage
pool = ObjectPool(create_db_connection, pool_size=5)
await pool.initialize()
conn = await pool.acquire()
# ... use conn ...
await pool.release(conn)
await pool.close_all()
```


---

## Design Principles at Play 📐

| Principle | How Object Pool Applies |
|-----------|------------------------|
| **Single Responsibility** | `ObjectPool` manages lifecycle; `DatabaseConnection` handles queries |
| **Open/Closed** | Swap the factory to pool different resource types without changing `ObjectPool` |
| **Dependency Inversion** | Pool depends on an abstract factory callable, not a concrete class |
| **Interface Segregation** | `DatabaseConnection` exposes only `get_connection()` and `close_connection()` |

---

## Running the Examples ▶️

```bash
# Run the basic synchronous pool example
python object_pool/src/object_pool_1.py

# Run the async SQLite pool example
cd object_pool
python -m src.example.main
```

---

## Key Takeaways 💡

1. **Pool = Reuse Over Recreation** — Avoid expensive setup/teardown by borrowing and returning objects
2. **Pre-allocate at Startup** — Initialize all objects upfront so acquire is instant
3. **Bounded Resources** — The pool enforces a max size, preventing resource exhaustion
4. **Release Is Critical** — Always return objects to the pool, or it will eventually starve
5. **Async-Friendly** — `asyncio.Queue` makes pooling natural in async Python applications
