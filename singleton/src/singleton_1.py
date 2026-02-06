
import threading

class SingletonDp():
    _instance=None
    # Lock ensures thread-safety: prevents race condition where multiple threads
    # could simultaneously check _instance==None and create multiple instances
    _lock=threading.Lock()

    # @staticmethod: allows calling get_instance() without creating an object first
    # (SingletonDp.get_instance() instead of SingletonDp().get_instance())
    # No 'self' or 'cls' parameter needed - it's just a regular function inside the class
    @staticmethod
    def get_instance():
        # First check (without lock) - fast path for when instance already exists
        if SingletonDp._instance==None:
            # Acquire lock only when instance might need creation
            with SingletonDp._lock:
                # Second check (with lock) - ensures only one thread creates instance
                # Another thread may have created it while we waited for the lock
                if SingletonDp._instance==None:
                    SingletonDp._instance=SingletonDp()
        return SingletonDp._instance


if __name__ == '__main__':
    # Create multiple instances using get_instance()
    s1 = SingletonDp.get_instance()
    print(f"Instance 1: {s1}")

    s2 = SingletonDp.get_instance()
    print(f"Instance 2: {s2}")

    s3 = SingletonDp.get_instance()
    print(f"Instance 3: {s3}")

    # Verify all instances are the same object
    print(f"\ns1 is s2: {s1 is s2}")
    print(f"s2 is s3: {s2 is s3}")
    print(f"All same instance: {s1 is s2 is s3}")
