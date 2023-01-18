from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd
import time


# import chromedriver_autoinstaller

def extract_stock_report(date):
  options = webdriver.ChromeOptions()
  options.add_argument("start-maximized")
  options.add_argument("lang=ko_KR")
  options.add_argument('headless')
  options.add_argument('window-size=1920x1080')
  options.add_argument("disable-gpu")
  options.add_argument("--no-sandbox")

  # path = chromedriver_autoinstaller.install()
  driver = webdriver.Chrome('chromdriver', chrome_options=options)
  url = 'http://hkconsensus.hankyung.com/apps.analysis/analysis.list?sdate='+date+'&edate='+date+'&now_page=1&search_value=&pagenum=80&search_text=&business_code='
  print(date)
  print(url)
  driver.get(url)

  time.sleep(2)

  title_list = []
  url_list = []
  pdf_list = []
  writer_list=[]
  category_list=[]
  company_list=[]

  upload_contents = ''
  telegram_contetns=''

  elements = driver.find_elements(By.CSS_SELECTOR, "#contents > div.table_style01 > table > tbody> tr")

  for element in elements:
    isCheck = element.find_element(By.CSS_SELECTOR, 'td:nth-child(1)').text
    print(isCheck)
    if isCheck == date:
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

      # content = f"- {category}, <a href='{url}'>{title}</a>, {writer}, {company}<br/>\n"
      telegramContent=f"- {category}, [{title}]({url})', {writer}, {company}\n"
      
    else:
      # content = '없음'
      telegramContent = '없음'

    # upload_contents += content
    telegram_contetns += telegramContent

  df = pd.DataFrame({'category':category_list, 'title':title_list,'writer':writer_list,'company':company_list, 'url':url_list})
  df.to_csv("today_report.csv",encoding='utf-8')

  # telegram(telegram_contetns)
  return telegram_contetns


# print(df)