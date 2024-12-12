import requests
from bs4 import BeautifulSoup
from stem import Signal
from stem.control import Controller

# TOR configuration
TOR_PROXY = "socks5h://127.0.0.1:9050"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Function to renew Tor identity
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="your_password_here")  # Set your Tor control password
        controller.signal(Signal.NEWNYM)
        print("IP address changed!")

# Function to fetch a dark web page
def fetch_dark_web_page(url):
    try:
        proxies = {"http": TOR_PROXY, "https": TOR_PROXY}
        response = requests.get(url, headers=HEADERS, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(f"Successfully fetched: {url}")
            return response.text
        else:
            print(f"Failed to fetch: {url}, Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return None

# Function to scrape content
def scrape_dark_web_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    # Example: Find all links
    links = soup.find_all("a")
    for link in links:
        href = link.get("href")
        if href:
            print(f"Found link: {href}")

# Main function
def main():
    # Example dark web URL (replace with a valid .onion URL)
    url = "http://exampledarkweb.onion"
    
    print("Renewing Tor IP...")
    renew_tor_ip()

    print("Fetching dark web page...")
    page_content = fetch_dark_web_page(url)

    if page_content:
        print("Scraping content...")
        scrape_dark_web_content(page_content)

if __name__ == "__main__":
    main()
