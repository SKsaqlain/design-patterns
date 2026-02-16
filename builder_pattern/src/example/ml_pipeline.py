from abc import ABC
from src.example.evaluation import Evaluation, F1Score
from src.example.model import LogisticRegression, Model
from src.example.preprocessing import Normalize, Preprocessing
from src.example.datasource import S3, DataSource


class MLPipeline():
    def __init__(self):
        self.data_source: DataSource = None
        self.preprocessing: Preprocessing = None
        self.model: Model = None
        self.evaluation: Evaluation = None

    def set_data_source(self, data_source: DataSource):
        self.data_source = data_source

    def set_preprocessing(self, preprocessing: Preprocessing):
        self.preprocessing = preprocessing

    def set_model(self, model:Model):
        self.model = model

    def set_evaluation(self, evaluation:Evaluation):
        self.evaluation = evaluation

    def get_pipeline_config(self):
        print(f"ML pipeline configuration : {self.data_source.name}, {self.preprocessing.name}, {self.model.name}, {self.evaluation.name}")



class MLPipelineBuilder(ABC):

    def add_data_source(self):
        pass
    
    def add_preprocessing_step(self):
        pass

    def add_model(self):
        pass

    def add_evaluation_step(self):
        pass

    def get_info(self):
        pass


class MLModelTest(MLPipelineBuilder):
    def __init__(self):
        self.ml_pipeline=MLPipeline()

    def add_data_source(self):
        self.ml_pipeline.set_data_source(S3())
    
    def add_preprocessing_step(self):
        self.ml_pipeline.set_preprocessing(Normalize())
    
    def add_model(self):
        self.ml_pipeline.set_model(LogisticRegression())
    
    def add_evaluation_step(self):
        self.ml_pipeline.set_evaluation(F1Score())
    
    def get_info(self):
        self.ml_pipeline.get_pipeline_config()


class MlModelTestDirector():
    def build_pipeline(self, ml_pipeline_builder: MLPipelineBuilder):
        ml_pipeline_builder.add_data_source()
        ml_pipeline_builder.add_preprocessing_step()
        ml_pipeline_builder.add_model()
        ml_pipeline_builder.add_evaluation_step()
