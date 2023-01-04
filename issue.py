import os
from github import Github

if __name__=='__main__':
  access_token = os.environ['MY_GITHUB_TOKEN']
  title = '깃 이슈 테스트 제목'
  body = '깃 이슈 테스트 내용입니다'

  repo_name = "dayStocks"

  g = Github(access_token)
  
  repo = g.get_user().get_repo(repo_name)
  repo.create_issue(title=title, body=body)
  print('issue test done')