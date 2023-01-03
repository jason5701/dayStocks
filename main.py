from crawler import extract_stock_report
from github_utils import get_github_repo, upload_github_issue
import os
from datetime import datetime
from pytz import timezone

if __name__ == '__main__':
  access_token = os.environ['MY_GITHUB_TOKEN']
  repo_name = "dayStocks"

  seoul_timezone = timezone('Asia/Seoul')
  today = datetime.now(seoul_timezone)
  today_date = today.strftime('%Y년 %m월 %d일')

  url = "http://hkconsensus.hankyung.com/apps.analysis/analysis.list?sdate=2023-01-03&edate=2023-01-03&now_page=1&search_value=&pagenum=20&search_text=&business_code="
  upload_contents = extract_stock_report(url)

  title = f"{today_date} 정보 알림"

  repo = get_github_repo(access_token, repo_name)
  upload_github_issue(repo, title, upload_contents)
  print('Upload done')