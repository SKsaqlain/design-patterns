from abc import ABC,abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass    
    @abstractmethod
    def turn_off(self):
        pass

class TV(Device):
    def turn_off(self):
        print("Turning off TV")
    def turn_on(self):
        print("Turning on TV")
    def change_channel(self):
        print("Chaning channel")

class Stereo(Device):
    def turn_off(self):
        print("Turning stereo off")
    
    def turn_on(self):
        print("Turning stereo on")
    
    def adjust_volume(self):
        print("Adjusting Volume")

class TurnOnCommand(Command):
    def __init__(self, device):
        self.device=device
    def execute(self):
        self.device.turn_on()

class TurnOffCommand(Command):
    def __init__(self, device):
        self.device=device
    def execute(self):
        self.device.turn_off()

class AdjustVolumeCommand(Command):
    def __init__(self,stereo):
        self.stereo=stereo
    def execute(self):
        self.stereo.adjust_volume()

class ChangeChannelCommand(Command):
    def __init__(self, tv):
        self.tv=tv
    def execute(self):
        self.tv.change_channel()


class RemoteControl:
    def __init__(self):
        self.command=None
    
    def set_command(self,command: Command):
        self.command=command
    
    def press_button(self):
        self.command.execute()


if __name__=='__main__':
    tv=TV()
    stereo=Stereo()

    turn_on_tv_command=TurnOnCommand(tv)
    turn_off_tv_command=TurnOffCommand(tv)
    adjust_volume_command=AdjustVolumeCommand(stereo=stereo)
    change_channel=ChangeChannelCommand(tv)


    
    remote=RemoteControl()
    remote.set_command(turn_on_tv_command)
    remote.press_button()

    remote.set_command(adjust_volume_command)
    remote.press_button()

    remote.set_command(change_channel)
    remote.press_button()

    remote.set_command(turn_off_tv_command)
    remote.press_button()

    


        