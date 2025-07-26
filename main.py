import sys
from crawl import get_html

def main():
    if (len(sys.argv) < 2):
        print("no website provided")
        exit(1)
    if (len(sys.argv) > 2):
        print("too many arguments provided")
        exit(1)
    BASE_URL = sys.argv[1]
    print(f"starting crawl of: {BASE_URL}")
    
    print(get_html(BASE_URL))


if __name__ == "__main__":
    main()
