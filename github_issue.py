import os

from github import Github

GITHUB_API = "https://api.github.com"


class GithubIssue:
    def __init__(self):
        self.token = os.getenv("github_token", "token")
        self.repo = os.getenv("github_repo", "repo")

    def create(self, title, body, label):
        git = Github(base_url=GITHUB_API, login_or_token=self.token)
        repo = git.get_repo(self.repo)
        url = repo.create_issue(title=title, body=body, labels=[label])
        return self.issue_url(url.number)

    def issue_url(self, number):
        return f"https://github.com/{self.repo}/issues/{number}"
