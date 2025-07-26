# A Python Webcrawler

This project is a simple web crawler designed to fetch and parse HTML content from a given URL.

Building this project thought about the basics of HTTP requests and web scraping in Python. The implementation was done following the [Test Driven Development](https://en.wikipedia.org/wiki/Test-driven_development) strategy.

## Technologies Used

*   **Python 3**: The primary programming language.
*   **uv**: A next-generation Python package manager and installer.
*   [`beautifulsoup4`](https://pypi.org/project/beautifulsoup4/): A Python library for parsing HTML and XML documents.
*   [`aiohttp`](https://pypi.org/project/aiohttp/): An asynchronous HTTP client/server framework for Python.
*   [`requests`](https://pypi.org/project/requests/): A simple, yet elegant, HTTP library for Python.

## Setup

To run this project, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/SirVoly/python-webscraper.git
    cd python-webscraper
    ```
2.  **Create and activate a virtual environment**:
    ```bash
    uv venv
    source .venv/bin/activate
    ```
3.  **Install dependencies**:
    ```bash
    uv add beautifulsoup4==4.13.4
    uv add aiohttp==3.12.12
    uv add requests==2.32.4
    ```

## Usage

Once the setup is complete and your virtual environment is activated, you can run the main script using `uv`:

```bash
uv run main.py
```

# Credit
This project was completed as part of a guided course on [Boot.dev](https://www.boot.dev).
It was build following along with the [Build a Web Scraper in Python](https://www.boot.dev/courses/build-web-scraper-python) course.