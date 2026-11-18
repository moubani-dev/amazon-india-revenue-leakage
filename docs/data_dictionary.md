# Data Dictionary

## Project
Amazon India — Revenue Leakage & Profitability Command Center

## Purpose
This document describes the columns present in the seven
source datasets, their data types, business meanings, and
data quality observations.

## Source Datasets
1. Amazon Sale Report
2. Cloud Warehouse Compersion Chart
3. Expense IIGF
4. International Sale Report
5. May-2022
6. P L March 2021
7. Sale Report

## Column-Level Documentation

The following inventory is generated from the data quality report.
Column meanings will be documented after inspecting the source data.

### amazon sale report

**Dataset Description:** Main Amazon India order-level sales dataset. Includes order status, fulfilment, product, quantity, sales amount, shipping geography, promotions and B2B information.

| Column | Business Meaning | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---:|---|
| index | Original row index from the source file. | int64 | 128975 | 0 | 0.00% | 128975 | No issues detected |
| order_id | Amazon order identifier. | str | 128975 | 0 | 0.00% | 120378 | No issues detected |
| date | Date on which the order was placed. | str | 128975 | 0 | 0.00% | 91 | No issues detected |
| status | Current or recorded order status. | str | 128975 | 0 | 0.00% | 13 | No issues detected |
| fulfilment | Party responsible for fulfilling the order. | str | 128975 | 0 | 0.00% | 2 | No issues detected |
| sales_channel | Sales platform or channel. | str | 128975 | 0 | 0.00% | 2 | No issues detected |
| ship_service_level | Shipping service level selected for the order. | str | 128975 | 0 | 0.00% | 2 | No issues detected |
| style | Product style or design identifier. | str | 128975 | 0 | 0.00% | 1377 | No issues detected |
| sku | Stock Keeping Unit identifying a product variant. | str | 128975 | 0 | 0.00% | 7195 | No issues detected |
| category | Product category. | str | 128975 | 0 | 0.00% | 9 | No issues detected |
| size | Size of the ordered product. | str | 128975 | 0 | 0.00% | 11 | No issues detected |
| asin | Amazon Standard Identification Number. | str | 128975 | 0 | 0.00% | 7190 | No issues detected |
| courier_status | Recorded shipment or courier delivery status. | str | 128975 | 6872 | 5.33% | 3 | Missing values |
| qty | Quantity recorded for the order line. | int64 | 128975 | 0 | 0.00% | 10 | No issues detected |
| currency | Currency code associated with the order amount. | str | 128975 | 7795 | 6.04% | 1 | Missing values |
| amount | Recorded monetary amount for the order. | float64 | 128975 | 7795 | 6.04% | 1410 | Missing values |
| ship_city | Customer delivery city. | str | 128975 | 33 | 0.03% | 8955 | Missing values |
| ship_state | Customer delivery state. | str | 128975 | 33 | 0.03% | 69 | Missing values |
| ship_postal_code | Customer delivery postal PIN code. | float64 | 128975 | 33 | 0.03% | 9459 | Missing values |
| ship_country | Customer delivery country. | str | 128975 | 33 | 0.03% | 1 | Missing values |
| promotion_ids | Promotion identifiers associated with the order. | str | 128975 | 49153 | 38.11% | 5787 | Missing values |
| b2b | Boolean flag indicating whether the order is a business-to-business order. | bool | 128975 | 0 | 0.00% | 2 | No issues detected |
| fulfilled_by | Fulfilment service or party recorded in the source. | str | 128975 | 89698 | 69.55% | 1 | Missing values |
| unnamed_22 | Unlabelled source column; business meaning is not yet established. | object | 128975 | 49050 | 38.03% | 1 | Missing values; Unnamed column |

### cloud warehouse compersion chart

**Dataset Description:** Warehouse service comparison document containing Shiprocket and INCREFF charges, operational procedures, service-level targets and commercial terms.

| Column | Business Meaning | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---:|---|
| index | Original row index from the source file. | int64 | 50 | 0 | 0.00% | 50 | No issues detected |
| shiprocket | Warehouse service information associated with Shiprocket. | str | 50 | 29 | 58.00% | 21 | Missing values |
| unnamed_1 | Unlabelled comparison field; exact meaning requires further inspection. | str | 50 | 9 | 18.00% | 40 | Missing values; Unnamed column |
| increff | Warehouse service information associated with INCREFF. | str | 50 | 22 | 44.00% | 27 | Missing values |

### expense iigf

**Dataset Description:** Financial record containing received amounts and expense entries in two side-by-side sections. Includes dated receipts, expense descriptions, amounts and totals.

| Column | Business Meaning | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---:|---|
| index | Original row index from the source file. | int64 | 17 | 0 | 0.00% | 17 | No issues detected |
| recived_amount | Received amount recorded in the financial section. | str | 17 | 11 | 64.71% | 6 | Missing values |
| unnamed_1 | Unlabelled field between the receipt and expense sections. | str | 17 | 11 | 64.71% | 6 | Missing values; Unnamed column |
| expance | Expense description or expense entry. | str | 17 | 2 | 11.76% | 15 | Missing values |
| unnamed_3 | Unlabelled field associated with the expense section. | str | 17 | 0 | 0.00% | 17 | Unnamed column |

### international sale report

**Dataset Description:** International sales records containing dates, customers, product styles, SKUs, sizes, quantities, rates and gross amounts. Sample records belong to 2021.

| Column | Business Meaning | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---:|---|
| index | Original row index from the source file. | int64 | 37432 | 0 | 0.00% | 37432 | No issues detected |
| date | Date associated with the international sales record. | str | 37432 | 1 | 0.00% | 1326 | Missing values |
| months | Month associated with the sales record. | str | 37432 | 25 | 0.07% | 571 | Missing values |
| customer | Customer name or identifier. | str | 37432 | 1040 | 2.78% | 172 | Missing values |
| style | Product style or design identifier. | str | 37432 | 1040 | 2.78% | 1065 | Missing values |
| sku | Stock Keeping Unit identifying the product. | str | 37432 | 2474 | 6.61% | 4598 | Missing values |
| size | Product size recorded for the sale. | str | 37432 | 1040 | 2.78% | 36 | Missing values |
| pcs | Number of pieces sold. | str | 37432 | 1040 | 2.78% | 658 | Missing values |
| rate | Rate or price per piece. | str | 37432 | 1040 | 2.78% | 1339 | Missing values |
| gross_amt | Gross sales amount recorded for the transaction. | str | 37432 | 1040 | 2.78% | 1208 | Missing values |

### may-2022

**Dataset Description:** Product catalogue and marketplace pricing reference containing SKU, style, category, weight, transfer price and marketplace MRPs.

| Column | Business Meaning | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---:|---|
| index | Original row index from the source file. | int64 | 1330 | 0 | 0.00% | 1330 | No issues detected |
| sku | Stock Keeping Unit identifying the product. | str | 1330 | 0 | 0.00% | 1330 | No issues detected |
| style_id | Product style identifier. | str | 1330 | 0 | 0.00% | 254 | No issues detected |
| catalog | Product catalogue classification. | str | 1330 | 0 | 0.00% | 9 | No issues detected |
| category | Product category. | str | 1330 | 0 | 0.00% | 5 | No issues detected |
| weight | Product weight. | str | 1330 | 0 | 0.00% | 4 | No issues detected |
| tp | Transfer price recorded for the product. | str | 1330 | 0 | 0.00% | 93 | No issues detected |
| mrp_old | Original MRP. | str | 1330 | 0 | 0.00% | 67 | No issues detected |
| final_mrp_old | Final or adjusted old MRP. | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| ajio_mrp | MRP listed for Ajio. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| amazon_mrp | MRP listed for Amazon. | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| amazon_fba_mrp | MRP listed for Amazon FBA. | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| flipkart_mrp | MRP listed for Flipkart. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| limeroad_mrp | MRP listed for LimeRoad. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| myntra_mrp | MRP listed for Myntra. | str | 1330 | 0 | 0.00% | 51 | No issues detected |
| paytm_mrp | MRP listed for Paytm. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| snapdeal_mrp | MRP listed for Snapdeal. | str | 1330 | 0 | 0.00% | 52 | No issues detected |

### p  l march 2021

**Dataset Description:** Product pricing reference containing SKU, style, category, weight, two transfer-price fields and marketplace MRPs.

| Column | Business Meaning | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---:|---|
| index | Original row index from the source file. | int64 | 1330 | 0 | 0.00% | 1330 | No issues detected |
| sku | Stock Keeping Unit identifying the product. | str | 1330 | 0 | 0.00% | 1330 | No issues detected |
| style_id | Product style identifier. | str | 1330 | 0 | 0.00% | 254 | No issues detected |
| catalog | Product catalogue classification. | str | 1330 | 0 | 0.00% | 9 | No issues detected |
| category | Product category. | str | 1330 | 0 | 0.00% | 5 | No issues detected |
| weight | Product weight. | str | 1330 | 0 | 0.00% | 4 | No issues detected |
| tp_1 | First transfer-price field in the source. | str | 1330 | 0 | 0.00% | 93 | No issues detected |
| tp_2 | Second transfer-price field in the source. | str | 1330 | 0 | 0.00% | 93 | No issues detected |
| mrp_old | Original MRP. | str | 1330 | 0 | 0.00% | 67 | No issues detected |
| final_mrp_old | Final or adjusted old MRP. | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| ajio_mrp | MRP listed for Ajio. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| amazon_mrp | MRP listed for Amazon. | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| amazon_fba_mrp | MRP listed for Amazon FBA. | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| flipkart_mrp | MRP listed for Flipkart. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| limeroad_mrp | MRP listed for LimeRoad. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| myntra_mrp | MRP listed for Myntra. | str | 1330 | 0 | 0.00% | 51 | No issues detected |
| paytm_mrp | MRP listed for Paytm. | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| snapdeal_mrp | MRP listed for Snapdeal. | str | 1330 | 0 | 0.00% | 52 | No issues detected |

### sale report

**Dataset Description:** Inventory stock report containing SKU code, design number, available stock, category, size and colour.

| Column | Business Meaning | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---:|---|
| index | Original row index from the source file. | int64 | 9271 | 0 | 0.00% | 9271 | No issues detected |
| sku_code | Stock Keeping Unit code identifying the inventory item. | str | 9271 | 83 | 0.90% | 9170 | Missing values |
| design_no | Product design number. | str | 9271 | 36 | 0.39% | 1594 | Missing values |
| stock | Available stock quantity. | float64 | 9271 | 36 | 0.39% | 295 | Missing values |
| category | Product category. | str | 9271 | 45 | 0.49% | 21 | Missing values |
| size | Product size. | str | 9271 | 36 | 0.39% | 11 | Missing values |
| color | Product colour. | str | 9271 | 45 | 0.49% | 62 | Missing values |
