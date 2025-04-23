import requests

# URL to scrape
url = 'https://www.thesmackdownhotel.com/events-results/ppv-special/wwe-survivor-series-wargames-2024'

# User-Agent to avoid getting blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Scrape the page
response = requests.get(url, headers=headers)

if response.status_code == 200:
    with open('wwe_survivor.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("Raw HTML data saved to 'royal_rumble_raw.html'")
else:
    print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
