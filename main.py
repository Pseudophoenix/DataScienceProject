# def main():
#     print("Hello from datascienceproject!")
# if __name__ == "__main__":
#     main()
from src.datascience.pipeline.data_ingestion import DataIngestionTrainingPipeline
from src.datascience import logger
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