import csv

with open('data/sales_data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('data/cleaned_sales_data.csv', 'w', newline='') as new_file:
        fieldnames = ['date', 'transaction_id', 'product_id', 'quantity', 'sale_amount']

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for row in csv_reader:
            csv_writer.writerow(row)