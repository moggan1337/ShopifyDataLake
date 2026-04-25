# ShopifyDataLake

<p align="center">
  <img src="https://img.shields.io/badge/Shopify-Analytics-95BF47?style=for-the-badge&logo=shopify&logoColor=white" alt="Shopify">
  <img src="https://img.shields.io/badge/ClickHouse-DB-FF6B6B?style=for-the-badge&logo=clickhouse&logoColor=white" alt="ClickHouse">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Apache%20Kafka-Streaming-231F20?style=for-the-badge&logo=apachekafka&logoColor=white" alt="Kafka">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/PRs-Welcome-blue?style=for-the-badge" alt="PRs Welcome">
</p>

> 📊 **Real-time ETL Analytics Pipeline** — Build a powerful data warehouse from Shopify with ClickHouse, real-time streaming via Kafka, custom dashboards, cohort analysis, and advanced analytics.

## About

ShopifyDataLake is an enterprise-grade ETL pipeline that syncs your Shopify data into a high-performance ClickHouse data warehouse, enabling deep analytics and custom dashboards that aren't possible with Shopify's native analytics. It provides real-time webhook-based sync, incremental loads, and pre-built Grafana/Superset dashboards for cohort analysis, LTV, and RFM segmentation. Built for data engineers and analysts who need advanced analytics capabilities beyond Shopify's native reporting.

## ✨ Features

### Data Pipeline
- ⚡ **Real-time Sync** — Webhook-based instant data updates (< 1 second latency)
- 📥 **Historical Import** — Bulk import all historical data with progress tracking
- 🔄 **Incremental Loads** — Delta syncs for efficiency and speed
- 🗄️ **Data Lake** — Raw + processed data storage in ClickHouse
- 🔌 **Kafka Integration** — Event streaming for real-time analytics
- 📦 **S3/MinIO** — Blob storage for media and backups

### Analytics
- 📈 **Sales Analytics** — Revenue, orders, AOV, conversion rates
- 👥 **Customer Analytics** — Cohort analysis, churn, RFM segmentation, LTV
- 📦 **Product Analytics** — Bestsellers, margins, return rates, inventory
- 🏪 **Vendor Analytics** — Per-vendor performance (if using ShopifyMarketHub)
- 🌐 **Marketing Analytics** — Attribution, campaign performance
- 🛒 **Cart Analytics** — Abandonment rates, recovery funnels

### Dashboards & Visualization
- 📊 **Pre-built Dashboards** — Ready-made Grafana dashboard templates
- 🎨 **Custom Dashboards** — Build your own with drag-drop Superset
- 📱 **Mobile App** — Native iOS/Android dashboard apps
- 📧 **Scheduled Reports** — Automated email reports to stakeholders
- 🔔 **Alerts** — Anomaly detection and threshold alerts

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            ShopifyDataLake                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                         Shopify Store                              │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐│  │
│  │  │  Products   │  │   Orders    │  │  Customers  │  │  Refunds  ││  │
│  │  │             │  │             │  │             │  │           ││  │
│  │  │ • Variants  │  │ • Line Items │  │ • Addresses │  │ • Reason  ││  │
│  │  │ • Inventory │  │ • Fulfillments│ │ • Orders   │  │ • Amount  ││  │
│  │  │ • Collections│ │ • Refunds   │  │ • Lifetime  │  │           ││  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘│  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                    │                                     │
│  ┌─────────────────────────────────┴─────────────────────────────────┐  │
│  │                        Ingestion Layer                              │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌───────────┐│  │
│  │  │  Webhooks   │  │   Admin     │  │    CSV      │  │    API     ││  │
│  │  │ (Real-time) │  │   Import    │  │   Import    │  │   Polling  ││  │
│  │  │             │  │ (Historical)│  │ (Bulk Load) │  │ (Scheduled)││  │
│  │  │ • Orders    │  │ • Products  │  │ • Backup    │  │ • Inventory││  │
│  │  │ • Customers │  │ • Orders    │  │ • Legacy    │  │            ││  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └───────────┘│  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                    │                                     │
│  ┌─────────────────────────────────┴─────────────────────────────────┐  │
│  │                      Processing Layer                              │  │
│  │  ┌───────────────────────────────────────────────────────────────┐ │  │
│  │  │              Apache Kafka / Redpanda                           │ │  │
│  │  │  Topics:                                                       │ │  │
│  │  │  • orders.created    • products.updated    • customers.new   │ │  │
│  │  │  • orders.paid       • inventory.changed    • refunds.issued  │ │  │
│  │  └───────────────────────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                    │                                     │
│  ┌─────────────────────────────────┴─────────────────────────────────┐  │
│  │                         Storage Layer                             │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────────┐│  │
│  │  │  ClickHouse  │  │ PostgreSQL  │  │    Redis    │  │  S3/MinIO ││  │
│  │  │ (Analytics) │  │ (Metadata)  │  │   (Cache)   │  │  (Blobs)  ││  │
│  │  │             │  │             │  │             │  │          ││  │
│  │  │ • orders    │  │ • sync_state│  │ • dashboards│  │ • backups ││  │
│  │  │ • products   │  │ • pipelines │  │ • queries   │  │ • raw_data││  │
│  │  │ • customers  │  │             │  │             │  │          ││  │
│  │  │ • events    │  │             │  │             │  │          ││  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └──────────┘│  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                    │                                     │
│  ┌─────────────────────────────────┴─────────────────────────────────┐  │
│  │                    Query & Visualization                          │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────────┐│  │
│  │  │   Grafana   │  │  Superset   │  │   Custom    │  │   API     ││  │
│  │  │ Dashboards  │  │   Charts    │  │   React     │  │ (FastAPI) ││  │
│  │  │             │  │             │  │             │  │          ││  │
│  │  │ • Sales     │  │ • Trends    │  │ • Reports   │  │ • SQL    ││  │
│  │  │ • Customers │  │ • Funnels   │  │ • Exports   │  │ • Export ││  │
│  │  │ • Products   │  │ • Cohorts   │  │ • Alerts    │  │          ││  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └──────────┘│  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/moggan1337/ShopifyDataLake.git
cd ShopifyDataLake

# Start infrastructure with Docker
docker-compose up -d clickhouse kafka minio postgres

# Install Python packages
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env

# Configure .env with your credentials:
# - SHOPIFY_STORE_DOMAIN=your-store.myshopify.com
# - SHOPIFY_ACCESS_TOKEN=shpat_xxxxx
# - CLICKHOUSE_HOST=localhost
# - KAFKA_BOOTSTRAP_SERVERS=localhost:9092

# Run database migrations
python scripts/init_db.py

# Start the ETL pipeline
python -m etl.pipeline
```

## 🚀 Quick Start

```bash
# 1. Configure Shopify credentials
export SHOPIFY_STORE_DOMAIN=your-store.myshopify.com
export SHOPIFY_ACCESS_TOKEN=shpat_xxxxx

# 2. Start infrastructure
docker-compose up -d clickhouse kafka

# 3. Run initial sync
python -m etl sync --mode=full --entity=orders

# 4. Check data in ClickHouse
clickhouse-client --query "SELECT COUNT(*) FROM orders"

# 5. Start real-time pipeline
python -m etl pipeline --mode=realtime

# 6. Access dashboards
# Grafana: http://localhost:3000
# Superset: http://localhost:8088
```

## 🛠️ Commands Reference

### `etl sync`

Synchronize data from Shopify.

```bash
# Full sync (all entities)
python -m etl sync --mode=full

# Incremental sync (delta only)
python -m etl sync --mode=incremental

# Sync specific entity
python -m etl sync --entity=orders
python -m etl sync --entity=products
python -m etl sync --entity=customers

# Sync with date range
python -m etl sync --entity=orders --start=2024-01-01 --end=2024-12-31

# Sync with parallelism
python -m etl sync --entity=orders --workers=4
```

### `etl pipeline`

Run the real-time pipeline.

```bash
# Start real-time pipeline
python -m etl pipeline --mode=realtime

# Start batch pipeline
python -m etl pipeline --mode=batch --schedule="0 * * * *"

# Dry run (show what would be processed)
python -m etl pipeline --dry-run

# Start with Kafka
python -m etl pipeline --mode=realtime --kafka
```

### `etl query`

Query the data warehouse.

```bash
# Run SQL query
python -m etl query "SELECT COUNT(*) FROM orders WHERE created_at > '2024-01-01'"

# Export to CSV
python -m etl query --sql-file=queries/top_products.sql --format=csv --output=./output.csv

# Save as dashboard
python -m etl query --sql="SELECT *" --save-as=top-products --refresh=hourly
```

## 📁 Project Structure

```
shopify-datalake/
├── src/
│   ├── __init__.py
│   ├── cli.py                   # CLI entry point
│   ├── pipeline.py              # Main ETL orchestrator
│   ├── extract/
│   │   ├── shopify.py           # Shopify API extractor
│   │   ├── webhooks.py          # Webhook handlers
│   │   └── csv_importer.py      # CSV bulk import
│   ├── transform/
│   │   ├── orders.py            # Order transformations
│   │   ├── products.py          # Product transformations
│   │   ├── customers.py         # Customer transformations
│   │   └── events.py            # Event processing
│   ├── load/
│   │   ├── clickhouse.py        # ClickHouse loader
│   │   └── kafka_producer.py    # Kafka producer
│   └── schema/
│       ├── tables.py            # ClickHouse table definitions
│       └── migrations.py        # Schema migrations
├── scripts/
│   ├── init_db.py               # Database initialization
│   ├── backfill.py              # Historical data backfill
│   └── seed_dashboards.py       # Dashboard templates
├── kafka/
│   ├── docker-compose.yml       # Kafka infrastructure
│   └── topics.yml               # Topic definitions
├── dashboards/
│   ├── grafana/                 # Grafana dashboard JSON
│   └── superset/                # Superset dashboard exports
├── queries/
│   ├── sales.sql
│   ├── customers.sql
│   ├── products.sql
│   └── cohorts.sql
├── tests/
│   ├── extract/
│   ├── transform/
│   └── load/
├── requirements.txt
├── config.yaml
└── README.md
```

## 📊 ClickHouse Schema

### Orders Table

```sql
CREATE TABLE orders (
    id UInt64,
    order_id String,
    order_number UInt32,
    email String,
    created_at DateTime,
    updated_at DateTime,
    total_price Decimal(10, 2),
    subtotal_price Decimal(10, 2),
    total_tax Decimal(10, 2),
    total_shipping Decimal(10, 2),
    total_discounts Decimal(10, 2),
    currency String,
    financial_status String,
    fulfillment_status String,
    customer_id UInt64,
    customer_email String,
    customer_created_at DateTime,
    customer_orders_count UInt32,
    customer_total_spent Decimal(12, 2),
    customer_tags Array(String),
    shipping_address_city String,
    shipping_address_country String,
    shipping_address_province String,
    browser_ip String,
    user_agent String,
    landing_site String,
    source_url String,
    created_date Date DEFAULT toDate(created_at),
    created_month Date DEFAULT toDate(created_at)
) ENGINE = MergeTree()
ORDER BY (created_date, order_id)
PARTITION BY toYYYYMM(created_date);
```

### Products Table

```sql
CREATE TABLE products (
    id UInt64,
    product_id String,
    title String,
    handle String,
    vendor String,
    product_type String,
    tags Array(String),
    created_at DateTime,
    updated_at DateTime,
    published_at DateTime,
    price Decimal(10, 2),
    compare_at_price Decimal(10, 2),
    inventory_quantity Int32,
    inventory_policy String,
    is_active Bool,
    is_deleted Bool,
    total_sold UInt64,
    total_revenue Decimal(12, 2),
    created_date Date DEFAULT toDate(created_at)
) ENGINE = MergeTree()
ORDER BY (created_date, product_id)
PARTITION BY toYYYYMM(created_date);
```

### Customers Table

```sql
CREATE TABLE customers (
    id UInt64,
    customer_id String,
    email String,
    first_name String,
    last_name String,
    phone String,
    created_at DateTime,
    updated_at DateTime,
    orders_count UInt32,
    total_spent Decimal(12, 2),
    state String,
    tags Array(String),
    verified_email Bool,
    accepts_marketing Bool,
    last_order_id String,
    last_order_date DateTime,
    first_order_date DateTime,
    customer_lifetime_value Decimal(12, 2),
    days_since_last_order UInt32,
    churn_risk String  -- high, medium, low
) ENGINE = MergeTree()
ORDER BY (created_at, customer_id);
```

## 🔧 Configuration

### Environment Variables

```env
# Shopify Configuration
SHOPIFY_STORE_DOMAIN=your-store.myshopify.com
SHOPIFY_ACCESS_TOKEN=shpat_xxxxx
SHOPIFY_API_VERSION=2024-10

# ClickHouse
CLICKHOUSE_HOST=localhost
CLICKHOUSE_PORT=9000
CLICKHOUSE_DATABASE=shopify
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=xxxxx

# Kafka
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC_PREFIX=shopify

# PostgreSQL (metadata)
DATABASE_URL=postgresql://user:pass@localhost:5432/datalake

# Redis (cache)
REDIS_URL=redis://localhost:6379

# S3/MinIO (blob storage)
S3_ENDPOINT=http://localhost:9000
S3_ACCESS_KEY=xxxxx
S3_SECRET_KEY=xxxxx
S3_BUCKET=shopify-datalake

# Grafana
GRAFANA_URL=http://localhost:3000
GRAFANA_API_KEY=xxxxx

# Superset
SUPERSET_URL=http://localhost:8088
SUPERSET_API_KEY=xxxxx
```

### config.yaml

```yaml
shopify:
  store_domain: "${SHOPIFY_STORE_DOMAIN}"
  access_token: "${SHOPIFY_ACCESS_TOKEN}"
  api_version: "2024-10"
  rate_limit:
    max_retries: 3
    retry_delay: 2

clickhouse:
  host: "${CLICKHOUSE_HOST}"
  port: 9000
  database: shopify
  user: default
  password: "${CLICKHOUSE_PASSWORD}"

kafka:
  bootstrap_servers: "${KAFKA_BOOTSTRAP_SERVERS}"
  consumer_group: shopify-datalake
  topics:
    - orders
    - products
    - customers
    - fulfillments
    - refunds

etl:
  batch_size: 1000
  workers: 4
  schedule:
    orders: "*/15 * * * *"  # Every 15 minutes
    products: "0 * * * *"    # Hourly
    customers: "0 */6 * * *" # Every 6 hours

dashboards:
  grafana:
    url: "${GRAFANA_URL}"
    api_key: "${GRAFANA_API_KEY}"
  superset:
    url: "${SUPERSET_URL}"
    api_key: "${SUPERSET_API_KEY}"
```

## 📈 Analytics Queries

### Daily Sales Summary

```sql
SELECT
    toDate(created_at) AS date,
    COUNT(*) AS order_count,
    SUM(total_price) AS total_revenue,
    AVG(total_price) AS avg_order_value,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM orders
WHERE created_at >= today() - INTERVAL 30 DAY
GROUP BY date
ORDER BY date DESC;
```

### Customer Cohort Analysis

```sql
WITH cohorts AS (
    SELECT
        customer_id,
        toDate(MIN(created_at)) AS cohort_date,
        toYYYYMM(MIN(created_at)) AS cohort_month
    FROM orders
    GROUP BY customer_id
),
orders_with_cohorts AS (
    SELECT
        o.customer_id,
        o.created_at,
        c.cohort_month,
        toYYYYMM(o.created_at) - c.cohort_month AS months_since_signup
    FROM orders o
    JOIN cohorts c ON o.customer_id = c.customer_id
)
SELECT
    cohort_month,
    COUNT(DISTINCT customer_id) AS customers,
    COUNTIf(months_since_signup = 0) AS month_0,
    COUNTIf(months_since_signup = 1) AS month_1,
    COUNTIf(months_since_signup = 2) AS month_2,
    COUNTIf(months_since_signup = 3) AS month_3
FROM orders_with_cohorts
GROUP BY cohort_month
ORDER BY cohort_month DESC;
```

### RFM Analysis

```sql
WITH rfm AS (
    SELECT
        customer_id,
        MAX(created_at) AS last_order_date,
        COUNT(*) AS frequency,
        SUM(total_price) AS monetary,
        toDays(today()) - toDays(MAX(created_at)) AS recency
    FROM orders
    WHERE created_at >= today() - INTERVAL 180 DAY
    GROUP BY customer_id
)
SELECT
    customer_id,
    CASE
        WHEN recency <= 30 THEN 'Champions'
        WHEN recency <= 60 THEN 'Loyal'
        WHEN recency <= 90 THEN 'Potential'
        ELSE 'At Risk'
    END AS segment,
    recency,
    frequency,
    monetary
FROM rfm
ORDER BY monetary DESC
LIMIT 100;
```

## 📊 Dashboards

### Grafana Dashboard JSON

Pre-built dashboard templates are available in `dashboards/grafana/`:

- **Sales Overview** — Revenue, orders, AOV trends
- **Customer Analytics** — Acquisition, retention, LTV
- **Product Performance** — Bestsellers, inventory
- **Marketing Attribution** — Source/medium analysis

### Superset Charts

Pre-built Superset charts in `dashboards/superset/`:

- **Revenue Trends** — Line chart with date range selector
- **Geographic Sales** — World map with sales by country
- **Customer Segments** — Pie chart of RFM segments
- **Funnel Analysis** — Conversion from visit to purchase

## 🧪 Testing

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run integration tests (requires Docker)
pytest tests/integration/ -v

# Test specific module
pytest tests/extract/test_shopify.py -v

# Test ClickHouse connection
python -c "from src.load.clickhouse import ClickHouseLoader; c = ClickHouseLoader(); print(c.health_check())"
```

## 📚 Documentation

- [Installation Guide](docs/installation.md)
- [Architecture Overview](docs/architecture.md)
- [ClickHouse Schema](docs/schema.md)
- [API Reference](docs/api.md)
- [Dashboard Setup](docs/dashboards.md)
- [Deployment](docs/deployment.md)
- [Troubleshooting](docs/troubleshooting.md)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/ShopifyDataLake.git`
3. **Create** a virtual environment: `python -m venv venv && source venv/bin/activate`
4. **Install** dependencies: `pip install -r requirements.txt`
5. **Create** a feature branch: `git checkout -b feature/amazing-analytics`
6. **Make** your changes and **test**: `pytest tests/`
7. **Commit** your changes: `git commit -m 'Add amazing analytics feature'`
8. **Push** to the branch: `git push origin feature/amazing-analytics`
9. **Open** a Pull Request

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

Copyright (c) 2024 moggan1337

## 🙏 Acknowledgments

- [ClickHouse](https://clickhouse.com) for the high-performance OLAP database
- [Apache Kafka](https://kafka.apache.org) for event streaming
- [Shopify](https://shopify.dev) for API access
- [Grafana](https://grafana.com) for visualization
- [Apache Superset](https://superset.apache.org) for BI dashboards

---

<p align="center">
  Built with ❤️ for data-driven Shopify merchants
</p>
