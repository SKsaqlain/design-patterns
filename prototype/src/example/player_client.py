from src.example.player import PlayerPrototype


class PlayerClient:
    def __init__(self, player_prototype: PlayerPrototype):
        self.player_prototype= player_prototype

    def save_player_profile(self):
        return self.player_prototype.save()