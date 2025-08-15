from src.datascience.utils.configuration import ConfigurationManager
from src.datascience import logger
from src.datascience.components.model_evaluation import ModelEvaluation
STAGE_NAME="Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    def initaite_model_evaluation(self):
        try:
            config=ConfigurationManager()
            model_evaluation_config=config.get_model_evaluation_config()
            model_evaluation=ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e
if __name__=="__main__":
    try:
        logger.info(f">>>> Stage {STAGE_NAME} started <<<<<")
        obj=ModelEvaluation()
        obj.initaite_model_evaluation()
        logger.info(f">>>> Stage {STAGE_NAME} completed <<<<<\nx=========================x")
    except Exception as e:
        logger.exception(e)
        raise e