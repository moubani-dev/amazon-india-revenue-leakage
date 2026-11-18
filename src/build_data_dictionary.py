
from pathlib import Path
import pandas as pd

DATASET_DESCRIPTIONS = {
    "amazon sale report": "Main Amazon India order-level sales dataset. Includes order status, fulfilment, product, quantity, sales amount, shipping geography, promotions and B2B information.",

    "cloud warehouse compersion chart": "Warehouse service comparison document containing Shiprocket and INCREFF charges, operational procedures, service-level targets and commercial terms.",

    "expense iigf": "Financial record containing received amounts and expense entries in two side-by-side sections. Includes dated receipts, expense descriptions, amounts and totals.",

    "international sale report": "International sales records containing dates, customers, product styles, SKUs, sizes, quantities, rates and gross amounts. Sample records belong to 2021.",

    "may-2022": "Product catalogue and marketplace pricing reference containing SKU, style, category, weight, transfer price and marketplace MRPs.",

    "p  l march 2021": "Product pricing reference containing SKU, style, category, weight, two transfer-price fields and marketplace MRPs.",

    "sale report": "Inventory stock report containing SKU code, design number, available stock, category, size and colour."
}

COLUMN_MEANINGS = {
    "amazon sale report": {
        "index": "Original row index from the source file.",
        "order_id": "Amazon order identifier.",
        "date": "Date on which the order was placed.",
        "status": "Current or recorded order status.",
        "fulfilment": "Party responsible for fulfilling the order.",
        "sales_channel": "Sales platform or channel.",
        "ship_service_level": "Shipping service level selected for the order.",
        "style": "Product style or design identifier.",
        "sku": "Stock Keeping Unit identifying a product variant.",
        "category": "Product category.",
        "size": "Size of the ordered product.",
        "asin": "Amazon Standard Identification Number.",
        "courier_status": "Recorded shipment or courier delivery status.",
        "qty": "Quantity recorded for the order line.",
        "currency": "Currency code associated with the order amount.",
        "amount": "Recorded monetary amount for the order.",
        "ship_city": "Customer delivery city.",
        "ship_state": "Customer delivery state.",
        "ship_postal_code": "Customer delivery postal PIN code.",
        "ship_country": "Customer delivery country.",
        "promotion_ids": "Promotion identifiers associated with the order.",
        "b2b": "Boolean flag indicating whether the order is a business-to-business order.",
        "fulfilled_by": "Fulfilment service or party recorded in the source.",
        
        "unnamed_22": "Unlabelled source column; business meaning is not yet established."
    },

    "cloud warehouse compersion chart": {
        "index": "Original row index from the source file.",
        "shiprocket": "Warehouse service information associated with Shiprocket.",
        "unnamed_1": "Unlabelled comparison field; exact meaning requires further inspection.",
        "increff": "Warehouse service information associated with INCREFF."
    },

    "expense iigf": {
        "index": "Original row index from the source file.",
        "recived_amount": "Received amount recorded in the financial section.",
        "unnamed_1": "Unlabelled field between the receipt and expense sections.",
        "expance": "Expense description or expense entry.",
        "unnamed_3": "Unlabelled field associated with the expense section."
    },

    "international sale report": {
        "index": "Original row index from the source file.",
        "date": "Date associated with the international sales record.",
        "months": "Month associated with the sales record.",
        "customer": "Customer name or identifier.",
        "style": "Product style or design identifier.",
        "sku": "Stock Keeping Unit identifying the product.",
        "size": "Product size recorded for the sale.",
        "pcs": "Number of pieces sold.",
        "rate": "Rate or price per piece.",
        "gross_amt": "Gross sales amount recorded for the transaction."
    },

    "may-2022": {
        "index": "Original row index from the source file.",
        "sku": "Stock Keeping Unit identifying the product.",
        "style_id": "Product style identifier.",
        "catalog": "Product catalogue classification.",
        "category": "Product category.",
        "weight": "Product weight.",
        "tp": "Transfer price recorded for the product.",
        "mrp_old": "Original MRP.",
        "final_mrp_old": "Final or adjusted old MRP.",
        "ajio_mrp": "MRP listed for Ajio.",
        "amazon_mrp": "MRP listed for Amazon.",
        "amazon_fba_mrp": "MRP listed for Amazon FBA.",
        "flipkart_mrp": "MRP listed for Flipkart.",
        "limeroad_mrp": "MRP listed for LimeRoad.",
        "myntra_mrp": "MRP listed for Myntra.",
        "paytm_mrp": "MRP listed for Paytm.",
        "snapdeal_mrp": "MRP listed for Snapdeal."
    },

    "p  l march 2021": {
        "index": "Original row index from the source file.",
        "sku": "Stock Keeping Unit identifying the product.",
        "style_id": "Product style identifier.",
        "catalog": "Product catalogue classification.",
        "category": "Product category.",
        "weight": "Product weight.",
        "tp_1": "First transfer-price field in the source.",
        "tp_2": "Second transfer-price field in the source.",
        "mrp_old": "Original MRP.",
        "final_mrp_old": "Final or adjusted old MRP.",
        "ajio_mrp": "MRP listed for Ajio.",
        "amazon_mrp": "MRP listed for Amazon.",
        "amazon_fba_mrp": "MRP listed for Amazon FBA.",
        "flipkart_mrp": "MRP listed for Flipkart.",
        "limeroad_mrp": "MRP listed for LimeRoad.",
        "myntra_mrp": "MRP listed for Myntra.",
        "paytm_mrp": "MRP listed for Paytm.",
        "snapdeal_mrp": "MRP listed for Snapdeal."
    },

    "sale report": {
        "index": "Original row index from the source file.",
        "sku_code": "Stock Keeping Unit code identifying the inventory item.",
        "design_no": "Product design number.",
        "stock": "Available stock quantity.",
        "category": "Product category.",
        "size": "Product size.",
        "color": "Product colour."
    }
}


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

    description = DATASET_DESCRIPTIONS.get(
        dataset,
        "Description not available."
    )

    sections.append(f"**Dataset Description:** {description}")
    sections.append("")
    sections.append(
        "| Column | Business Meaning | Data Type | Total Rows | Null Count | "
        "Null % | Unique Values | Issues Found |"
    )
    sections.append(
        "|---|---|---:|---:|---:|---:|---:|---|"
    )

    for _, row in group.iterrows():
            meaning = COLUMN_MEANINGS.get(dataset, {}).get(
                row["column"],
                "Meaning to be documented."
            )


            sections.append(
                f"| {row['column']} "
                f"| {meaning} "
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
