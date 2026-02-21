from abc import ABC, abstractmethod

class PlayerPrototype(ABC):
    def __init__(self):
        self.name = "XYZ@123"
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
            if hasattr(self, key):
                setattr(self, key, value)
        
    @abstractmethod
    def display_user_profile(self):
        print(f"[{self.name}] HP:{self.health} ATK:{self.attack} DEF:{self.defense} MAG:{self.magic} SPD:{self.speed} LVL:{self.level}")


class MagePrototype(PlayerPrototype):
    def __init__(self, name, health=80, attack=5, defense=3, magic=15, speed=2):
        super().__init__()
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
    
    def save(self):
        return MagePrototype(
            name=self.name,
            health=self.health,
            attack=self.attack,
            defense=self.defense,
            magic=self.magic,
            speed=self.speed,
        )

    def display_user_profile(self):
        print(f"Mage Player Profile | [{self.name}] HP:{self.health} ATK:{self.attack} DEF:{self.defense} MAG:{self.magic} SPD:{self.speed} LVL:{self.level}")


class WarriorPrototype(PlayerPrototype):
    def __init__(self, name, health=150, attack=15, defense=12, magic=2, speed=3):
        super().__init__()
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed

    def save(self):
        return WarriorPrototype(
            name=self.name,
            health=self.health,
            attack=self.attack,
            defense=self.defense,
            magic=self.magic,
            speed=self.speed,
        )

    def display_user_profile(self):
        print(f"Warrior Player Profile | [{self.name}] HP:{self.health} ATK:{self.attack} DEF:{self.defense} MAG:{self.magic} SPD:{self.speed} LVL:{self.level}")


class RoguePrototype(PlayerPrototype):
    def __init__(self, name, health=90, attack=12, defense=4, magic=5, speed=10):
        super().__init__()
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed

    def save(self):
        return RoguePrototype(
            name=self.name,
            health=self.health,
            attack=self.attack,
            defense=self.defense,
            magic=self.magic,
            speed=self.speed,
        )

    def display_user_profile(self):
        print(f"Rouge Player Profile | [{self.name}] HP:{self.health} ATK:{self.attack} DEF:{self.defense} MAG:{self.magic} SPD:{self.speed} LVL:{self.level}")

