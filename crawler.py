from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
import time

import warnings
warnings.filterwarnings('ignore')

import chromedriver_autoinstaller

path = chromedriver_autoinstaller.install()
driver = webdriver.Chrome(path)
driver.get("http://hkconsensus.hankyung.com/apps.analysis/analysis.list?sdate=2023-01-03&edate=2023-01-03&now_page=1&search_value=&pagenum=20&search_text=&business_code=")

time.sleep(2)

title_list = []
url_list = []
pdf_list = []
writer_list=[]
category_list=[]
company_list=[]

elements = driver.find_elements(By.CSS_SELECTOR, "#contents > div.table_style01 > table > tbody> tr")

for element in elements:
  category_list.append(element.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text)
  title_list.append(element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text)
  writer_list.append(element.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text)
  company_list.append(element.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text)
  url_list.append(element.find_element(By.CSS_SELECTOR, "td:nth-child(3) > a").get_attribute('href'))

df = pd.DataFrame({'category':category_list, 'title':title_list,'writer':writer_list,'company':company_list, 'url':url_list})
df.to_csv("today_report.csv",encoding='utf-8')

# print(df)