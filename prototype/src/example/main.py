import logging

from src.example.player import MagePrototype, WarriorPrototype, RoguePrototype
from src.example.player_client import PlayerClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    # Test 1: Create a mage, customize stats, and save (clone)
    logger.info("=== Test 1: Mage — create, customize, save ===")
    mage = MagePrototype(name='Gandalf')
    mage.display_user_profile()

    gandalf_stats = {'health': 60, 'attack': 60, 'defense': 80, 'magic': 90, 'speed': 20}
    mage.set_attributes(gandalf_stats)  # customize stats from dict
    mage.display_user_profile()

    client = PlayerClient(mage)
    saved_mage = client.save_player_profile()  # clone preserves customized stats
    saved_mage.display_user_profile()

    # Test 2: Create a warrior, save default profile
    logger.info("=== Test 2: Warrior — save with defaults ===")
    warrior = WarriorPrototype(name='Thorin')
    warrior.display_user_profile()

    warrior_clone = warrior.save()  # clone with default warrior stats
    warrior_clone.display_user_profile()

    # Test 3: Create a rogue, modify, and verify clone is independent
    logger.info("=== Test 3: Rogue — clone independence ===")
    rogue = RoguePrototype(name='Shadow')
    rogue_clone = rogue.save()

    rogue.set_attributes({'attack': 99})  # modify original after cloning
    logger.info(f"Original rogue attack: {rogue.attack}")
    logger.info(f"Cloned rogue attack: {rogue_clone.attack}")  # clone stays unchanged
    assert rogue_clone.attack == 12, "Clone should retain original attack value"
    logger.info("Test 3 passed: Clone is independent of original")

    # Test 4: set_attributes ignores unknown keys
    logger.info("=== Test 4: Unknown keys ignored ===")
    rogue2 = RoguePrototype(name='Viper')
    rogue2.set_attributes({'flight': True, 'health': 50})  # 'flight' doesn't exist
    assert not hasattr(rogue2, 'flight'), "Unknown key should not be set"
    assert rogue2.health == 50, "Known key should be updated"
    logger.info("Test 4 passed: Unknown keys safely ignored")

    # Test 5: PlayerClient works with any prototype type
    logger.info("=== Test 5: Client works with all types ===")
    for proto in [MagePrototype('M'), WarriorPrototype('W'), RoguePrototype('R')]:
        c = PlayerClient(proto)
        clone = c.save_player_profile()  # client doesn't know the concrete type
        clone.display_user_profile()
    logger.info("Test 5 passed: Client cloned all three types")
