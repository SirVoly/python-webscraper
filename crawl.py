from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


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