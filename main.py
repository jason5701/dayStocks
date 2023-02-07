from crawler import extract_stock_report
from datetime import datetime, timedelta
from pytz import timezone
import os
from send import telegram
from github_utils import get_github_issue, get_github_repo, upload_github_issue

if __name__ == '__main__':
  access_token = os.environ['MY_GITHUB_TOKEN']
  repo_name = "dayStocks"

  repo = get_github_repo(access_token, repo_name)
  last_issue = get_github_issue(repo)

  seoul_timezone = timezone('Asia/Seoul')
  today = datetime.now(seoul_timezone)
  today_date = today.strftime('%Y-%m-%d')
  before_week = datetime.now(seoul_timezone) - timedelta(weeks=1)
  before_week_date = before_week.strftime('%Y-%m-%d')

  dates = [before_week_date, today_date]

  upload_contents, telegram_contents = extract_stock_report(dates, last_issue)

  title = f"{today_date} 정보알림"

  if not upload_contents:
    print('there is no data')
  else:
    upload_github_issue(repo, title, upload_contents)
    telegram(telegram_contents)
    print('Upload done')

