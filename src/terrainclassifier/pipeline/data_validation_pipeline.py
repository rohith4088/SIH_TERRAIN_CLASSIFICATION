from terrainclassifier.config.configuration import ConfigurationManager
from terrainclassifier.conponents.data_validation_components import DataValiadtion
from terrainclassifier.logging import logger


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_files_exist()