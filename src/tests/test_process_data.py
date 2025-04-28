import unittest
from scripts.process_data import generate_aggregated_report

class TestProcessData(unittest.TestCase):

    def test_generate_aggregated_report(self):
        sales_data = [
            {'category': 'Gadgets', 'sale_amount': 45.0, 'quantity': 3},
            {'category': 'Tools', 'sale_amount': 50.0, 'quantity': 1},
            {'category': 'Gadgets', 'sale_amount': 75.0, 'quantity': 5}
        ]
        report = generate_aggregated_report(sales_data)
        expected_report = {
            'Gadgets': {
                'total_sales': 120.0,
                'total_transactions': 2,
                'total_quantity': 8,
                'average_transaction_value': 60.0
            },
            'Tools': {
                'total_sales': 50.0,
                'total_transactions': 1,
                'total_quantity': 1,
                'average_transaction_value': 50.0
            }
        }
        self.assertEqual(report, expected_report)

if __name__ == '__main__':
    unittest.main()