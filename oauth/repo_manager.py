#!/usr/bin/env python3
"""GitHub Client - OAUth and API study | Alta3 Research"""

import json
import requests

MY_USERNAME = "nayan-mistry"

def create_repo(repo_name: str, token: str) -> str:
    """
    This will create a repo for your GitHub account.
    """
    repo_data = {"name": repo_name}
    json_data = json.dumps(repo_data)
    headers = {"Authorization": f"token {token}"}
    result = requests.post(f"https://api.github.com/user/repos",data=json_data, headers=headers)
    response_code = result.status_code
    response = result.text
    print(response_code, response)
    return response

def show_repos(username: str, token: str) -> list:
    """
    This will list out all of the repos associated with your GitHub account.
    """
    url = f"https://api.github.com/users/{username}/repos"
    headers = headers = {"Authorization": f"token {token}"}
    result = requests.get(url, headers=headers)
    resp_headers = result.headers
    print(f"""Rate - \n            Limit: {resp_headers['X-RateLimit-Limit']}
            Used: {resp_headers['X-RateLimit-Used']}
            Remaining: {resp_headers['X-RateLimit-Remaining']}""")
    repos = list(result.json())
    for repo in repos:
        print(repo['name'])
    return repos

def get_token() -> str:
    # Read token in from file
    with open("/home/student/mycode/secrets/token") as f:
        token = f.read().rstrip("\n")
        return token

if __name__ == "__main__":
    tkn = get_token()
    show_repos(MY_USERNAME, tkn)
    create_repo("learning_oauth", tkn)