from abc import ABC,abstractmethod

class Model(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def run_model(self):
        pass

class LogisticRegression(Model):
    def __init__(self):
        super().__init__("Logistic_Regression")
    
    def run_model(self):
        print(f"Running logistic regression")