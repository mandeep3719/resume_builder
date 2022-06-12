import requests
from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time
import pandas as pd

url = "https://www.naukri.com/finanacial-ananlyst-jobs-in-mumbai?k=finanacial%20ananlyst&l=mumbai"
url1 = "https://www.naukri.com/financial-analyst-jobs-in-mumbai?k=financial%20analyst&l=mumbai"

page = requests.get(url)
print(page.text)
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

time.sleep(3)

soup = BeautifulSoup(driver.pages_source,'html5lib')

print(soup.prettify())

driver.close()



results = soups.find(class_='list_jobs')
print(results)

job_elems = results.find('articles',class_='jobsTuple ')

for job_elem in job_elems:
    URL = job_ele.find('a',class_='titling').get('href')
    print(URL)

    Title = job_ele.find('a',class_="titling")
    print(Title.text)
    rating_span = job.find('span',class_='Rating dot')
    if rating_span is None:
        continue
    else:
        Ratings = rating_span.text
        print(Ratings)

    Review_span = job_ele.find('a',class_="revCount")
    if Review_span is None:
        continue
    else:
        Reviews = Review_span.text
    print(Reviews)
    print(""*2)

 

