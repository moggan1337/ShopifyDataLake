# ShopifyDataLake

<p align="center">
  <img src="https://img.shields.io/badge/Shopify-Analytics-95BF47?style=for-the-badge&logo=shopify&logoColor=white" alt="Shopify">
  <img src="https://img.shields.io/badge/ClickHouse-FF6B6B?style=for-the-badge&logo=clickhouse&logoColor=white" alt="ClickHouse">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

> 📊 **Real-time ETL Pipeline** - Build a data warehouse from Shopify with ClickHouse, custom dashboards, cohort analysis, and advanced analytics.

## ✨ Features

### Data Pipeline
- ⚡ **Real-time Sync** - Webhook-based instant data updates
- 📥 **Historical Import** - Bulk import all historical data
- 🔄 **Incremental** - Delta syncs for efficiency
- 🗄️ **Data Lake** - Raw + processed data storage

### Analytics
- 📈 **Sales Analytics** - Revenue, orders, AOV, LTV
- 👥 **Customer Analytics** - Cohort analysis, churn, RFM
- 📦 **Product Analytics** - Bestsellers, margins, returns
- 🏪 **Vendor Analytics** - Per-vendor performance
- 🌐 **Marketing Analytics** - Attribution, campaigns

### Dashboards
- 📊 **Pre-built** - Ready-made dashboard templates
- 🎨 **Custom** - Build your own with drag-drop
- 📱 **Mobile** - Native iOS/Android apps
- 📧 **Reports** - Scheduled email reports

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                      ShopifyDataLake                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    Shopify Store                          │   │
│  │  Products, Orders, Customers, Fulfillments, Refunds       │   │
│  └──────────────────────────┬───────────────────────────────┘   │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    Ingestion Layer                             │ │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌─────────────┐ │ │
│  │  │ Webhooks  │ │  Admin    │ │  CSV      │ │   API       │ │ │
│  │  │ (Real-time)│ │  Import  │ │  Import  │ │  Polling    │ │ │
│  │  └───────────┘ └───────────┘ └───────────┘ └─────────────┘ │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    Processing Layer                           │ │
│  │  ┌──────────────────────────────────────────────────────┐   │ │
│  │  │ Apache Kafka / Redpanda                               │   │ │
│  │  │ - Order Events                                        │   │ │
│  │  │ - Customer Events                                     │   │ │
│  │  │ - Product Events                                      │   │ │
│  │  └──────────────────────────────────────────────────────┘   │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    Storage Layer                              │ │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌─────────────┐ │ │
│  │  │ ClickHouse│ │ PostgreSQL│ │  Redis    │ │  S3/MinIO  │ │ │
│  │  │ (Analytics)│ │(Metadata)│ │ (Cache)  │ │  (Blobs)   │ │ │
│  │  └───────────┘ └───────────┘ └───────────┘ └─────────────┘ │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                             │                                    │
│  ┌──────────────────────────┴──────────────────────────────────┐ │
│  │                    Query & Visualization                      │ │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌─────────────┐ │ │
│  │  │  Grafana  │ │  Superset │ │  Custom   │ │   API       │ │ │
│  │  │  Dashboards│ │  Charts  │ │   React   │ │   (FastAPI) │ │ │
│  │  └───────────┘ └───────────┘ └───────────┘ └─────────────┘ │ │
│  └──────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

## 📦 Installation

```bash
git clone https://github.com/moggan1337/ShopifyDataLake.git
cd ShopifyDataLake

# Start infrastructure
docker-compose up -d clickhouse kafka minio

# Install Python packages
pip install -r requirements.txt

# Run migrations
python scripts/init_db.py

# Start ETL pipeline
python -m etl.pipeline
```

## 📄 License

MIT License
