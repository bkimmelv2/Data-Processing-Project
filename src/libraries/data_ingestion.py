import csv
import json
from datetime import datetime

def read_sales_data(sales_filepath):

    # Initialize an empty list to store the sales data
    sales_data = []

    # Read the sales data from the CSV file
    with open(sales_filepath, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Retrieve the date from the current row
            date = row['date']

            # First try to parse the date as a YYYY-MM-DD format
            try:
                parsed_date = datetime.strptime(date, '%Y-%m-%d')
            # If that fails, try to parse it as a date in MM/DD/YYYY format
            except ValueError:
                parsed_date = datetime.strptime(date, '%m/%d/%Y')
            
            # Convert the date back into a string in YYYY-MM-DD format when storing the data back in the row
            row['date'] = parsed_date.strftime('%Y-%m-%d')
            
            # Convert quantity and sale_amount to appropriate data types
            row['quantity'] = int(row['quantity'])
            row['sale_amount'] = float(row['sale_amount'])
            
            sales_data.append(row)
    # print(sales_data)
    return sales_data

def read_product_data(product_filepath):
    # Read the product data from the JSON file
    with open(product_filepath) as file:
        # Load the JSON data into a Python dictionary
        product_data = json.load(file)
    
    # Create a dictionary indexed by product_id for easy lookup
    # print({product['product_id']: product for product in product_data})
    return {product['product_id']: product for product in product_data}

# read_sales_data('../data/sales_data.csv')
# read_product_data('../data/product_data.json')