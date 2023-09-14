# from terrainclassifier.logging import logger
# logger.info("hello")
from terrainclassifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from terrainclassifier.pipeline.data_validation_pipeline  import DataValidationTrainingPipeline
from terrainclassifier.logging import logger
STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f" STAGE {STAGE_NAME} COMPLETED<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
