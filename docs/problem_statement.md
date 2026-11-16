
# Revenue Leakage & Profitability Command Center
## Amazon India — Business Problem Statement

**Project:** NYCTA Data Analytics Program — Project 02  
**Domain:** E-Commerce Analytics  
**Business:** Indian Ethnic-Wear Brand  
**Marketplace:** Amazon India  
**Analysis Period:** April–June 2022  
**Prepared by:** Moubani Das

---

## 1. Business Background

A fast-growing Indian ethnic-wear brand sells kurtas, sets, sarees and western dresses through Amazon India and other e-commerce marketplaces.

Although sales are increasing, the company's actual cash realization and profitability are not growing at the same rate.

The management suspects revenue leakage caused by cancellations, returns to seller, inventory stock-outs, dead stock and inconsistent product pricing across marketplaces.

The company needs a data-driven solution to identify where revenue is being lost, quantify the financial impact in Indian Rupees (₹), and prioritize corrective actions.

## 2. Stakeholder

**Primary Stakeholder:** Company Founder / Business Owner.

**Supporting Stakeholders:**
- Finance and Accounts Team
- Inventory and Warehouse Managers
- Marketplace Operations Team
- Pricing and Product Managers

## 3. Business Problem

The organization currently lacks a unified analytical system to understand the difference between gross sales and net realized revenue.

The main challenges include:

1. Revenue loss through cancellations and returns.
2. High leakage in specific product categories, sizes and SKUs.
3. Demand variations across Indian states and cities.
4. Inventory shortages for best-selling products.
5. Dead stock occupying warehouse space.
6. Inconsistent pricing across marketplaces.
7. Limited ability to identify high-risk orders before dispatch.
8. Lack of reliable short-term demand forecasting.

## 4. Project Objectives

The project aims to:

- Quantify revenue leakage in ₹ and percentage terms.
- Identify the products, categories and locations responsible for maximum leakage.
- Analyze order outcomes and fulfilment performance.
- Identify stock-out risks and dead inventory.
- Compare marketplace pricing and estimate margins.
- Develop a machine learning model to predict cancellation and return risks.
- Forecast demand for the next 14 days for the top three categories.
- Build an interactive Streamlit dashboard for business decision-making.
- Provide prioritized recommendations with estimated financial impact.

## 5. KPI Tree

### Level 1: Gross Sales

Total sales value before accounting for cancellations and returns.

### Level 2: Revenue Leakage

Financial value associated with:
- Cancelled orders
- Returns to seller

### Level 3: Net Realised Revenue

Gross Sales minus quantified revenue leakage.

### Supporting KPIs

| KPI | Purpose |
|---|---|
| Gross Sales | Measure total sales value |
| Net Realised Revenue | Measure revenue after leakage |
| Leakage Amount (₹) | Quantify financial losses |
| Leakage Rate (%) | Measure leakage relative to gross sales |
| Average Order Value | Measure average order value |
| Units Sold | Measure product demand |
| Cancellation Rate | Monitor cancellations |
| Return Rate | Monitor returns |
| Stock-out Risk SKUs | Identify inventory shortages |
| Dead Stock Value | Estimate capital tied up in unsold inventory |
| Price Parity Gap | Identify marketplace pricing differences |

## 6. Key Business Questions

1. How much gross sales revenue is lost through cancellations and returns?
2. Which categories, sizes and SKUs experience the highest leakage?
3. Which states and cities generate the most demand?
4. Does Amazon fulfilment perform better than merchant fulfilment?
5. Do promotions increase order value or attract more returns?
6. How do B2B orders differ from B2C orders?
7. Which 20% of SKUs generate approximately 80% of revenue?
8. Which products face stock-out risks and which represent dead stock?
9. Where do marketplace prices differ and how does this affect margins?
10. Which orders have the highest cancellation or return risk?
11. What will demand look like over the next 14 days?
12. Which six actions can recover the most money?

## 7. Project Scope

### Included

- Data ingestion and quality auditing.
- Data cleaning and feature engineering.
- SQLite star schema and advanced SQL.
- Exploratory data analysis.
- Statistical hypothesis testing.
- Revenue leakage diagnostics.
- Inventory and pricing analysis.
- Predictive modelling.
- Demand forecasting.
- Streamlit dashboard development.
- Business insights and recommendations.

### Excluded

- Direct access to Amazon's live seller account.
- Real-time order processing.
- Actual bank settlement reconciliation.
- Guaranteed future revenue recovery.

## 8. Assumptions

1. The provided dataset represents historical Amazon India seller activity from April to June 2022.
2. Order status will determine the order outcome after examining the actual status values.
3. Orders still in transit will not automatically be treated as revenue leakage.
4. Missing values will be investigated before deciding whether to remove, retain or impute them.
5. Transfer price will be used as a cost proxy for margin estimation, as specified in the project brief.
6. Inventory and marketplace SKU keys may require reconciliation.
7. Historical demand patterns may not represent future market conditions.
8. Only information supported by the supplied datasets will be used in final business recommendations.

## 9. Expected Deliverables

- Cleaned and documented datasets.
- Data quality report.
- Data dictionary.
- SQLite database and ER diagram.
- 15+ advanced SQL queries.
- 15+ EDA visualizations.
- Revenue leakage waterfall analysis.
- Statistical hypothesis tests.
- Inventory and pricing intelligence.
- Cancellation and return risk model.
- 14-day demand forecast.
- Multi-page Streamlit dashboard.
- 10–12 business insights.
- Six prioritized recommendations.
- Executive summary PDF.
- GitHub repository and deployed application.

## 10. Expected Business Outcome

The final Revenue Leakage & Profitability Command Center will provide management with a unified view of revenue performance, financial leakage, inventory health, pricing differences and predictive risk.

It will transform raw e-commerce data into actionable business intelligence, helping the company make better operational and financial decisions.

---

**Project Prepared By:** Moubani Das  
**Program:** NYCTA Data Analytics Program  
**Project Number:** 02 / 10
