import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime, timedelta
import random

# Database name
db_name = 'ABHIRANG.db'

# Data generation sizes
num_users = 200
num_products = 500
num_orders = 200
num_commissions = 100
num_reviews = 300

# Generating users
usernames = [f'user_{i}' for i in range(1, num_users + 1)]
password_hashes = ['hashed_password'] * num_users  # Placeholder for hashed passwords
emails = [f'user_{i}@example.com' for i in range(1, num_users + 1)]  # Ensure uniqueness
phone_numbers = [f'555-010{i % 100}' for i in range(1, num_users + 1)]  # Modulo for unique phone numbers
user_types = ['artist' if i % 2 == 0 else 'buyer' for i in range(num_users)]  # Alternate artist and buyer

users_df = pd.DataFrame({
    'username': usernames,
    'password_hash': password_hashes,
    'email': emails,  # List of unique emails
    'phone_number': phone_numbers,
    'user_type': user_types
})

# Generating products
product_names = [f'Art Piece {i}' for i in range(1, num_products + 1)]
product_descriptions = [f'Description of Art Piece {i}' for i in range(1, num_products + 1)]
prices = [random.randint(100, 10000) for _ in range(num_products)]  # Price range
stock_quantities = [random.randint(1, 100) for _ in range(num_products)]  # Stock
categories = [random.randint(1, 5) for _ in range(num_products)]  # Assuming 5 categories
ratings = [round(random.uniform(1, 5), 1) for _ in range(num_products)]

# Make sure the artist_ids are valid by limiting to the actual number of artists
artist_ids = [random.choice([i for i in range(1, num_users + 1) if users_df['user_type'].iloc[i-1] == 'artist']) for _ in range(num_products)]

products_df = pd.DataFrame({
    'name': product_names,
    'description': product_descriptions,
    'price': prices,
    'stock_quantity': stock_quantities,
    'category_id': categories,
    'artist_id': artist_ids,
    'rating': ratings
})

# Generating orders
order_dates = [datetime.now() - timedelta(days=random.randint(1, 60)) for _ in range(num_orders)]
total_amounts = [random.randint(100, 5000) for _ in range(num_orders)]
order_statuses = ['completed', 'pending', 'shipped', 'canceled']
user_ids = [random.choice(range(1, num_users + 1)) for _ in range(num_orders)]

orders_df = pd.DataFrame({
    'user_id': user_ids,
    'order_date': order_dates,
    'total_amount': total_amounts,
    'order_status': [random.choice(order_statuses) for _ in range(num_orders)]
})

# Generating commissions
commission_descriptions = [f'Commission for user {random.choice(user_ids)}' for _ in range(num_commissions)]
agreed_prices = [random.randint(200, 5000) for _ in range(num_commissions)]
commission_statuses = ['pending', 'completed', 'canceled']
deadlines = [datetime.now() + timedelta(days=random.randint(1, 60)) for _ in range(num_commissions)]

commissions_df = pd.DataFrame({
    'user_id': [random.choice(user_ids) for _ in range(num_commissions)],
    'artist_id': [random.choice([i for i in range(1, num_users + 1) if users_df['user_type'].iloc[i-1] == 'artist']) for _ in range(num_commissions)],
    'description': commission_descriptions,
    'agreed_price': agreed_prices,
    'status': [random.choice(commission_statuses) for _ in range(num_commissions)],
    'deadline': deadlines
})

# Generating reviews
review_product_ids = [random.choice(range(1, num_products + 1)) for _ in range(num_reviews)]
review_user_ids = [random.choice(user_ids) for _ in range(num_reviews)]
review_ratings = [random.randint(1, 5) for _ in range(num_reviews)]
review_comments = [f'Review comment {i}' for i in range(1, num_reviews + 1)]
review_dates = [datetime.now() - timedelta(days=random.randint(1, 60)) for _ in range(num_reviews)]

reviews_df = pd.DataFrame({
    'product_id': review_product_ids,
    'user_id': review_user_ids,
    'rating': review_ratings,
    'comment': review_comments,
    'created_at': review_dates
})

# Saving data to CSV files
users_df.to_csv('users.csv', index=False)
products_df.to_csv('products.csv', index=False)
orders_df.to_csv('orders.csv', index=False)
commissions_df.to_csv('commissions.csv', index=False)
reviews_df.to_csv('reviews.csv', index=False)

# Connect to SQLite database
conn = sqlite3.connect(db_name)

# Load CSV files into DataFrames
users_df = pd.read_csv('users.csv')
products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')
commissions_df = pd.read_csv('commissions.csv')
reviews_df = pd.read_csv('reviews.csv')

# Insert data into tables
users_df.to_sql('user', conn, if_exists='append', index=False)
products_df.to_sql('product', conn, if_exists='append', index=False)
orders_df.to_sql('Order', conn, if_exists='append', index=False)
commissions_df.to_sql('Commission', conn, if_exists='append', index=False)
reviews_df.to_sql('Review', conn, if_exists='append', index=False)

# Commit changes and close the connection
conn.commit()
conn.close()

print("Data generated and imported successfully into ABHIRANG.db!")
