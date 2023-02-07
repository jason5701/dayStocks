from github import Github

def get_github_repo(access_token, repo_name):
  g = Github(access_token)
  return g.get_user().get_repo(repo_name)

def upload_github_issue(repo, title, body):
  repo.create_issue(title=title,body=body)

def get_github_issue(repo):
  issues = repo.get_issues()

  str_index = issues[0].body.find('report_idx=')

  last_report = ''
  last_report_index = -1
  if str_index > -1:
    last_report = issues[0].body[str_index:(str_index+17)]
    last_report_index = int(last_report[-6:])
    print(last_report_index)
  else:
    print('없음')
  
  return last_report_index