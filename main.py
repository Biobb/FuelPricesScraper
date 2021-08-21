import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://www.polttoaine.net/Jyva_skyla_"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
table = soup.find("table")
table_rows = table.find_all("tr")

data = []
for tr in table_rows:
    td = tr.find_all("td")
    row = [tr.text for tr in td]
    data.append(row)

df = pd.DataFrame(data, columns=['Jakeluasema', 'PVM', '95E10', '98E', 'Di'])
df = df.drop([0,1,2])
df = df.drop(columns=['95E10', '98E'])
df = df.sort_values(by=['PVM','Di'], ascending=[False,True])
print(df)
