#! /usr/bin/env python3

import argparse

from perceval.backends.core.gitlab import (GitLab,
                                           CATEGORY_ISSUE,
                                           CATEGORY_MERGE_REQUEST)
import datetime
import dateutil
import json

# Optional API token argument
parser = argparse.ArgumentParser(
    description="Simple parser for GitHub issues and pull requests"
)
parser.add_argument("-t", "--token",
                    '--nargs', nargs='?',
                    help="GitLab token")

# Positional repository argument
parser.add_argument("repository",
                    help="GitLab repository, as 'owner/repo'")

args = parser.parse_args()

(owner, repository) = args.repository.split('/')

gitlab = GitLab(owner=owner, repository=repository, api_token=args.token, sleep_for_rate=True)

# Printing Owner and Repository
print("Owner: ", owner)
print("Repository: ", repository)
print("Categories: ", GitLab.CATEGORIES)

# Date from which data is to be fetched
from_date = datetime.datetime(2020, 3, 10, 0, 0, 0, tzinfo=dateutil.tz.tzutc())

# Fetch Issue data
issue_list_generator = gitlab.fetch(category=CATEGORY_ISSUE, from_date=from_date)
issue_list = list(issue_list_generator)

with open("gitlab_issue.json", "w") as file:
    for issues in issue_list:
        json.dump(issues, file)

issue = issue_list[0]

# Printing some features of the issue
print('*' * 50)
print("ISSUE")

print('Category: ', issue['category'])
print("Issue Count: ", len(issue_list))
print('Title: ', issue['data']['title'])
print('Notes Count: ', len(issue['data']['notes_data']))
print('Search Fields:', issue['search_fields'])
print('Timestamp: ', issue['timestamp'])
print('Updated on: ', issue['updated_on'])
print('UUID: ', issue['uuid'])
print('*' * 50)

# Fetch Merge Request data

pr_list_generator = gitlab.fetch(category=CATEGORY_MERGE_REQUEST, from_date=from_date)
pr_list = list(pr_list_generator)

with open("gitlab_pr.json", "w") as file:
    for prs in pr_list:
        json.dump(prs, file)

pr = pr_list[0]

# Printing some features of the repository data
print("PULL REQUEST")

print('Category: ', pr['category'])
print("Merge Request Count: ", len(pr_list))
print('Title: ', pr['data']['title'])
print('Notes Count: ', len(pr['data']['notes_data']))
print('Search Fields:', pr['search_fields'])
print('Timestamp: ', pr['timestamp'])
print('Updated on: ', pr['updated_on'])
print('UUID: ', pr['uuid'])
print('*' * 50)
