
from abc import ABC,abstractmethod

class Preprocessing(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def run_preprocessing(self):
        pass

class Normalize(Preprocessing):
    def __init__(self):
        super().__init__('Normalize')
    
    def run_preprocessing(self):
        print(f"performing normalization on the data")