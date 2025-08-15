from src.datascience.components.data_ingestion import DataIngestion
from src.datascience.utils.configuration import ConfigurationManager
from src.datascience.utils.common import logger

try:
    config=ConfigurationManager()
    data_ingestion_config=config.get_data_ingestion_config()
    data_ingestion=DataIngestion(config=data_ingestion_config)
    data_ingestion.download_file()
    data_ingestion.extract_zip()
except Exception as e:
    logger.info(f"{e}")