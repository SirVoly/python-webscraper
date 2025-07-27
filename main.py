import sys
from async_crawler import crawl_site_async
from asyncio import run

async def main_async():
    if (len(sys.argv) < 2):
        print("Usage: main.py <base_url> [max_concurrency] [max_pages]")
        exit(1)
    if (len(sys.argv) > 4):
        print("Usage: main.py <base_url> [max_concurrency] [max_pages]")
        exit(1)
        
    base_url = sys.argv[1]
    if (len(sys.argv) >= 3):
        max_concurrency = int(sys.argv[2])
    else:
        max_concurrency = 1
    if (len(sys.argv) == 4):
        max_pages = int(sys.argv[3])
    else:
        max_pages = 10
    
    print(f"starting crawl of: {base_url}...")
    
    try:
        pages = await crawl_site_async(base_url, max_concurrency, max_pages)
        for p in pages:
            print(f"{p} is linked {pages[p]} times.")
    except Exception as e:
        print(f"Error crawling through webpage {base_url}: {str(e)}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    run(main_async())
