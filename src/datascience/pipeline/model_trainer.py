from src.datascience.utils.configuration import ConfigurationManager
from src.datascience.components.model_trainer import ModelTrainer
from src.datascience import logger
STAGE_NAME="Model Training Stage"
class ModelTrainerPipeline:
    def __init__(self):
        pass
    def initiate_model_train(self):
        try:
            config=ConfigurationManager()
            model_trainer_config=config.get_model_trainer_config()
            model_trainer=ModelTrainer(model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e
        

if __name__=="__main__":
    try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=ModelTrainerPipeline()
        obj.initiate_model_train()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e