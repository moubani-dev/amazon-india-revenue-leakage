
"""
DataLoader Module
-----------------
Loads the seven raw CSV files, standardizes column names,
inspects data quality and generates audit reports.
"""

import logging
import re
from pathlib import Path
from typing import Dict

import pandas as pd


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


class DataLoader:
    """
    Loads and audits the Amazon India e-commerce datasets.
    """

    def __init__(self, data_dir: str = "data/raw") -> None:
        """
        Initialize the DataLoader.

        Args:
            data_dir: Directory containing the raw CSV files.
        """

        self.data_dir = Path(data_dir)

        if not self.data_dir.exists():
            raise FileNotFoundError(
                f"Data directory not found: {self.data_dir}"
            )

        self.datasets: Dict[str, pd.DataFrame] = {}
        self.original_columns: Dict[str, list] = {}

        logger.info("DataLoader initialized: %s", self.data_dir)

    @staticmethod
    def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert column names into lowercase snake_case.
        """

        df = df.copy()

        standardized = []

        for column in df.columns:
            name = str(column).strip().lower()

            name = re.sub(r"[^a-z0-9]+", "_", name)
            name = name.strip("_")

            standardized.append(name)

        # Preserve uniqueness if two columns normalize identically
        seen = {}
        unique_columns = []

        for name in standardized:
            count = seen.get(name, 0)
            seen[name] = count + 1

            if count:
                name = f"{name}_{count}"

            unique_columns.append(name)

        df.columns = unique_columns

        return df

    def load_csv(self, filename: str) -> pd.DataFrame:
        """
        Load one CSV file without changing its original contents.

        Args:
            filename: Name of the CSV file.

        Returns:
            Loaded Pandas DataFrame.
        """

        file_path = self.data_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Dataset not found: {file_path}"
            )

        df = pd.read_csv(
            file_path,
            encoding="utf-8-sig",
            low_memory=False
        )

        logger.info(
            "Loaded %s | Rows: %s | Columns: %s",
            filename,
            df.shape[0],
            df.shape[1]
        )

        return df

    def load_all(self) -> Dict[str, pd.DataFrame]:
        """
        Load all seven project datasets.

        Returns:
            Dictionary containing all loaded DataFrames.
        """

        files = sorted(self.data_dir.glob("*.csv"))

        if len(files) != 7:
            logger.warning(
                "Expected 7 CSV files, found %s",
                len(files)
            )

        for file_path in files:

            filename = file_path.name

            df = self.load_csv(filename)

            dataset_name = file_path.stem.lower()

            self.original_columns[dataset_name] = list(df.columns)

            df = self.standardize_columns(df)

            self.datasets[dataset_name] = df

        logger.info(
            "Successfully loaded %s datasets.",
            len(self.datasets)
        )

        return self.datasets

    def inspect_data(self) -> pd.DataFrame:
        """
        Inspect dimensions, data types, nulls and duplicates.

        Returns:
            Dataset-level summary DataFrame.
        """

        if not self.datasets:
            raise ValueError(
                "No datasets loaded. Run load_all() first."
            )

        summaries = []

        for name, df in self.datasets.items():

            summary = {
                "dataset": name,
                "rows": df.shape[0],
                "columns": df.shape[1],
                "total_nulls": int(df.isnull().sum().sum()),
                "duplicate_rows": int(df.duplicated().sum()),
                "memory_mb": round(
                    df.memory_usage(deep=True).sum() / (1024 ** 2),
                    2
                )
            }

            summaries.append(summary)

            logger.info(
                "%s | Rows: %s | Columns: %s | Nulls: %s | Duplicates: %s",
                name,
                summary["rows"],
                summary["columns"],
                summary["total_nulls"],
                summary["duplicate_rows"]
            )

        return pd.DataFrame(summaries)

    def generate_quality_report(self) -> pd.DataFrame:
        """
        Generate a column-level data quality report.

        Returns:
            One row per dataset column.
        """

        if not self.datasets:
            raise ValueError(
                "No datasets loaded. Run load_all() first."
            )

        reports = []

        for dataset_name, df in self.datasets.items():

            for column in df.columns:

                series = df[column]

                null_count = int(series.isnull().sum())

                null_percentage = (
                    null_count / len(df) * 100
                    if len(df) > 0 else 0
                )

                unique_count = int(series.nunique(dropna=True))

                issues = []

                if null_count > 0:
                    issues.append("Missing values")

                if series.nunique(dropna=False) <= 1:
                    issues.append("Constant or empty column")

                if column.startswith("unnamed"):
                    issues.append("Unnamed column")

                reports.append({
                    "dataset": dataset_name,
                    "column": column,
                    "data_type": str(series.dtype),
                    "total_rows": len(df),
                    "null_count": null_count,
                    "null_percentage": round(null_percentage, 2),
                    "unique_values": unique_count,
                    "issues_found": (
                        "; ".join(issues) if issues else "No issues detected"
                    )
                })

        report = pd.DataFrame(reports)

        output_path = Path("data/processed")
        output_path.mkdir(parents=True, exist_ok=True)

        report.to_csv(
            output_path / "data_quality_report.csv",
            index=False
        )

        logger.info(
            "Data quality report saved successfully."
        )

        return report


if __name__ == "__main__":

    loader = DataLoader()

    loader.load_all()

    print("\nDATASET SUMMARY")
    print(loader.inspect_data().to_string(index=False))

    print("\nDATA QUALITY REPORT")
    report = loader.generate_quality_report()

    print(report.head(20).to_string(index=False))

    print("\nTotal columns audited:", len(report))
