import sys
from async_crawler import crawl_site_async
from asyncio import run

async def main_async():
    if (len(sys.argv) < 2):
        print("no website provided")
        exit(1)
    if (len(sys.argv) > 2):
        print("too many arguments provided")
        exit(1)
    base_url = sys.argv[1]
    print(f"starting crawl of: {base_url}...")
    
    try:
        pages = {}
        await crawl_site_async(base_url)
        for p in pages:
            print(f"{p} is linked {pages[p]} times.")
    except Exception as e:
        print(f"Error crawling through webpage {base_url}: {str(e)}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    run(main_async())
