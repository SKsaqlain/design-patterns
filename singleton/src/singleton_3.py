
import threading

class SingletonDp():
    _instance=None
    # Lock ensures thread-safety: prevents race condition where multiple threads
    # could simultaneously check _instance==None and create multiple instances
    _lock=threading.Lock()
    # Track if instance has been initialized
    _initialized=False

    # @classmethod: like @staticmethod but receives 'cls' (the class) as first parameter
    # This makes it subclass-friendly - cls refers to the actual class being called
    # Unlike @staticmethod which hardcodes the class name (e.g., SingletonDp._instance)
    @classmethod
    def get_instance(cls, x, y):
        # First check (without lock) - fast path for when instance already exists
        if cls._instance is None:
            # Acquire lock only when instance might need creation
            with cls._lock:
                # Second check (with lock) - ensures only one thread creates instance
                # Another thread may have created it while we waited for the lock
                if cls._instance is None:
                    # Create instance using object.__new__ directly
                    cls._instance = object.__new__(cls)
                    # Initialize the instance (only happens once)
                    cls._instance._initialized = True
                    print(f"Creating new instance with x={x}, y={y}")
                    cls._instance.x = x
                    cls._instance.y = y
        return cls._instance


if __name__=='__main__':
    # Test 1: First call - should create new instance and initialize with (1,2)
    print("--- Creating c1 ---")
    c1 = SingletonDp.get_instance(1, 2)
    print(f"c1: {c1}, x={c1.x}, y={c1.y}")

    # Test 2: Second call - should return same instance, ignore new arguments
    print("\n--- Creating c2 ---")
    c2 = SingletonDp.get_instance(2, 3)
    print(f"c2: {c2}, x={c2.x}, y={c2.y}")

    # Test 3: Third call - same behavior as c2
    print("\n--- Creating c3 ---")
    c3 = SingletonDp.get_instance(3, 4)
    print(f"c3: {c3}, x={c3.x}, y={c3.y}")

    # Verify all instances are the same object
    print("\n--- Verification ---")
    print(f"c1 is c2: {c1 is c2}")
    print(f"c2 is c3: {c2 is c3}")
    print(f"All same instance: {c1 is c2 is c3}")
