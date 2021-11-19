import requests
from bs4 import BeautifulSoup
import pandas as pd

dfPlayers = pd.read_csv('NBA_Players.csv')
url = 'https://www.rotowire.com/basketball/nba-lineups.php'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup)
#print(results)
##First approach
Teams = soup.find_all('div', {'class': 'lineup__abbr'})
Teams = [t.text.strip() for t in Teams]
print(Teams)
Player = soup.find_all('li',{'class': 'lineup__player is-pct-play-100'})

Player = [p.text.strip() for p in Player]
Player = [p.replace('\n', ' ') for p in Player]
Player = [p.replace('PG ', '') for p in Player]
Player = [p.replace('SG ', '') for p in Player]
Player = [p.replace('SF ', '') for p in Player]
Player = [p.replace('PF ', '') for p in Player]
Player = [p.replace('C ','') for p in Player]
df = pd.DataFrame(Player, columns=['Name'])
df['Starter'] = .3
df = pd.merge(df, dfPlayers, how='left', left_on=['Name'], right_on = ['Rotowire'])

df.to_csv('Starters.csv')
print(Player)



