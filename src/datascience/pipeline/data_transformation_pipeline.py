from src.datascience.utils.configuration import ConfigurationManager
from src.datascience import logger
from src.datascience.components.data_transformation import DataTransformation
STAGE_NAME="Data Transformation Stage"
class DataTransformationPipeline:
    def __init__(self):
        pass
    def initiate_data_transformation(self):    
        config=ConfigurationManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()

if __name__=="__main__":
    try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e