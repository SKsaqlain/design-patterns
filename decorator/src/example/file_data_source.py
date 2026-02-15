from src.example.data_source import DataSource


# --- Concrete Component ---
# The base data source that decorators will wrap.
# Returns raw data without any modifications.
class FileDataSource(DataSource):

    # Simulates reading data from a file
    def fetch_data(self) -> str:
        return "fetching data"
