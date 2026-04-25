# ShopifyDataLake - Development Guide

## Project Overview

**ShopifyDataLake** is an ETL pipeline that extracts data from Shopify and loads it into ClickHouse for analytics and reporting.

## Tech Stack

| Layer | Technology |
|-------|------------|
| **Runtime** | Python 3.10+ |
| **Data** | Pandas, NumPy |
| **Warehouse** | ClickHouse |
| **API** | Shopify Admin API |

## Project Structure

```
ShopifyDataLake/
├── src/
│   ├── __init__.py
│   ├── cli.py              # CLI entry point
│   ├── pipeline.py         # Main ETL pipeline
│   ├── extract/
│   │   └── shopify.py      # Shopify API extractor
│   ├── transform/
│   │   ├── orders.py       # Order transformations
│   │   ├── products.py     # Product transformations
│   │   └── customers.py   # Customer transformations
│   ├── load/
│   │   └── clickhouse.py   # ClickHouse loader
│   └── schema/
│       └── tables.py       # Table definitions
├── requirements.txt
├── CLAUDE.md
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
# Full sync
python -m shopify_datalake --store mystore.myshopify.com --token shpat_xxx --full

# Incremental sync
python -m shopify_datalake --store mystore.myshopify.com --token shpat_xxx --incremental
```

## Data Tables

- `orders` - Order transactions with time dimensions
- `products` - Product catalog
- `customers` - Customer data
- `order_items` - Line item details

## LLM Integration

Uses MiniMax API for:
- Data quality checks
- Anomaly detection in data
- Natural language queries
- Report generation
