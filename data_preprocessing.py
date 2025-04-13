import pandas as pd
from logger import get_logger

logger = get_logger(__name__)

def load_data(filepath):
    try:
        logger.info(f"Loading data from: {filepath}")
        df = pd.read_csv(filepath)
        logger.info("Data loaded successfully.")
        return df
    except Exception as e:
        logger.error("Error loading data", exc_info=True)
        raise e
