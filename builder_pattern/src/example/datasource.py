from abc import ABC, abstractmethod


class DataSource(ABC):
    def __init__(self,name):
        self.name=name
    
    @abstractmethod
    def fetch_data(self):
        pass


class S3(DataSource):
    def __init__(self):
        super().__init__('S3')
    
    def fetch_data(self):
        print(f"Fetching data from S3")