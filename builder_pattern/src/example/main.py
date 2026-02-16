import logging

from src.example.ml_pipeline import MLModelTest, MLModelTestDirector

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)-7s | %(name)-20s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


if __name__ == '__main__':
    logger.info("=== Builder Pattern — ML Pipeline Example ===")

    # Create a concrete builder — knows which components to use
    ml_builder = MLModelTest()

    # Director orchestrates the build steps in the correct order
    director = MLModelTestDirector()
    director.build_pipeline(ml_builder)

    # Retrieve the finished product from the builder
    ml_pipeline = ml_builder.get_result()
    ml_pipeline.get_pipeline_config()  # Display the assembled pipeline
