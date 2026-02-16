from abc import ABC,abstractmethod


class Evaluation(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def run_evaluation(self):
        pass

class F1Score(Evaluation):
    def __init__(self):
        super().__init__('F1_Score')
    
    def run_evaluation(self):
        print(f"Running F1 Score evaluation on model")
