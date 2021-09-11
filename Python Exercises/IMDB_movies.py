import requests
from bs4 import BeautifulSoup
imdburl = "https://www.imdb.com/chart/top/"
r = requests.get(imdburl)
soup = BeautifulSoup(r.content,"html.parser")
gelenveri = soup.find_all("table",{"class":"chart full-width"})

tablo = (gelenveri[0].contents)[len(gelenveri[0].contents)-2]

tablo = tablo.find_all("tr")
for film in tablo:
    filmisimleri = film.find_all("td",{"class":"titleColumn"})
    filmadi = filmisimleri[0].text
    filmadi = filmadi.replace("\n","")
    print(filmadi)
