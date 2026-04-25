#!/usr/bin/env python3
"""
ShopifyDataLake CLI - ETL Pipeline to ClickHouse
"""

import argparse
import sys
from .pipeline import ShopifyDataPipeline

def main():
    parser = argparse.ArgumentParser(description='ShopifyDataLake - ETL to ClickHouse')
    parser.add_argument('--store', required=True, help='Shopify store domain')
    parser.add_argument('--token', required=True, help='Shopify access token')
    parser.add_argument('--clickhouse-host', default='localhost', help='ClickHouse host')
    parser.add_argument('--clickhouse-port', type=int, default=9000, help='ClickHouse port')
    parser.add_argument('--clickhouse-user', default='default', help='ClickHouse user')
    parser.add_argument('--clickhouse-password', default='', help='ClickHouse password')
    parser.add_argument('-- incremental', action='store_true', help='Incremental sync')
    parser.add_argument('-- full', action='store_true', help='Full sync')
    
    args = parser.parse_args()
    
    pipeline = ShopifyDataPipeline(
        store=args.store,
        access_token=args.token,
        clickhouse_host=args.clickhouse_host,
        clickhouse_port=args.clickhouse_port,
        clickhouse_user=args.clickhouse_user,
        clickhouse_password=args.clickhouse_password,
    )
    
    if args.incremental:
        print("Running incremental sync...")
        pipeline.run_incremental()
    elif args.full:
        print("Running full sync...")
        pipeline.run_full()
    else:
        print("Specify --incremental or --full")

if __name__ == '__main__':
    main()
