from asyncio import Lock, Semaphore, create_task, gather
from aiohttp import ClientSession, ClientResponse
from crawl import normalize_url, get_urls_from_html
from urllib.parse import urlparse

class AsyncCrawler():
	def __init__(self, base_url, max_concurrency, max_pages):
		self.base_url = base_url
		self.base_domain = urlparse(base_url).netloc
		self.pages = {}
		self.lock = Lock()
		self.max_concurrency = max_concurrency
		self.semaphore = Semaphore(self.max_concurrency)
		self.session  : ClientSession = None
		self.max_pages : int = max_pages

	async def __aenter__(self):
		self.session = ClientSession()
		return self

	async def __aexit__(self, exc_type, exc_val, exc_tb):
		await self.session.close()

	async def add_page_visit(self, normalized_url):
		async with self.lock:
			if (normalized_url not in self.pages):
				self.pages[normalized_url] = 1
				return True
			else:
				self.pages[normalized_url] += 1
				return False
			
	async def get_html(self, url):
		async with self.session.get(url) as response:
			if response.status > 399:
				print(f"Error: HTTP {response.status} for {url}")
				return None

			if "text/html" not in response.content_type :
				print(f"Error: Non-HTML content {response.content_type} for {url}")
				return None

			return await response.text()
	
	async def crawl_page(self, current_url=None):
		current_url_obj = urlparse(current_url)
		if current_url_obj.netloc != self.base_domain:
			return
		
		async with self.lock:
			if len(self.pages) >= self.max_pages:
				return
		
		norm_current_url = normalize_url(current_url)

		first_visit = await self.add_page_visit(norm_current_url)

		if not first_visit:
			return
		
		async with self.semaphore:
			print(f"continueing crawl to: {current_url}... (Active: {self.max_concurrency - self.semaphore._value})")

			html = await self.get_html(current_url)
			if html is None:
				return
			
			next_urls = get_urls_from_html(html, self.base_url)
			
		background_tasks = []

		for url in next_urls:
			background_tasks.append(create_task(self.crawl_page(url)))
		
		if background_tasks:
			await gather(*background_tasks)

	async def crawl(self):
		await self.crawl_page(self.base_url)
		return self.pages

async def crawl_site_async(base_url, max_concurrency, max_pages):
	async with AsyncCrawler(base_url, max_concurrency, max_pages) as crawler:
		return await crawler.crawl()