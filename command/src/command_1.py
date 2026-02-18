import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# Command interface — declares the execute method all commands must implement
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Receiver interface — declares basic device operations
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# Concrete Receiver — TV with channel switching capability
class TV(Device):
    def turn_on(self):
        logger.info("Turning on TV")

    def turn_off(self):
        logger.info("Turning off TV")

    def change_channel(self):
        logger.info("Changing channel")


# Concrete Receiver — Stereo with volume control
class Stereo(Device):
    def turn_on(self):
        logger.info("Turning stereo on")

    def turn_off(self):
        logger.info("Turning stereo off")

    def adjust_volume(self):
        logger.info("Adjusting volume")


# Concrete Command — delegates turn_on to any device
class TurnOnCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_on()


# Concrete Command — delegates turn_off to any device
class TurnOffCommand(Command):
    def __init__(self, device):
        self.device = device

    def execute(self):
        self.device.turn_off()


# Concrete Command — specific to Stereo receiver
class AdjustVolumeCommand(Command):
    def __init__(self, stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.adjust_volume()


# Concrete Command — specific to TV receiver
class ChangeChannelCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.change_channel()


# Invoker — holds a command and triggers it on button press
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command: Command):
        self.command = command  # swap the active command at runtime
        logger.info(f"Remote set to: {command.__class__.__name__}")

    def press_button(self):
        self.command.execute()  # invoke without knowing the receiver


if __name__ == '__main__':
    tv = TV()  # receiver 1
    stereo = Stereo()  # receiver 2

    # wrap each action in a command object
    turn_on_tv_command = TurnOnCommand(tv)
    turn_off_tv_command = TurnOffCommand(tv)
    adjust_volume_command = AdjustVolumeCommand(stereo=stereo)
    change_channel = ChangeChannelCommand(tv)

    remote = RemoteControl()  # invoker — decoupled from receivers

    remote.set_command(turn_on_tv_command)
    remote.press_button()

    remote.set_command(adjust_volume_command)
    remote.press_button()

    remote.set_command(change_channel)
    remote.press_button()

    remote.set_command(turn_off_tv_command)
    remote.press_button()
