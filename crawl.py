from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import requests


def normalize_url(url : str) -> str :
    parsed_url = urlparse(url)
    full_path = f"{parsed_url.netloc}{parsed_url.path}"
    full_path = full_path.rstrip("/")
    return full_path.lower()

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

	try:
		response = requests.get(url)
	except Exception as e:
		raise Exception(f"Network error while fetching {url}: {e}")

	response.headers['Content-Type']
	
	if response.status_code > 400:
		raise Exception(f"HTTP Error Code {response.status_code}: {response.reason}")

	if "text/html" not in response.headers['Content-Type'] :
		raise Exception(f"HTTP Content-Type is not text/html, but instead {response.headers['Content-Type']}")

	return response.text

def crawl_page(base_url, current_url=None, pages=None):
	if not current_url.startswith(base_url):
		return
	
	norm_current_url = normalize_url(current_url)

	if norm_current_url in pages:
		pages[norm_current_url] += 1
		return
	else:
		pages[norm_current_url] = 1
	
	print(f"continueing crawl to: {current_url}...")
	try:
		html = get_html(current_url)
		next_urls = get_urls_from_html(html, base_url)
	except Exception as e:
		if str(e).startswith("HTTP Content-Type"):
			# Ignore non HTML pages
			return
		raise Exception(f"Error crawling through {current_url}: {str(e)}")
	
	for url in next_urls:
		crawl_page(base_url, url, pages)