import requests
from PyPDF2 import PdfReader
from bs4 import BeautifulSoup

class DataScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def extract_text_from_pdf(self, pdf_path):
        """
        Extract text from a PDF file using PyPDF2.
        """
        try:
            reader = PdfReader(pdf_path)
            text = "".join([page.extract_text() for page in reader.pages])
            return text
        except Exception as e:
            print(f"Error reading PDF: {e}")
            return ""

    def scrape_news(self, query):
        """
        Scrape news articles related to a query using Google News RSS feed.
        """
        try:
            url = f"https://news.google.com/rss/search?q={query}"
            response = requests.get(url, headers=self.headers)
            soup = BeautifulSoup(response.content, "xml")
            articles = [
                {"title": item.title.text, "link": item.link.text}
                for item in soup.find_all("item")
            ]
            return articles
        except Exception as e:
            print(f"Error scraping news for query '{query}': {e}")
            return []

    def fetch_stock_price(self, ticker):
        """
        Fetch stock price data for a given ticker using Yahoo Finance API.
        """
        try:
            url = f"https://finance.yahoo.com/quote/{ticker}"
            response = requests.get(url, headers=self.headers)
            # Parsing logic for stock price can be added here
            return {"ticker": ticker, "price": "MockPrice"}
        except Exception as e:
            print(f"Error fetching stock price for {ticker}: {e}")
            return {}

