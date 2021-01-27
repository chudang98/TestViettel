import unittest

import crawlData

DELTA_DAY_TIME = 50
CV_URL = 'https://airtable.com/shr7Q4iNWosrNgxoH/tblHrgb8n4fNAHI4Q'


class TestCrawlCV(unittest.TestCase):
    
    def test_crawl_data(self):
        self.assertEqual(len(crawlData.crawl_data_cv(CV_URL)), 13)

if __name__ == '__main__':
    unittest.main()