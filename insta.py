from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests
import shutil

baseURL= 'https://www.instagram.com/explore/tags/'
plusURL= input("검색할 태그를 입력하세요. :")

url = baseURL + quote_plus(plusURL)


driver=webdriver.Chrome()
driver.get(url)

time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html,"html.parser")

imglist=[]

for i in range(0,20):
    insta= soup.select("._aabd._aa8k._aanf")
    for i in insta:
        print('https://www.instagram.com' + i.a['href'])
        imgURL=i.select_one('._aagv').img['src']
        imglist.append(imgURL)
        imglist=list(set(imglist))
        html = driver.page_source
        soup = BeautifulSoup(html,"html.parser")
        insta= soup.select("._aabd._aa8k._aanf")
   #     insta= soup.select("._aabd._aa8k._aanf")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
n=0
for i in range(0,200):
    try:
        image_url=imglist[n]
    except IndexError:
        print("over") 
    resp = requests.get(image_url,stream=True)
    localfile=open('./img3/' + plusURL + str(n) + '.jpg', 'wb')
    resp.raw.decode_content =True
    shutil.copyfileobj(resp.raw, localfile)
    n+=1
    del resp
    # with urlopen(imgURL) as f:
    #     with open('./img/' + plusURL + str(n) + '.jpg', 'wb') as h:
    #         img = f.read()
    #         h.write(img)
    # n+=1
    # print(imgURL)
    # print()
#="/p/CpurCGCJnQj/"

driver.close()