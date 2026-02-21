import logging

from src.example.player import PlayerPrototype

logger = logging.getLogger(__name__)


# Client — uses a prototype to save (clone) player profiles without knowing the concrete type
class PlayerClient:
    def __init__(self, player_prototype: PlayerPrototype):
        self.player_prototype = player_prototype  # holds any player prototype
        logger.info(f"PlayerClient initialized with '{player_prototype.name}' prototype")

    def save_player_profile(self):
        saved = self.player_prototype.save()  # delegate cloning to the prototype
        logger.info(f"Saved player profile for '{saved.name}'")
        return saved
