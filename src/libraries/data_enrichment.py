def clean_sales_data(sales_data):
    # Filter out sales that are missing product_id
    return [row for row in sales_data if row['product_id']]

def enrich_sales_data(sales_data, product_data):

    # Initialize an empty list to store the enriched sales data
    enriched_data = []

    for sale in sales_data:
        # Retrieve the product_id from the current sale
        product_id = sale.get('product_id')
        # If the product_id is present, retrieve the product information from the product_data dictionary
        product_info = product_data.get(product_id)
        
        # If the product_info is present, add the category to the sale
        if product_info:
            sale['category'] = product_info['category']
            enriched_data.append(sale)

    return enriched_data