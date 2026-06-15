import pandas as pd

from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/enterprise_ai"
engine = create_engine(DATABASE_URL)

df = pd.read_csv(
    "data/Global_Superstore2.csv",
    encoding="latin1"
)

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nCreating Customers DataFrame...")
customers_df = (
    df[
        [
            "Customer ID",
            "Customer Name",
            "Segment",
            "City",
            "State",
            "Country"
        ]
    ]
    .drop_duplicates(subset=["Customer ID"])
)

customers_df.columns = [
    "customer_id",
    "customer_name",
    "segment",
    "city",
    "state",
    "country"
]

print(f"Customers: {customers_df.shape}")
print(f"Unique customer IDs: {customers_df['customer_id'].nunique()}")

print("\nCreating Products DataFrame...")
products_df = (
    df[
        [
            "Product ID",
            "Category",
            "Sub-Category",
            "Product Name"
        ]
    ]
    .drop_duplicates(subset=["Product ID"])
)

products_df.columns = [
    "product_id",
    "category",
    "sub_category",
    "product_name"
]

print(f"Products: {products_df.shape}")
print(f"Unique product IDs: {products_df['product_id'].nunique()}")

print("\nCreating Orders DataFrame...")
orders_df = df[
    [
        "Order ID",
        "Customer ID",
        "Product ID",
        "Order Date",
        "Sales",
        "Profit",
        "Discount",
        "Quantity"
    ]
].copy()

orders_df.columns = [
    "order_id",
    "customer_id",
    "product_id",
    "order_date",
    "sales",
    "profit",
    "discount",
    "quantity"
]

orders_df["order_date"] = pd.to_datetime(orders_df["order_date"], dayfirst=True)

print(f"Orders: {orders_df.shape}")

print("\nCustomers Preview:")
print(customers_df.head())

print("\nProducts Preview:")
print(products_df.head())

print("\nOrders Preview:")
print(orders_df.head())

print("\nLoading data into PostgreSQL...")

customers_df.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

products_df.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

orders_df.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False,
    chunksize=1000
)

print("\nData loaded successfully.")
print(f"Customers inserted: {len(customers_df)}")
print(f"Products inserted: {len(products_df)}")
print(f"Orders inserted: {len(orders_df)}")