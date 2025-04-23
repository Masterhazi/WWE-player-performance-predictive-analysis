import re
from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open('royal_rumble_raw.html', 'r', encoding='utf-8') as file:
    html = file.read()

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')
data = []

# Extract Event Name
event_name = re.search(r'<h1>\s*(.*?)\s*</h1>', html).group(1)

# Extract matches
matches = soup.find_all('div', class_='match-wrestlers')

for match in matches:
    # Match name
    match_name = match.find_previous('div', class_='match-header').find('h3').text.strip()

    # Winner
    winner = re.search(r'<div class="winning-side.*?<span class="wrestler-name">(.*?)</span>', str(match))
    winner = winner.group(1) if winner else 'N/A'
    
    # Loser
    loser = re.search(r'<div class="losing-side.*?<span class="wrestler-name">(.*?)</span>', str(match))
    loser = loser.group(1) if loser else 'N/A'

    # Title Match
    title_match = 'Yes' if re.search(r'<span class="champion">C</span>', str(match)) else 'No'

    # Add to data
    data.append([event_name, match_name, winner, loser, title_match])

# Royal Rumble Special Case
rumble_rows = soup.find_all('tr', class_='wrestlers-row multiple')
for row in rumble_rows:
    loser = re.search(r'<span class="wrestler-name">(.*?)</span>', str(row)).group(1)
    eliminated_by = re.search(r'by (.*?)</span>', str(row))
    eliminated_by = eliminated_by.group(1) if eliminated_by else 'N/A'
    data.append([event_name, 'Royal Rumble', eliminated_by, loser, 'No'])

# Save to CSV
df = pd.DataFrame(data, columns=['Event Name', 'Match', 'Winner', 'Loser', 'Title Match'])
df.to_csv('wwe_matches.csv', index=False)

print("Data saved to 'wwe_matches.csv'")
