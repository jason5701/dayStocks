from github import Github

def get_github_repo(access_token, repo_name):
  git = Github(access_token)
  return git.get_user().get_repo(repo_name)

def upload_github_issue(repo, title, body):
  repo.create_issue(title=title,body=body)