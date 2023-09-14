#pipeline
from terrainclassifier.config.configuration import ConfigurationManager
from terrainclassifier.conponents.data_ingestion_components import DataIngestion
from terrainclassifier.logging import logger


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()