# Task 6: Interactive Web Scraper (CLI Version)
# Student: Manjunath G K
# Date: 12/09/2025

import requests
from bs4 import BeautifulSoup

def scrape_headlines(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Get first 10 headlines (h1, h2, h3 tags)
        headlines = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])[:10]]

        if not headlines:
            print(" No headlines found on this website.")
        else:
            print(f"\nTop Headlines from {url}:\n")
            for i, headline in enumerate(headlines, 1):
                print(f"{i}. {headline}")

    except Exception as e:
        print(f" Error while fetching data: { e }")


def main():
    print("=====  Interactive Web Scraper =====")
    while True:
        url = input("\nEnter website URL (or type 'exit' to quit): ")
        if url.lower() == "exit":
            print(" Exiting Web Scraper. Goodbye!")
            break
        scrape_headlines(url)


if __name__ == "__main__":
    main()
