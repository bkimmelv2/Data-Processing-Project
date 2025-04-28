import unittest
from unittest.mock import mock_open, patch
from libraries import data_ingestion

class TestDataIngestion(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='''date,quantity,sale_amount,product_id
2023-03-01,2,40.00,P001
03/04/2023,2,50.00,P002
    ''')
    def test_read_sales_data(self, mock_file):
        filepath = 'dummy.csv'
        sales_data = data_ingestion.read_sales_data(filepath)
        expected_data = [
            {'date': '2023-03-01', 'quantity': 2, 'sale_amount': 40.0, 'product_id': 'P001'},
            {'date': '2023-03-04', 'quantity': 2, 'sale_amount': 50.0, 'product_id': 'P002'}
        ]
        self.assertEqual(sales_data, expected_data)

    @patch('builtins.open', new_callable=mock_open, read_data='''[
        {"product_id": "P001", "category": "Gadgets"},
        {"product_id": "P002", "category": "Tools"}
    ]''')
    def test_read_product_data(self, mock_file):
        filepath = 'dummy.json'
        product_data = data_ingestion.read_product_data(filepath)
        expected_data = {
            'P001': {"product_id": "P001", "category": "Gadgets"},
            'P002': {"product_id": "P002", "category": "Tools"}
            }
        self.assertEqual(product_data, expected_data)

if __name__ == '__main__':
    unittest.main()