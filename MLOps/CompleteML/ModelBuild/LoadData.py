import pandas as pd
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data_operations.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger()

def load_data(file_path,sep=','):
    try:
        # Load the dataset
        Source = pd.read_csv(file_path,sep)
        Source['index'] = Source.index
        logger.info(f"Dataset loaded successfully. Size: {Source.shape} (rows, columns).")
        return Source
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
    except pd.errors.EmptyDataError:
        logger.error("The file is empty.")
    except pd.errors.ParserError as e:
        logger.error(f"Error parsing the file: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    return None
