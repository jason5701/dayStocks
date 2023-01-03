from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
import time

import warnings
warnings.filterwarnings('ignore')

import chromedriver_autoinstaller

def extract_stock_report(url):
  path = chromedriver_autoinstaller.install()
  driver = webdriver.Chrome(path)
  driver.get(url)

  time.sleep(2)

  title_list = []
  url_list = []
  pdf_list = []
  writer_list=[]
  category_list=[]
  company_list=[]

  upload_contents = ''

  elements = driver.find_elements(By.CSS_SELECTOR, "#contents > div.table_style01 > table > tbody> tr")

  for element in elements:
    category = element.find_element(By.CSS_SELECTOR, "td:nth-child(2)").text
    title = element.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
    writer = element.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
    company = element.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
    url = element.find_element(By.CSS_SELECTOR, "td:nth-child(3) > a").get_attribute('href')

    category_list.append(category)
    title_list.append(title)
    writer_list.append(writer)
    company_list.append(company)
    url_list.append(url)

    content = f"- " + category +", " + "<a href={url}>" + title + "</a>" + ", " + writer + ", "+ company+ "<br/>\n"
    upload_contents += content

  df = pd.DataFrame({'category':category_list, 'title':title_list,'writer':writer_list,'company':company_list, 'url':url_list})
  df.to_csv("today_report.csv",encoding='utf-8')

  return upload_contents


# print(df)