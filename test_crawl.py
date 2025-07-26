import unittest
from crawl import normalize_url

class TestCrawl(unittest.TestCase):
	def test_normalize_url(self):
		input_url = "https://blog.boot.dev/path"
		processed_url = normalize_url(input_url)
		expected_url = "blog.boot.dev/path"

		self.assertEqual(processed_url, expected_url)

if __name__ == "__main__":
    unittest.main()
