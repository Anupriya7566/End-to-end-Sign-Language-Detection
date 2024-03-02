from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.logger import logging


logging.info("welcome to my custom log")

obj = TrainPipeline()
obj.run_pipeline()
print("Training pipeline finished!")
