
import threading

class SingletonDp():
    _instance=None
    # Lock ensures thread-safety: prevents race condition where multiple threads
    # could simultaneously check _instance==None and create multiple instances
    _lock=threading.Lock()
    # Track if __init__ has run, since __init__ is called every time we call SingletonDp()
    _initialized=False


    # __new__ is called BEFORE __init__ and controls object creation
    # Unlike __init__, it returns the instance (new or existing)
    # *args, **kwargs needed to accept arguments that will be passed to __init__
    def __new__(cls, *args, **kwargs):
        # First check (without lock) - fast path for when instance already exists
        if cls._instance==None:
            print("Creating new Class")
            # Acquire lock only when instance might need creation
            with cls._lock:
                # Second check (with lock) - ensures only one thread creates instance
                # Another thread may have created it while we waited for the lock
                if cls._instance==None:
                    # super() returns parent class (object), then we call its __new__(cls)
                    # object.__new__(cls) allocates memory and creates the actual instance
                    # We must pass 'cls' so it creates a SingletonDp instance, not a base object
                    cls._instance=super().__new__(cls)
        return cls._instance

    # __init__ is called EVERY time SingletonDp() is called, even if __new__ returns existing instance
    # So we need _initialized flag to ensure initialization logic runs only once
    def __init__(self, x, y):
        if not self._initialized:
            self._initialized = True
            print(x)
            print(y)
        else:
            print("Class already initialized")

    

if __name__=='__main__':
    # Test 1: First instantiation - should create new instance and initialize with (1,2)
    print("--- Creating c1 ---")
    c1 = SingletonDp(1, 2)
    print(f"c1: {c1}")

    # Test 2: Second instantiation - should return same instance, skip initialization
    print("\n--- Creating c2 ---")
    c2 = SingletonDp(2, 3)
    print(f"c2: {c2}")

    # Test 3: Third instantiation - same behavior as c2
    print("\n--- Creating c3 ---")
    c3 = SingletonDp(3, 4)
    print(f"c3: {c3}")

    # Verify all instances are the same object
    print("\n--- Verification ---")
    print(f"c1 is c2: {c1 is c2}")
    print(f"c2 is c3: {c2 is c3}")
    print(f"All same instance: {c1 is c2 is c3}")