# %%
#Mitre Crawler
#CVE Details Crawler
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
url = 'https://www.cvedetails.com/vulnerability-list/'

#initial Request
first_page = requests.get(url).text
#Parse initial Page
soup = BeautifulSoup(first_page, 'html.parser')


# %%
#How many vulnerabilities are on cvedetails.com?
vulnerabilities = soup.select('div[class="paging"]')[1].select('b')[0].getText()
print('There are',vulnerabilities,'known vulnerabilities on cvedetails.com')

# %%
#How many pages are on cvedetails.com?
pages = len(soup.select('div[class="paging"]')[1].select('a'))
print('There are',pages,'pages on cvedetails.com')
#Compile Link List
link_list = []
base_url = '/'.join(url.split('/')[0:3])
for url in soup.select('div[class="paging"]')[1].select('a'):
    link_list.append(base_url+url['href'])

# %%
#print CVE Infos
def obtain_cve_info(url):
    #Perform HTTP Request
    html = requests.get(url).text
    #Parse html
    soup = BeautifulSoup(html, 'html.parser')
    #Locate Table
    table = soup.select('table[class="searchresults sortable"]')
    #What headers exist?
    headers = []
    for header in table[0].findAll('th')[1:]:
        headertext = header.get_text().strip()
        headers.append(headertext)
    headers.append('Description')
    #Get Data Elements
    i = 0
    cve_elements = []
    for cve in table[0].select('tr[class="srrowns"]'):
        cve_element = {}
        subid = 0
        for subelement in cve.select('td')[1:]:
            cve_element[headers[subid]] = subelement.get_text().strip()
            subid += 1
        cve_element[headers[subid]] = table[0].select('td[class="cvesummarylong"]')[i].get_text().strip()
        i += 1
        cve_elements.append(cve_element)
    return (cve_elements)


# %%
cve_list = []
for link in tqdm(link_list):
    cve_list.extend(obtain_cve_info(link))

# %%
df = pd.DataFrame(cve_list)
#save as csv
df.to_csv('cves.csv')