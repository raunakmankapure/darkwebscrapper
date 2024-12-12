# Dark Web Scraper

## Description
This project is a Python-based ethical dark web scraper designed for cybersecurity research. It leverages the Tor network for anonymity and automates data extraction from `.onion` websites.

## Features
- Routes traffic through the Tor network using a SOCKS5 proxy.
- Scrapes content like links and text from publicly accessible dark web pages.
- Implements IP rotation with the Stem library for anonymity.

## Technologies Used
- Python
- Tor network
- `requests`
- `BeautifulSoup`
- `stem`

## Usage
1. Install Tor and start the service.
2. Install Python dependencies:
   ```bash
   pip install requests[socks] stem beautifulsoup4
