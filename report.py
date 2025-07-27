def print_report(pages, base_url):
    print("=============================")
    print(f"REPORT for {base_url}")
    print("=============================")

    sorted_pages = sort_pages(pages)
    for url, count in sorted_pages:
        print(f"Found {count} internal links to {url}")


def sort_pages(pages):
    pages_list = list(pages.items())

    # Sort by amount (desc.) then page (alpha, asc.)
    pages_list.sort(key=lambda x: (-x[1], x[0]))

    return pages_list