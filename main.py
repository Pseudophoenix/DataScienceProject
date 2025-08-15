# def main():
#     print("Hello from datascienceproject!")
# if __name__ == "__main__":
#     main()
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience import logger
from src.datascience.pipeline.data_validation import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer import ModelTrainerPipeline
from src.datascience.pipeline.model_evaluation import ModelEvaluationPipeline
STAGE_NAME="Data Ingestion stage"

logger.info('Welcome to our custom logging data science')
try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Data Validation stage"
try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME="Data Validation stage"
try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
except Exception as e:
        logger.exception(e)
        raise e
STAGE_NAME="Model Training Stage"
try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=ModelTrainerPipeline()
        obj.initiate_model_train()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME="Model Evaluation Stage"

try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=ModelEvaluationPipeline()
        obj.initaite_model_evaluation()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
except Exception as e:
        logger.exception(e)
        raise e