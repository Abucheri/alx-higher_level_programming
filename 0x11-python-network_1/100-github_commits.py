#!/usr/bin/python3
"""
Module: 100-github_commits
Lists 10 commits of a GitHub repository
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        response = requests.get(url)
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
