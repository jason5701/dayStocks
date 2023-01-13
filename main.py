from crawler import extract_stock_report
from github_utils import get_github_repo, upload_github_issue
import os
from datetime import datetime
from pytz import timezone

if __name__ == '__main__':
  access_token = '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'
  # access_token = os.environ['MY_GITHUB_TOKEN']
  repo_name = "dayStocks"

  seoul_timezone = timezone('Asia/Seoul')
  today = datetime.now(seoul_timezone)
  today_date = today.strftime('%Y-%m-%d')

  print(today_date)
  # url = f"http://hkconsensus.hankyung.com/apps.analysis/analysis.list?sdate={today_date}&edate={today_date}&now_page=1&search_value=&pagenum=20&search_text=&business_code="
  # print(url)
  upload_contents = extract_stock_report(today_date)

  title = f"{today_date} 정보 알림"

  repo = get_github_repo(access_token, repo_name)
  upload_github_issue(repo, title, upload_contents)
  print('Upload done')