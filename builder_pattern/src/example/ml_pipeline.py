import logging
from abc import ABC, abstractmethod
from src.example.evaluation import Evaluation, F1Score
from src.example.model import LogisticRegression, Model
from src.example.preprocessing import Normalize, Preprocessing
from src.example.datasource import S3, DataSource

logger = logging.getLogger(__name__)


# --- Product ---
# The complex object being built step by step.
class MLPipeline():
    def __init__(self):
        # Each part of the pipeline starts empty until the builder sets it
        self.data_source: DataSource = None
        self.preprocessing: Preprocessing = None
        self.model: Model = None
        self.evaluation: Evaluation = None

    # Setters — called by the builder to assemble the product piece by piece
    def set_data_source(self, data_source: DataSource):
        self.data_source = data_source

    def set_preprocessing(self, preprocessing: Preprocessing):
        self.preprocessing = preprocessing

    def set_model(self, model: Model):
        self.model = model

    def set_evaluation(self, evaluation: Evaluation):
        self.evaluation = evaluation

    # Display the final assembled configuration
    def get_pipeline_config(self):
        logger.info(
            "ML pipeline configuration: %s, %s, %s, %s",
            self.data_source.name, self.preprocessing.name,
            self.model.name, self.evaluation.name
        )


# --- Builder Interface ---
# Declares the step-by-step methods needed to build an MLPipeline.
class MLPipelineBuilder(ABC):

    # Each step corresponds to one part of the MLPipeline product
    @abstractmethod
    def add_data_source(self):
        pass

    @abstractmethod
    def add_preprocessing_step(self):
        pass

    @abstractmethod
    def add_model(self):
        pass

    @abstractmethod
    def add_evaluation_step(self):
        pass

    # Returns the fully constructed product to the client
    @abstractmethod
    def get_result(self) -> MLPipeline:
        pass


# --- Concrete Builder ---
# Builds an ML test pipeline with S3, Normalize, LogisticRegression, F1Score.
class MLModelTest(MLPipelineBuilder):
    def __init__(self):
        self.ml_pipeline = MLPipeline()  # Initialize empty product

    # Each build step sets one component on the product
    def add_data_source(self):
        logger.info("Adding data source: S3")
        self.ml_pipeline.set_data_source(S3())

    def add_preprocessing_step(self):
        logger.info("Adding preprocessing: Normalize")
        self.ml_pipeline.set_preprocessing(Normalize())

    def add_model(self):
        logger.info("Adding model: LogisticRegression")
        self.ml_pipeline.set_model(LogisticRegression())

    def add_evaluation_step(self):
        logger.info("Adding evaluation: F1Score")
        self.ml_pipeline.set_evaluation(F1Score())

    # Hand the finished product back to the client
    def get_result(self) -> MLPipeline:
        return self.ml_pipeline


# --- Director ---
# Orchestrates the build steps in the correct order.
class MLModelTestDirector():
    # Defines the fixed build order — client doesn't need to know the steps
    def build_pipeline(self, ml_pipeline_builder: MLPipelineBuilder):
        logger.info("Director: building ML pipeline")
        ml_pipeline_builder.add_data_source()
        ml_pipeline_builder.add_preprocessing_step()
        ml_pipeline_builder.add_model()
        ml_pipeline_builder.add_evaluation_step()
