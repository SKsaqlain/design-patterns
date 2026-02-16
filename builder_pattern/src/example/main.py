
    



    


    
    

from abc import ABC
from src.example.ml_pipeline import MLModelTest, MLPipeline, MlModelTestDirector
from src.example.evaluation import Evaluation, F1Score
from src.example.model import LogisticRegression, Model
from src.example.preprocessing import Normalize, Preprocessing
from src.example.datasource import S3, DataSource



if __name__=='__main__':
    ml_model_test=MLModelTest()
    ml_director=MlModelTestDirector()
    ml_director.build_pipeline(ml_model_test)
    ml_model_test.get_info()

    




        
