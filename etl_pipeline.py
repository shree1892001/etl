from utils import setup_logging, load_config
from extract import extract_data
from transform import apply_transformations
from load import load_data

def main(config_path):
    config = load_config(config_path)

    logger = setup_logging(config["logging"]["log_level"], config["logging"]["log_path"])
    logger.info("Starting ETL pipeline")

    try:
        # Extract
        logger.info("Extracting data from source")
        df = extract_data(config["input"])

        # Transform
        logger.info("Transforming data")
        df_transformed = apply_transformations(df, config["transformations"])

        # Load
        logger.info("Loading data to destination")
        load_data(df_transformed, config["output"])

        logger.info("ETL pipeline executed successfully")

    except Exception as e:
        logger.error(f"Error in ETL pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    config_file_path = "D://ETL//config//config.json"
    main(config_file_path)
