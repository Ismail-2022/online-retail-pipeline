# Online Retail Transaction Analytics

End-to-end data pipeline and business intelligence dashboard built on Databricks, analyzing two years of transactions from a UK-based online retailer to surface revenue trends, customer value, and product performance.

## Business Problem

Online retailers sit on transaction data that, left unprocessed, can't answer basic operating questions: which markets drive revenue, which customers are worth retaining, and which products deserve inventory and marketing focus. This project builds a production-style pipeline that turns raw transaction logs into decision-ready insights — the kind of foundation a retail analytics or growth team would use to prioritize retention campaigns, market expansion, and stock planning.

## Architecture

Built using the **medallion architecture** pattern on Databricks with Delta Lake and Unity Catalog:

```
Bronze (raw)  →  Silver (cleaned)  →  Gold (business aggregates)  →  Dashboard
```

| Layer | Purpose | Key steps |
|---|---|---|
| **Bronze** | Land raw data as-is | Ingest CSV source into a Delta table, no transformation |
| **Silver** | Clean, validated, analysis-ready data | Remove returns/cancellations, drop null customer IDs, dedupe, enforce types, compute per-line revenue |
| **Gold** | Business-facing aggregates | Monthly revenue by country, customer lifetime value, top products by revenue |

Dashboard is built in **Databricks Lakeview**, querying directly off the Gold layer tables.

## Key Findings

- **Total revenue analyzed: £8.84M** across the full transaction history
- **UK dominates revenue concentration** — ~82% of total revenue originates from the United Kingdom, with the remaining ~18% spread across 15+ other countries (Netherlands, EIRE, Germany, France among the next largest)
- **Customer value is concentrated** — the top 10 customers by lifetime spend each contribute well above the median, highlighting clear retention targets
- **A small set of SKUs drive outsized revenue** — products like *Regency Cakestand*, *Paper Craft* items, and *White Hanging Heart* decorations rank consistently among top revenue drivers

## Dashboard

![Online Retail Dashboard](dashboards/Dashboard1.png)

![Online Retail Dashboard](dashboards/Dashboard2.png)

*Interactive version built in Databricks Lakeview (not publicly hostable — screenshot above reflects the live dashboard).*

## Repository Structure

```
online-retail-pipeline/
├── notebooks/
│   ├── 01_bronze_ingestion.py      # Raw ingestion into Delta
│   ├── 02_silver_transform.py      # Cleaning and enrichment
│   └── 03_gold_aggregation.py      # Business aggregates
├── sql/
│   ├── monthly_revenue_trend.sql
│   ├── top_customers.sql
│   ├── top_products.sql
│   └── kpi_summary.sql
├── dashboards/
│   └── revenue_dashboard.png
└── README.md
```

## Tech Stack

- **Databricks** (Unity Catalog, Delta Lake, Lakeview Dashboards)
- **PySpark / Spark SQL**
- **Delta Lake** for ACID-compliant, versioned table storage
- **Medallion architecture** (Bronze/Silver/Gold)

## Dataset

[Online Retail II](https://archive.ics.uci.edu/dataset/502/online+retail+ii) — real transaction records (Dec 2009 – Dec 2011) from a UK-based online retailer, sourced from the UCI Machine Learning Repository.

## Reproducing This Project

1. Upload the Online Retail II CSV to a Unity Catalog Volume
2. Run notebooks in order: `01_bronze_ingestion` → `02_silver_transform` → `03_gold_aggregation`
3. Create a Lakeview dashboard against the resulting `gold` schema tables using the queries in `sql/`
