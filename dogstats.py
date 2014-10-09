from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.akc.org/reg/dogreg_stats.cfm"
r=requests.get(url)
data= r.text
soup = BeautifulSoup(data)	
	
table = soup.find_all('table')[1] 
rows = table.find_all('tr')
dogData= 0
for tr in rows:
    cols = tr.find_all('td')
	dogName =cols[0].get_text()
	ranking2013 = cols[1].get_text()
	ranking2012 =cols[2].get_text()
	ranking2008 =cols[3].get_text()
	ranking2003 =cols[4].get_text()
	dogData = pd.DataFrame(dogName,ranking2013,ranking2013,ranking2008,ranking2003)
	dogDataCsv = dogData.to_csv("AKC Dog Registrations Stats")#turns the dataFrame into a csv
