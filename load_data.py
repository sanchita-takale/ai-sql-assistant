import os
import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from sqlalchemy import create_engine

# ---------------------------------
# MYSQL CONNECTION
# ---------------------------------

engine = create_engine(
    "mysql+pymysql://root:root123@localhost/ai_sql_project"
)

# ---------------------------------
# KAGGLE AUTH
# ---------------------------------

api = KaggleApi()
api.authenticate()

# ---------------------------------
# DOWNLOAD DATASET
# ---------------------------------

dataset_name = "olistbr/brazilian-ecommerce"

download_path = "data"

os.makedirs(download_path, exist_ok=True)

print("Downloading dataset...")

api.dataset_download_files(
    dataset_name,
    path=download_path,
    unzip=True
)

print("Dataset downloaded!")

# ---------------------------------
# LOAD CUSTOMERS
# ---------------------------------

customers = pd.read_csv(
    "data/olist_customers_dataset.csv"
)

customers = customers[[
    "customer_id",
    "customer_city"
]]

customers.columns = [
    "customer_id",
    "location"
]

customers.to_sql(
    "customers",
    con=engine,
    if_exists="replace",
    index=False
)

print("Customers table loaded!")

# ---------------------------------
# LOAD ORDERS
# ---------------------------------

orders = pd.read_csv(
    "data/olist_orders_dataset.csv"
)

orders = orders[[
    "order_id",
    "customer_id",
    "order_purchase_timestamp"
]]

orders["total_amount"] = 0

orders.columns = [
    "order_id",
    "customer_id",
    "order_date",
    "total_amount"
]

orders.to_sql(
    "orders",
    con=engine,
    if_exists="replace",
    index=False
)

print("Orders table loaded!")

# ---------------------------------
# LOAD PRODUCTS
# ---------------------------------

products = pd.read_csv(
    "data/olist_products_dataset.csv"
)

products = products[[
    "product_id",
    "product_category_name"
]]

products.columns = [
    "product_id",
    "category"
]

products.to_sql(
    "products",
    con=engine,
    if_exists="replace",
    index=False
)

print("Products table loaded!")

# ---------------------------------
# LOAD ORDER ITEMS
# ---------------------------------

order_items = pd.read_csv(
    "data/olist_order_items_dataset.csv"
)

order_items = order_items[[
    "order_id",
    "product_id",
    "price"
]]

order_items["quantity"] = 1

order_items.columns = [
    "order_id",
    "product_id",
    "price",
    "quantity"
]

order_items.to_sql(
    "order_items",
    con=engine,
    if_exists="replace",
    index=False
)

print("Order items table loaded!")

print("Everything completed successfully!")