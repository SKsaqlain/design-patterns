import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


# Prototype interface — declares save (clone) and display for all player types
class PlayerPrototype(ABC):
    def __init__(self):
        self.name = "XYZ@123"  # default placeholder name
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.magic = 3
        self.speed = 3
        self.level = 1

    @abstractmethod
    def save(self):
        pass

    def set_attributes(self, params):
        for key, value in params.items():
            if hasattr(self, key):  # only set attributes that exist on the instance
                setattr(self, key, value)
                logger.debug(f"Set {key}={value} on {self.name}")

    @abstractmethod
    def display_user_profile(self):
        pass


# Concrete Prototype — Mage: high magic, low health and defense
class MagePrototype(PlayerPrototype):
    def __init__(self, name, health=80, attack=5, defense=3, magic=15, speed=2):
        super().__init__()
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        logger.info(f"Created MagePrototype '{name}'")

    def save(self):
        logger.info(f"Cloning MagePrototype '{self.name}'")
        return MagePrototype(  # clone with all current attribute values
            name=self.name,
            health=self.health,
            attack=self.attack,
            defense=self.defense,
            magic=self.magic,
            speed=self.speed,
        )

    def display_user_profile(self):
        logger.info(f"Mage Player Profile | [{self.name}] HP:{self.health} ATK:{self.attack} DEF:{self.defense} MAG:{self.magic} SPD:{self.speed} LVL:{self.level}")


# Concrete Prototype — Warrior: high health and defense, strong attack
class WarriorPrototype(PlayerPrototype):
    def __init__(self, name, health=150, attack=15, defense=12, magic=2, speed=3):
        super().__init__()
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        logger.info(f"Created WarriorPrototype '{name}'")

    def save(self):
        logger.info(f"Cloning WarriorPrototype '{self.name}'")
        return WarriorPrototype(  # clone with all current attribute values
            name=self.name,
            health=self.health,
            attack=self.attack,
            defense=self.defense,
            magic=self.magic,
            speed=self.speed,
        )

    def display_user_profile(self):
        logger.info(f"Warrior Player Profile | [{self.name}] HP:{self.health} ATK:{self.attack} DEF:{self.defense} MAG:{self.magic} SPD:{self.speed} LVL:{self.level}")


# Concrete Prototype — Rogue: fast speed, moderate attack, low defense
class RoguePrototype(PlayerPrototype):
    def __init__(self, name, health=90, attack=12, defense=4, magic=5, speed=10):
        super().__init__()
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        logger.info(f"Created RoguePrototype '{name}'")

    def save(self):
        logger.info(f"Cloning RoguePrototype '{self.name}'")
        return RoguePrototype(  # clone with all current attribute values
            name=self.name,
            health=self.health,
            attack=self.attack,
            defense=self.defense,
            magic=self.magic,
            speed=self.speed,
        )

    def display_user_profile(self):
        logger.info(f"Rogue Player Profile | [{self.name}] HP:{self.health} ATK:{self.attack} DEF:{self.defense} MAG:{self.magic} SPD:{self.speed} LVL:{self.level}")
