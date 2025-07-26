import unittest
from crawl import normalize_url, get_urls_from_html

class TestCrawl(unittest.TestCase):
	# normalize_url tests

	def test_remove_https(self):
		self.assertEqual(
			normalize_url("https://blog.boot.dev/path"),
			"blog.boot.dev/path"
		)

	def test_remove_http(self):
		self.assertEqual(
			normalize_url("http://blog.boot.dev/path"),
			"blog.boot.dev/path"
		)

	def test_remove_trailing_slash(self):
		self.assertEqual(
			normalize_url("https://blog.boot.dev/path/"),
			"blog.boot.dev/path"
		)

	def test_no_trailing_slash(self):
		self.assertEqual(
			normalize_url("https://blog.boot.dev/path"),
			"blog.boot.dev/path"
		)

	def test_already_normalized(self):
		self.assertEqual(
			normalize_url("blog.boot.dev/path"),
			"blog.boot.dev/path"
		)

	def test_https_in_path(self):
		self.assertEqual(
			normalize_url("https://en.wikipedia.org/wiki/HTTPS"),
			"en.wikipedia.org/wiki/https"
		)

	def test_http_in_path(self):
		self.assertEqual(
			normalize_url("https://en.wikipedia.org/wiki/HTTP"),
			"en.wikipedia.org/wiki/http"
		)

	def test_empty_string(self):
		self.assertEqual(
			normalize_url(""),
			""
		)
	
	def test_upper_case_url(self):
		self.assertEqual(
			normalize_url("https://blog.BOOT.dev/PATH"),
			"blog.boot.dev/path"
		)
	
	# get_urls_from_html tests

	def test_get_urls_from_html_basic(self):
		self.assertEqual(
			get_urls_from_html(
				'<html><body><a href="https://blog.boot.dev"><span>Boot.dev</span></a></body></html>',
				"https://blog.boot.dev"
			),
			["https://blog.boot.dev"]
		)
	
	def test_get_urls_from_html_multiple(self):
		self.assertEqual(
			get_urls_from_html(
				'<html><body><a href="https://blog.boot.dev"><span>Boot.dev</span></a><a href="https://www.google.com"><span>Boot.dev</span></a><a href="https://www.wikipedia.org"><span>Boot.dev</span></a></body></html>',
				"https://blog.boot.dev"
			),
			["https://blog.boot.dev", "https://www.google.com", "https://www.wikipedia.org"]
		)
	
	def test_get_urls_from_html_none(self):
		self.assertEqual(
			get_urls_from_html(
				'<html><body><span>Boot.dev></span></body></html>',
				"https://blog.boot.dev"
			),
			[]
		)
	
	def test_get_urls_from_html_relative(self):
		self.assertEqual(
			get_urls_from_html(
				'<html><body><a href="/courses"><span>Boot.dev</span></a></body></html>',
				"https://blog.boot.dev"
			),
			["https://blog.boot.dev/courses"]
		)

if __name__ == "__main__":
    unittest.main()
