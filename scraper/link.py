from urllib.request import urlopen, urljoin
import re
import requests
from bs4 import BeautifulSoup
import os

catname = input("give us a name category: ")
urlname = input("Type the url: ")
pagenum = int(input("Give the number of page you want to be scraped: "))
path = str(os.getcwd())

try:
    os.mkdir(path + '/' + catname)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)


def download_page(url):
    return urlopen(url).read().decode('utf-8')

def extract_links(page):
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)

stri = urlname

links = []
txt = []


for a in range(1, pagenum+1):
    links.append(stri.replace('pi=1', 'pi=' + str(a)))

with open('link.txt', 'r') as f:
        notin = f.read()
        f.close()

for nes in links:
    urls = []
    target_url = nes
    page = download_page(target_url)
    links = extract_links(page)
    for link in links:
        urls.append(urljoin(target_url, link))
    

    list1 = notin.split('\n')

    news = [c for c in urls if 'www.isna.ir/news' in c and '95031711050' not in c]

    newsUrl = list(set(news) - set(list1))

    for link in newsUrl:
        txt.append(link)

itr = 0 
for aim in txt:
        url = aim
        resp = requests.get(url)
        #resp = urlopen(url)
        document = ''
        soup = BeautifulSoup(resp.text, 'html.parser')
        document = document + str(soup.find("h1",{"class":"first-title"}).text) + '\n'
        document = document + str(soup.find("p",{"class":"summary"}).text) + '\n'
        document = document + str(soup.find("p",{"class":""}).text) + '\n'

        for i in soup.find("p",{"class":""}).next_siblings:
                if str(type(i)) == "<class 'bs4.element.Tag'>":
                        document = document + str(i.text) + '\n'

        with open(str(str(path + '/' + catname + '/' + catname) + str(itr) + '.txt'), 'w') as f:
                f.write(document)
                itr += 1
                f.close()
