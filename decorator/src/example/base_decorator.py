from src.example.data_source import DataSource


# --- Base Decorator ---
# Wraps a DataSource and delegates calls to it.
# Concrete decorators extend this to add behavior (logging, modification, etc.).
class DataSourceDecorator(DataSource):

    def __init__(self, decorated_datasource: DataSource):
        # Hold a reference to the wrapped data source (composition)
        self.decorated_datasource = decorated_datasource

    # Default: pass through to the wrapped data source
    def fetch_data(self):
        return self.decorated_datasource.fetch_data()