from bs4 import BeautifulSoup
import re

with open('top-50-universities-in-usa/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

# Find the full list table
# It's the second table in the article body
tables = soup.find_all('table')
if len(tables) > 1:
    top50_table = tables[1]
    rows = top50_table.find('tbody').find_all('tr')
    print(f"Number of schools in the Top 50 table: {len(rows)}")
    
    # Check the last row
    last_row = rows[-1]
    cols = last_row.find_all('td')
    print(f"Last row rank: {cols[0].text.strip()}, School: {cols[1].text.strip()}")
    
    ranks = [r.find_all('td')[0].text.strip() for r in rows]
    print(f"Last 10 ranks: {ranks[-10:]}")
else:
    print("Could not find table")
