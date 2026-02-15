from src.example.base_decorator import DataSourceDecorator


# --- Concrete Decorator A ---
# Adds data modification behavior — converts fetched data to uppercase.
class UppercaseDecorator(DataSourceDecorator):

    # Fetch from wrapped source, then transform to uppercase
    def fetch_data(self):
        return self.decorated_datasource.fetch_data().upper()
