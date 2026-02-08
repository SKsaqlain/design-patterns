
from abc import ABC,abstractmethod

class BankAccount(ABC):
    
    @abstractmethod
    def validate_user_identity(self,user_name:str,password:str):
        pass

    @abstractmethod
    def calculate_interest_rate(self):
        pass

    @abstractmethod
    def register_account():
        pass




