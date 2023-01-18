from github import Github

def get_github_repo(access_token, repo_name):
  g = Github(access_token)
  return g.get_user().get_repo(repo_name)

def upload_github_issue(repo, title, body):
<<<<<<< HEAD
  repo.create_issue(title=title,body=body)
=======
  repo.create_issue(title=title,body=body)
>>>>>>> f43098b0880c8b53cab2a1a799d2a7f75cc772ba
