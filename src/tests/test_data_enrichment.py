import unittest
from libraries import data_enrichment

class TestDataEnrichment(unittest.TestCase):

    def test_clean_sales_data(self):
        sales_data = [{'product_id': 'P001'}, {'product_id': ''}]
        clean_data = data_enrichment.clean_sales_data(sales_data)
        expected_data = [{'product_id': 'P001'}]
        self.assertEqual(clean_data, expected_data)

    def test_enrich_sales_data(self):
        sales_data = [{'product_id': 'P001'}, {'product_id': 'P002'}]
        product_data = {'P001': {'category': 'Gadgets'}, 'P002': {'category': 'Tools'}}
        enriched_data = data_enrichment.enrich_sales_data(sales_data, product_data)
        expected_data = [{'product_id': 'P001', 'category': 'Gadgets'}, {'product_id': 'P002', 'category': 'Tools'}]
        self.assertEqual(enriched_data, expected_data)


if __name__ == '__main__':
    unittest.main()