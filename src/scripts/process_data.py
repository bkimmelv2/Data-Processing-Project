import csv
from libraries import data_ingestion
from libraries import data_enrichment

def generate_aggregated_report(sales_data):
    # Initialize an empty dictionary to store the report
    report = {}

    for sale in sales_data:
        # Retrieve the category from each sale
        category = sale['category']
        # If the category is not present in the report, add it with default values
        if category not in report:
            report[category] = {
                'total_sales': 0.0,
                'total_transactions': 0,
                'total_quantity': 0
            }
        # Add the sale_amount to the total_sales for the category
        report[category]['total_sales'] += sale['sale_amount']
        # Increment the total_transactions for the category
        report[category]['total_transactions'] += 1
        # Add the sale quantity to the total_quantity for the category
        report[category]['total_quantity'] += sale['quantity']
    
    # Calculate average transaction value for each category and add it to the report
    for category in report:
        r = report[category]
        r['average_transaction_value'] = r['total_sales'] / r['total_transactions']
    
    return report

def write_aggregated_report_to_csv(report, filepath):
    # Sort the categories in alphabetical order
    sorted_categories = sorted(report.keys())

    # Write the report to a CSV file
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['category', 'total_sales', 'total_transactions', 'average_transaction_value', 'total_quantity'])
        # Iterate over the sorted categories and write the report data to the CSV file
        for category in sorted_categories:
            r = report[category]
            writer.writerow([
                category,
                f"{r['total_sales']:.2f}",
                r['total_transactions'],
                f"{r['average_transaction_value']:.2f}",
                r['total_quantity']
            ])

if __name__ == '__main__':
    sales_file = '../data/sales_data.csv'
    product_file = '../data/product_data.json'

    # Retrieve the sales data, parse the dates, and adjust data types
    sales_data = data_ingestion.read_sales_data(sales_file)
    # Retrieve the product data and parse the product_id
    product_data = data_ingestion.read_product_data(product_file)
    
    # Clean the sales data from any missing product_id
    clean_sales = data_enrichment.clean_sales_data(sales_data)
    # Enrich the clean sales data with product category information
    enriched_sales = data_enrichment.enrich_sales_data(clean_sales, product_data)
    
    # Generate the report using the enriched sales data
    report = generate_aggregated_report(enriched_sales)
    # Write the report to a CSV file
    write_aggregated_report_to_csv(report, '../data/aggregated_report.csv')