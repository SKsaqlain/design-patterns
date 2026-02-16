from abc import ABC, abstractmethod


# --- Product ---
# The complex object being built step by step.
class Computer():
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def set_cpu(self, cpu):
        self.cpu = cpu

    def set_ram(self, ram):
        self.ram = ram

    def set_storage(self, storage):
        self.storage = storage

    def display_info(self):
        print(f"Computer config: \nCPU: {self.cpu}\nRAM: {self.ram}\nStorage: {self.storage}\n")


# --- Builder Interface ---
# Declares the step-by-step methods needed to build a Computer.
class ComputerBuilder(ABC):

    @abstractmethod
    def build_cpu(self):
        pass

    @abstractmethod
    def build_ram(self):
        pass

    @abstractmethod
    def build_storage(self):
        pass

    # Returns the fully constructed product
    @abstractmethod
    def get_result(self) -> Computer:
        pass


# --- Concrete Builder ---
# Builds a gaming computer with high-end components.
class GamingComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    def build_cpu(self):
        self.computer.set_cpu('Gaming CPU')

    def build_ram(self):
        self.computer.set_ram('16GB DDR4')

    def build_storage(self):
        self.computer.set_storage('1TB SSD')

    def get_result(self) -> Computer:
        return self.computer


# --- Director ---
# Orchestrates the build steps in the correct order.
class ComputerDirector:
    def construct(self, builder: ComputerBuilder):
        builder.build_cpu()
        builder.build_ram()
        builder.build_storage()


if __name__ == '__main__':
    # Create a builder and let the director orchestrate the build
    gaming_builder = GamingComputerBuilder()
    director = ComputerDirector()
    director.construct(gaming_builder)
    # Retrieve the finished product
    gaming_computer = gaming_builder.get_result()
    gaming_computer.display_info()


    