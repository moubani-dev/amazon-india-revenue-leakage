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

| Column | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---|
| index | int64 | 128975 | 0 | 0.00% | 128975 | No issues detected |
| order_id | str | 128975 | 0 | 0.00% | 120378 | No issues detected |
| date | str | 128975 | 0 | 0.00% | 91 | No issues detected |
| status | str | 128975 | 0 | 0.00% | 13 | No issues detected |
| fulfilment | str | 128975 | 0 | 0.00% | 2 | No issues detected |
| sales_channel | str | 128975 | 0 | 0.00% | 2 | No issues detected |
| ship_service_level | str | 128975 | 0 | 0.00% | 2 | No issues detected |
| style | str | 128975 | 0 | 0.00% | 1377 | No issues detected |
| sku | str | 128975 | 0 | 0.00% | 7195 | No issues detected |
| category | str | 128975 | 0 | 0.00% | 9 | No issues detected |
| size | str | 128975 | 0 | 0.00% | 11 | No issues detected |
| asin | str | 128975 | 0 | 0.00% | 7190 | No issues detected |
| courier_status | str | 128975 | 6872 | 5.33% | 3 | Missing values |
| qty | int64 | 128975 | 0 | 0.00% | 10 | No issues detected |
| currency | str | 128975 | 7795 | 6.04% | 1 | Missing values |
| amount | float64 | 128975 | 7795 | 6.04% | 1410 | Missing values |
| ship_city | str | 128975 | 33 | 0.03% | 8955 | Missing values |
| ship_state | str | 128975 | 33 | 0.03% | 69 | Missing values |
| ship_postal_code | float64 | 128975 | 33 | 0.03% | 9459 | Missing values |
| ship_country | str | 128975 | 33 | 0.03% | 1 | Missing values |
| promotion_ids | str | 128975 | 49153 | 38.11% | 5787 | Missing values |
| b2b | bool | 128975 | 0 | 0.00% | 2 | No issues detected |
| fulfilled_by | str | 128975 | 89698 | 69.55% | 1 | Missing values |
| unnamed_22 | object | 128975 | 49050 | 38.03% | 1 | Missing values; Unnamed column |

### cloud warehouse compersion chart

| Column | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---|
| index | int64 | 50 | 0 | 0.00% | 50 | No issues detected |
| shiprocket | str | 50 | 29 | 58.00% | 21 | Missing values |
| unnamed_1 | str | 50 | 9 | 18.00% | 40 | Missing values; Unnamed column |
| increff | str | 50 | 22 | 44.00% | 27 | Missing values |

### expense iigf

| Column | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---|
| index | int64 | 17 | 0 | 0.00% | 17 | No issues detected |
| recived_amount | str | 17 | 11 | 64.71% | 6 | Missing values |
| unnamed_1 | str | 17 | 11 | 64.71% | 6 | Missing values; Unnamed column |
| expance | str | 17 | 2 | 11.76% | 15 | Missing values |
| unnamed_3 | str | 17 | 0 | 0.00% | 17 | Unnamed column |

### international sale report

| Column | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---|
| index | int64 | 37432 | 0 | 0.00% | 37432 | No issues detected |
| date | str | 37432 | 1 | 0.00% | 1326 | Missing values |
| months | str | 37432 | 25 | 0.07% | 571 | Missing values |
| customer | str | 37432 | 1040 | 2.78% | 172 | Missing values |
| style | str | 37432 | 1040 | 2.78% | 1065 | Missing values |
| sku | str | 37432 | 2474 | 6.61% | 4598 | Missing values |
| size | str | 37432 | 1040 | 2.78% | 36 | Missing values |
| pcs | str | 37432 | 1040 | 2.78% | 658 | Missing values |
| rate | str | 37432 | 1040 | 2.78% | 1339 | Missing values |
| gross_amt | str | 37432 | 1040 | 2.78% | 1208 | Missing values |

### may-2022

| Column | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---|
| index | int64 | 1330 | 0 | 0.00% | 1330 | No issues detected |
| sku | str | 1330 | 0 | 0.00% | 1330 | No issues detected |
| style_id | str | 1330 | 0 | 0.00% | 254 | No issues detected |
| catalog | str | 1330 | 0 | 0.00% | 9 | No issues detected |
| category | str | 1330 | 0 | 0.00% | 5 | No issues detected |
| weight | str | 1330 | 0 | 0.00% | 4 | No issues detected |
| tp | str | 1330 | 0 | 0.00% | 93 | No issues detected |
| mrp_old | str | 1330 | 0 | 0.00% | 67 | No issues detected |
| final_mrp_old | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| ajio_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| amazon_mrp | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| amazon_fba_mrp | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| flipkart_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| limeroad_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| myntra_mrp | str | 1330 | 0 | 0.00% | 51 | No issues detected |
| paytm_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| snapdeal_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |

### p  l march 2021

| Column | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---|
| index | int64 | 1330 | 0 | 0.00% | 1330 | No issues detected |
| sku | str | 1330 | 0 | 0.00% | 1330 | No issues detected |
| style_id | str | 1330 | 0 | 0.00% | 254 | No issues detected |
| catalog | str | 1330 | 0 | 0.00% | 9 | No issues detected |
| category | str | 1330 | 0 | 0.00% | 5 | No issues detected |
| weight | str | 1330 | 0 | 0.00% | 4 | No issues detected |
| tp_1 | str | 1330 | 0 | 0.00% | 93 | No issues detected |
| tp_2 | str | 1330 | 0 | 0.00% | 93 | No issues detected |
| mrp_old | str | 1330 | 0 | 0.00% | 67 | No issues detected |
| final_mrp_old | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| ajio_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| amazon_mrp | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| amazon_fba_mrp | str | 1330 | 0 | 0.00% | 53 | No issues detected |
| flipkart_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| limeroad_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| myntra_mrp | str | 1330 | 0 | 0.00% | 51 | No issues detected |
| paytm_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |
| snapdeal_mrp | str | 1330 | 0 | 0.00% | 52 | No issues detected |

### sale report

| Column | Data Type | Total Rows | Null Count | Null % | Unique Values | Issues Found |
|---|---|---:|---:|---:|---:|---|
| index | int64 | 9271 | 0 | 0.00% | 9271 | No issues detected |
| sku_code | str | 9271 | 83 | 0.90% | 9170 | Missing values |
| design_no | str | 9271 | 36 | 0.39% | 1594 | Missing values |
| stock | float64 | 9271 | 36 | 0.39% | 295 | Missing values |
| category | str | 9271 | 45 | 0.49% | 21 | Missing values |
| size | str | 9271 | 36 | 0.39% | 11 | Missing values |
| color | str | 9271 | 45 | 0.49% | 62 | Missing values |
