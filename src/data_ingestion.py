from pathlib import Path
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# Step 1: Define project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data" / "raw"

FREQ_PATH = DATA_DIR / "freMTPL2freq.parquet"
SEV_PATH = DATA_DIR / "freMTPL2sev.parquet"


# Step 2: Create a reusable data loading function
def load_data(file_path: Path) -> pd.DataFrame:
    """Load a Parquet file into a Pandas DataFrame."""
    if not file_path.is_file():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    logger.info("Loading dataset: %s", file_path.name)

        


    df = pd.read_parquet(file_path, engine="pyarrow")

    logger.info(
            "Dataset loaded: %s | Rows: %d | Columns: %d",
            file_path.name,
            df.shape[0],
            df.shape[1]
        )
    return df



# Step 3: Main execution function
def main():
    
    
    print("Starting insurance data ingestion...")

    # Load policy frequency data
    freq = load_data(FREQ_PATH)

    # Load individual claim severity data
    sev = load_data(SEV_PATH)

    # Display dataset information
    print("\n=== FREQUENCY DATASET ===")
    print(freq.head())
    print("Shape:", freq.shape)
    freq.info()

    print("\n=== SEVERITY DATASET ===")
    print(sev.head())
    print("Shape:", sev.shape)
    sev.info()

    print("\nData ingestion completed successfully.")


# Step 4: Python entry point
if __name__ == "__main__":
    main()
