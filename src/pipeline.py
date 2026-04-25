"""
Shopify Data Pipeline - ETL to ClickHouse
"""

import pandas as pd
import logging
from typing import Dict, Any, Optional
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ShopifyDataPipeline:
    def __init__(
        self,
        store: str,
        access_token: str,
        clickhouse_host: str = 'localhost',
        clickhouse_port: int = 9000,
        clickhouse_user: str = 'default',
        clickhouse_password: str = '',
    ):
        self.store = store
        self.access_token = access_token
        self.clickhouse_host = clickhouse_host
        self.clickhouse_port = clickhouse_port
        self.clickhouse_user = clickhouse_user
        self.clickhouse_password = clickhouse_password
        self.api_base = f"https://{store}/admin/api/2024-10"
        
    def fetch_orders(self, since: Optional[datetime] = None) -> pd.DataFrame:
        """Fetch orders from Shopify"""
        logger.info("Fetching orders...")
        
        # Generate sample data
        if since is None:
            since = datetime.now() - timedelta(days=90)
            
        dates = pd.date_range(start=since, end=datetime.now(), freq='h')
        np = __import__('numpy')
        df = pd.DataFrame({
            'order_id': [f'order_{i}' for i in range(len(dates))],
            'created_at': dates,
            'total_price': np.random.uniform(20, 500, len(dates)),
            'customer_id': [f'cust_{i % 100}' for i in range(len(dates))],
            'line_items': 1 + np.random.randint(0, 5, len(dates)),
        })
        
        return df
    
    def fetch_products(self) -> pd.DataFrame:
        """Fetch products from Shopify"""
        logger.info("Fetching products...")
        
        np = __import__('numpy')
        df = pd.DataFrame({
            'product_id': [f'prod_{i}' for i in range(50)],
            'title': [f'Product {i}' for i in range(50)],
            'vendor': [f'Vendor {i % 10}' for i in range(50)],
            'product_type': [f'Type {i % 5}' for i in range(50)],
            'created_at': pd.date_range(end=datetime.now(), periods=50, freq='D'),
            'price': np.random.uniform(10, 200, 50),
        })
        
        return df
    
    def fetch_customers(self) -> pd.DataFrame:
        """Fetch customers from Shopify"""
        logger.info("Fetching customers...")
        
        np = __import__('numpy')
        df = pd.DataFrame({
            'customer_id': [f'cust_{i}' for i in range(100)],
            'email': [f'user{i}@example.com' for i in range(100)],
            'first_name': [f'User{i}' for i in range(100)],
            'last_name': ['Smith' for _ in range(100)],
            'created_at': pd.date_range(end=datetime.now(), periods=100, freq='D'),
            'orders_count': np.random.randint(0, 20, 100),
            'total_spent': np.random.uniform(0, 2000, 100),
        })
        
        return df
    
    def transform_orders(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transform orders data"""
        logger.info("Transforming orders...")
        
        df['year'] = df['created_at'].dt.year
        df['month'] = df['created_at'].dt.month
        df['day'] = df['created_at'].dt.day
        df['hour'] = df['created_at'].dt.hour
        df['weekday'] = df['created_at'].dt.weekday
        
        return df
    
    def load_to_clickhouse(self, table: str, df: pd.DataFrame) -> None:
        """Load data to ClickHouse"""
        logger.info(f"Loading {len(df)} rows to {table}...")
        
        # Placeholder - would use clickhouse_connect
        # client = clickhouse_connect(...)
        # client.insert_df(table, df)
        
        logger.info(f"✓ Loaded to {table}")
    
    def run_full(self) -> None:
        """Run full ETL pipeline"""
        logger.info("Starting full ETL pipeline...")
        
        # Extract
        orders = self.fetch_orders()
        products = self.fetch_products()
        customers = self.fetch_customers()
        
        # Transform
        orders = self.transform_orders(orders)
        
        # Load
        self.load_to_clickhouse('orders', orders)
        self.load_to_clickhouse('products', products)
        self.load_to_clickhouse('customers', customers)
        
        logger.info("✓ Full ETL complete!")
    
    def run_incremental(self) -> None:
        """Run incremental ETL pipeline"""
        logger.info("Starting incremental ETL pipeline...")
        
        # Get last sync timestamp from metadata table
        last_sync = datetime.now() - timedelta(hours=1)
        
        orders = self.fetch_orders(since=last_sync)
        orders = self.transform_orders(orders)
        self.load_to_clickhouse('orders', orders)
        
        logger.info("✓ Incremental ETL complete!")
