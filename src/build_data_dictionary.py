
from pathlib import Path
import pandas as pd

# Project paths
report_path = Path("data/processed/data_quality_report.csv")
dictionary_path = Path("docs/data_dictionary.md")

# Load the data quality report
df = pd.read_csv(report_path)

# Start with the existing introduction.
# Replace the generated section if this script is run again.
existing_text = dictionary_path.read_text(encoding="utf-8")
marker = "## Column-Level Documentation"

if marker in existing_text:
    introduction = existing_text.split(marker)[0].rstrip()
else:
    introduction = existing_text.rstrip()

sections = [
    "## Column-Level Documentation",
    "",
    "The following inventory is generated from the data quality report.",
    "Column meanings will be documented after inspecting the source data.",
    ""
]

# Create one table for each dataset
for dataset, group in df.groupby("dataset", sort=False):

    sections.append(f"### {dataset}")
    sections.append("")
    sections.append(
        "| Column | Data Type | Total Rows | Null Count | "
        "Null % | Unique Values | Issues Found |"
    )
    sections.append(
        "|---|---|---:|---:|---:|---:|---|"
    )

    for _, row in group.iterrows():
        sections.append(
            f"| {row['column']} "
            f"| {row['data_type']} "
            f"| {row['total_rows']} "
            f"| {row['null_count']} "
            f"| {row['null_percentage']:.2f}% "
            f"| {row['unique_values']} "
            f"| {row['issues_found']} |"
        )

    sections.append("")

# Write the updated dictionary
final_text = introduction + "\n\n" + "\n".join(sections)
dictionary_path.write_text(final_text, encoding="utf-8")

print("Data dictionary generated successfully.")
print("Total documented columns:", len(df))
print("Datasets documented:", df["dataset"].nunique())
print("Updated file:", dictionary_path)
