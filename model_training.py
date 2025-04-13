from sklearn.cluster import KMeans
from logger import get_logger

logger = get_logger(__name__)

def train_model(df, n_clusters=5):
    try:
        required_cols = ['Annual_Income', 'Spending_Score']
        if not all(col in df.columns for col in required_cols):
            raise ValueError(f"Missing columns: {', '.join(set(required_cols) - set(df.columns))}")

        logger.info(f"Training KMeans with {n_clusters} clusters.")
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        df['Cluster'] = kmeans.fit_predict(df[required_cols])
        logger.info("Model training and clustering completed.")
        return df, kmeans
    except Exception as e:
        logger.error("Error in model training", exc_info=True)
        raise e
