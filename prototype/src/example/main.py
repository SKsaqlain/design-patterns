


from src.example.player import MagePrototype
from src.example.player_client import PlayerClient


if __name__=='__main__':
    mage_profile=MagePrototype(name='Gandalf')
    mage_profile.display_user_profile()
    client=PlayerClient(mage_profile)

    gandalf_profile={'health':60,'attack':60,'defence':80,'magic':90,'speed':20}
    mage_profile.set_attributes(gandalf_profile)
    
    
    saved_profile=mage_profile.save()
    saved_profile.display_user_profile()


    
    

