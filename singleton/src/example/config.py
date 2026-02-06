# Allows using "Config" as type hint inside the Config class itself
from __future__ import annotations
import os
from dataclasses import dataclass, field
from threading import Lock
# ClassVar: marks class-level variables that dataclass should ignore
# Optional: allows None as a valid value
from typing import Any, ClassVar, Dict, Optional

# init=False: prevent dataclass from generating __init__ that would reset values every time
@dataclass(init=False)
class Config():

    # Instance fields (dataclass will include these in __repr__ output)
    env: str = "dev"                # Current environment: dev, staging, prod
    debug: bool = False             # Enable debug mode
    db_url: str = "sqlite:///app.db"  # Database connection string
    # field(default_factory=dict) creates a new empty dict for each instance
    # Using default_factory avoids the mutable default argument pitfall
    extras: Dict[str,Any]=field(default_factory=dict)  # Additional custom config

    # ClassVar marks these as class-level variables, NOT instance fields
    # Without ClassVar, @dataclass treats them as instance attributes
    _instance: ClassVar[Optional["Config"]] = None
    _lock: ClassVar[Lock] = Lock()
    _initialized: ClassVar[bool] = False


    # __new__ controls object creation - called BEFORE __init__
    def __new__(cls,*args, **kwargs):
        # First check (without lock) - fast path when instance already exists
        if cls._instance==None:
            # Acquire lock for thread-safe instance creation
            with cls._lock:
                # Second check (with lock) - another thread may have created it while we waited
                if cls._instance==None:
                    # super().__new__(cls) actually allocates memory for the object
                    cls._instance=super().__new__(cls)
        return cls._instance

    # Custom __init__ with guard - only initializes once
    # Without init=False, dataclass would generate __init__ that resets values every time
    def __init__(self):
        if not Config._initialized:
            Config._initialized = True
            self.env = "dev"
            self.debug = False
            self.db_url = "sqlite:///app.db"
            self.extras = {}
            self._load_from_env()

    # Load config from environment variables, falling back to current values if not set
    # os.getenv(key, default) returns the env var value or default if not found
    def _load_from_env(self):
        self.env=os.getenv("APP_ENV", self.env)
        self.debug=os.getenv("APP_DEBUG",self.debug)
        self.db_url=os.getenv("APP_DB_URL",self.db_url)



    # Get a config value - first check if it's a known attribute, then check extras
    # hasattr() checks if object has an attribute, getattr() retrieves its value
    def get(self, key : str, default:Any= None):
        if hasattr(self,key):
            return getattr(self,key)
        else:
            # Key not a known field, look in extras dict
            return self.extras.get(key,default)

    # Set a config value - use setattr for known fields, extras dict for custom keys
    def set(self,key:str, value: Any):
        if hasattr(self,key):
            # setattr(obj, name, value) is equivalent to obj.name = value
            setattr(self,key,value)
        else:
            # Store unknown keys in extras dict for flexibility
            self.extras[key]=value
            
if __name__=='__main__':
    # Test 1: Create first config instance
    print("--- Test 1: Create config_1 ---")
    config_1 = Config()
    print(f"Initial: {config_1}")

    # Test 2: Modify config using set()
    print("\n--- Test 2: Modify config_1 ---")
    config_1.set("env", "prod")
    config_1.set("debug", True)
    config_1.set("api_key", "secret123")  # Goes to extras
    print(f"After set: {config_1}")

    # Test 3: Create second instance - should be same object with same values
    print("\n--- Test 3: Create config_2 (should be same instance) ---")
    config_2 = Config()
    print(f"config_2: {config_2}")

    # Test 4: Verify singleton - both are the same object
    print("\n--- Test 4: Verify singleton identity ---")
    print(f"config_1 is config_2: {config_1 is config_2}")

    # Test 5: Test get() method
    print("\n--- Test 5: Test get() method ---")
    print(f"config_2.get('env'): {config_2.get('env')}")
    print(f"config_2.get('debug'): {config_2.get('debug')}")
    print(f"config_2.get('api_key'): {config_2.get('api_key')}")  # From extras
    print(f"config_2.get('missing', 'default_val'): {config_2.get('missing', 'default_val')}")

    # Test 6: Changes in config_2 reflect in config_1 (same object)
    print("\n--- Test 6: Changes in config_2 reflect in config_1 ---")
    config_2.set("env", "staging")
    print(f"config_1.env after config_2.set(): {config_1.get('env')}")

