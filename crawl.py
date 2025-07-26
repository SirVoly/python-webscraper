from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests


def normalize_url(url : str) -> str :
	url = url.lower()
	parse_results = urlparse(url)

	if not parse_results:
		return url
	if not parse_results.netloc:
		return url
	if not parse_results.path:
		return url
	
	result_url = parse_results.hostname + parse_results.path

	if (result_url[-1] == '/'):
		result_url = result_url[:-1]

	return result_url

def get_urls_from_html(html, base_url):
	links = []

	soup = BeautifulSoup(html, 'html.parser')
	for link in soup.find_all('a'):
		if href := link.get("href"):
			try:
				absolute_url = urljoin(base_url, href)
				links.append(absolute_url)
			except Exception as e:
				print(f"{str(e)}: {href}")

	return links

def get_html(url):

	response = requests.get(url)

	response.headers['Content-Type']
	
	if response.status_code > 400:
		raise Exception(f"HTTP Error Code {response.status_code}")

	if "text/html" not in response.headers['Content-Type'] :
		raise Exception(f"HTTP Content-Type is not text/html, but instead {response.headers['Content-Type']}")

	return response.text