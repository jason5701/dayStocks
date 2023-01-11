import os
from github import Github
from datetime import datetime
from pytz import timezone

if __name__=='__main__':
  access_token = os.environ['MY_GITHUB_TOKEN']

  seoul_timezone = timezone('Asia/Seoul')
  today = datetime.now(seoul_timezone)
  today_format = today.strftime('%Y-%m-%d')

  title = f'깃 이슈 테스트 제목{today_format}'
  body = '깃 이슈 테스트 내용입니다'

  repo_name = "dayStocks"

  g = Github(access_token)
  
  repo = g.get_user().get_repo(repo_name)
  repo.create_issue(title=title, body=body)
  print('issue test done')