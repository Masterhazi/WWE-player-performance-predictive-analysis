import requests
from bs4 import BeautifulSoup
import pandas as pd

# URLs of the three pages
urls = [
    'https://www.cagematch.net/?id=8&nr=1&page=17&year=2024&s=0',
    'https://www.cagematch.net/?id=8&nr=1&page=17&year=2024&s=100',
    'https://www.cagematch.net/?id=8&nr=1&page=17&year=2024&s=200'
]

# List to store data
data = []

# User-Agent to avoid getting blocked
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

# Function to scrape data from each page
def scrape_page(url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', {'class': 'TBase'})  # Find the table
        if table:
            rows = table.find_all('tr')[1:]  # Skip the header row
            for row in rows:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols)
    else:
        print(f"Failed to fetch data from {url}")

# Scrape each page
for url in urls:
    scrape_page(url)

# Create a DataFrame and save it as a CSV
if data:
    df = pd.DataFrame(data, columns=['S.No', 'Name', 'Matches', 'Wins', '%wins', 'Losses', '%losses', 'Draws', '%draws'])
    df.to_csv('wwe_win_loss_records.csv', index=False)
    print("Data saved to 'wwe_win_loss_records.csv'")
else:
    print("No data scraped!")
