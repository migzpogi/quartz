import unittest
from lib.scrape import scrape_stub

class TestLibScrape(unittest.TestCase):

    def test_scrape_stub(self):
        self.assertEqual(scrape_stub(), 1)


if __name__ == '__main__':
    unittest.main()