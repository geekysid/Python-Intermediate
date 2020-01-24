"""
    Program that takes username of github from user and displays stats his/her accounts
    1. User basic information  
        Name
        Website
        Avatar
        Location
        Github Link
        Bio
        email
        Account created on
        Account last updated
        Number of people following this Github Account
        Number of people this account is following
    2. Language chart
    3. Repository chart wrt number oc commit
"""


import requests, json

github_username = input("Please enter your github username: ")  # asking username of the github from user for which data is to be fetched

url = 'https://api.github.com/users/'+github_username   # creating a api url

resp = requests.get(url)    # making api requests to githb to collect data for the user's username
if resp.status_code == 200:     # if the api request returns validity of the account

    # fetching basic data from the api
    json_user = json.loads(resp.text)
    name = json_user['name']
    website = json_user['blog']
    Username = json_user['login']
    avatar = json_user['avatar_url']
    location = json_user['location']
    html_url = json_user['html_url']
    bio = json_user['bio'].replace('\n', '. ')
    email = json_user['email']
    created_at = json_user['created_at']
    updated_at = json_user['updated_at']
    followers = json_user['followers']
    followings = json_user['following']
    events_url = json_user['events_url']

    print('\nUser\'s Basic Information\n' + '='*25 + '\n')
    print(f'Github Account Details with username: {Username}')
    print(f'Account Holder\'s Name: {name}')
    print(f'Account Holder\'s Website: {website}')
    print(f'Account Holder\'s Avatar: {avatar}')
    print(f'Account Holder\'s Location: {location}')
    print(f'Account Holder\'s Github Link: {html_url}')
    print(f'Account Holder\'s Bio: {bio}')
    print(f'Account Holder\'s email: {email}')
    print(f'This Github account was created on: {created_at}')
    print(f'This Github account was last updated on: {updated_at}')
    print(f'Number of people following this Github Account: {followers}')
    print(f'Number of people this account is following: {followings}')

    # using repos api link to fetch data about user's repositary
    repos_url = json_user['repos_url']
    resp_repos = requests.get(repos_url)

    if resp_repos.status_code == 200:   # executing if user have atleast one repository
        json_repos = json.loads(resp_repos.text)    # converting the received reponse object into json

        print(f'Total number of repositary user has: {len(json_repos)}')
        print('\nUser\'s Repository Information\n' + '='*30 + '\n')

        # looping through all of repos
        for repo in json_repos:
            repo_name = repo['name']
            repo_desc = repo['description']
            repo_privary = repo['private']
            repo_starCount = repo['stargazers_count']
            repo_viewCount = repo['watchers_count']
            repo_url = repo['html_url']
            repo_api_url = repo['url']
            repo_languages_url = repo['languages_url']
            repo_forks_url = repo['forks_url']
            repo_contributors_url = repo['contributors_url']
            repo_subscribers_url = repo['subscribers_url']
            repo_commits_url = repo['commits_url']
            repo_issues_url = repo['issues_url']
            repo_issuesCount = repo['open_issues']
            repo_forksCount = repo['forks_count']
            repo_created_at = repo['created_at']
            repo_updated_at = repo['updated_at']

            resp_laguage = requests.get(repo_languages_url)
            json_lang = json.loads(resp_laguage.text)

            resp_susbcribe = requests.get(repo_subscribers_url)
            json_subs = json.loads(resp_susbcribe.text)

            resp_commits = requests.get(repo_commits_url)
            json_commits = json.loads(resp_commits.text)
            print(json.dumps(json_commits, indent=4))

            resp_forks = requests.get(repo_forks_url)
            json_forks = json.loads(resp_forks.text)

            resp_issues = requests.get(repo_issues_url)
            json_issues = json.loads(resp_issues.text)

            print(f'*** {repo_name} ***')
            print(f'\tDescription: {repo_desc}')
            print(f'\tPrivate: {repo_privary}')
            print(f'\tURL: {repo_url}')
            print(f'\tTotal Views: {repo_viewCount}')
            print(f'\tTotal Number of Stars: {repo_starCount}')
            print(f'\tTotal Number of Forks: {repo_forksCount}')
            print(f'\tTotal Number of Isusses: {repo_issuesCount}')
            print(f'\tCreated On: {repo_created_at}')
            print(f'\tLast Updated On: {repo_updated_at}')

            print(f'\tLanguages: {repo_languages_url}')
            for lang in json_lang:
                print(f'\t\t{lang}: {json_lang[lang]}')
            print()
            print(f'\tSubscriber: {repo_subscribers_url}')
            for sub in json_subs:
                print(f'\t\tUsername: {sub["login"]}, URL: {sub["html_url"]}')
            print()
            print(f'\tCommits Details: {repo_commits_url}')
            # for commit in json_commits:
            #     commited_by = commit
            #     print(commited_by)bchiang7
            #     commited_by_url = json_commits[commit]['committer']['html_url']
            #     commit_log = json_commits[commit]['sha']
            #     commit_url = json_commits[commit]['html_url']
            #     commit_date = json_commits[commit]['commit']['committer']['date']
            #     commit_message = json_commits[commit]['commit']['message']
            #     commit_comment = json_commits[commit]['commit']['comment_count']
            #     commit_comment_api = json_commits[commit]['comments_url']

            #     print(f'\t\tcommited_by: {commited_by}')
            #     print(f'\t\tcommited_by_url: {commited_by_url}')
            #     print(f'\t\tcommit_log: {commit_log}')
            #     print(f'\t\tcommit_url: {commit_url}')
            #     print(f'\t\tcommit_date: {commit_date}')
            #     print(f'\t\tcommit_message: {commit_message}')
            #     print(f'\t\tcommit_comment: {commit_comment}')
            #     print(f'\t\tcommit_comment_api: {commit_comment_api}')
            #     print()
            print('\n' + '-'*50 + '\n')

    else:
        print("Sorry.. We are unable to connect to the user's repositaries. Please make sure user have atleats one repositary")

else:   # if there is no github account with the username provided by user
    if resp.status_code == 403:
        print(f'Opps..... Something went wrong. You might have hit the rate limit of 60 searches per hour. Please try after an hour or so.')
    else:
        print("Sorry this is not a valid username")

# user_data = json.loads(resp.text)
# print(json.dumps(user_data, indent=4))

# user_repos = json.loads(requests.get(user_data['repos_url']).text)
# print(len(user_repos))
# print(json.dumps(user_repos, indent=4))

# for repo in user_repos:
#     print(repo['name'])
#     print(repo['owner']['login'])
#     print(repo['description'])
#     print(repo['url'])
#     print(repo['languages_url'])
#     repo_language = json.loads(requests.get(repo['languages_url']).text)
#     # print(json.dumps(repo_language))
#     print()
#     break

# USER BASIC INFORMATION
# {
#     "login": "siddhantshah1986",
#     "id": 59141234,
#     "node_id": "MDQ6VXNlcjU5MTQxMjM0",
#     "avatar_url": "https://avatars2.githubusercontent.com/u/59141234?v=4",
#     "gravatar_id": "",
#     "url": "https://api.github.com/users/siddhantshah1986",
#     "html_url": "https://github.com/siddhantshah1986",
#     "followers_url": "https://api.github.com/users/siddhantshah1986/followers",
#     "following_url": "https://api.github.com/users/siddhantshah1986/following{/other_user}",
#     "gists_url": "https://api.github.com/users/siddhantshah1986/gists{/gist_id}",
#     "starred_url": "https://api.github.com/users/siddhantshah1986/starred{/owner}{/repo}",
#     "subscriptions_url": "https://api.github.com/users/siddhantshah1986/subscriptions",
#     "organizations_url": "https://api.github.com/users/siddhantshah1986/orgs",
#     "repos_url": "https://api.github.com/users/siddhantshah1986/repos",
#     "events_url": "https://api.github.com/users/siddhantshah1986/events{/privacy}",
#     "received_events_url": "https://api.github.com/users/siddhantshah1986/received_events",
#     "type": "User",
#     "site_admin": false,
#     "name": "Siddhant Shah",
#     "company": null,
#     "blog": "http://www.geekysid.com",
#     "location": "India",
#     "email": null,
#     "hireable": null,
#     "bio": "I love coding. Let's Python\r\n\r\nwww.geekysid.com",
#     "public_repos": 5,
#     "public_gists": 0,
#     "followers": 0,
#     "following": 0,
#     "created_at": "2019-12-22T14:06:12Z",
#     "updated_at": "2020-01-21T23:54:10Z"
# }

# REPOSITORY INFORMATION
# {
#     "id": 231768712,
#     "node_id": "MDEwOlJlcG9zaXRvcnkyMzE3Njg3MTI=",
#     "name": "Django-Projects",
#     "full_name": "siddhantshah1986/Django-Projects",
#     "private": false,
#     "owner": {
#         "login": "siddhantshah1986",
#         "id": 59141234,
#         "node_id": "MDQ6VXNlcjU5MTQxMjM0",
#         "avatar_url": "https://avatars2.githubusercontent.com/u/59141234?v=4",
#         "gravatar_id": "",
#         "url": "https://api.github.com/users/siddhantshah1986",
#         "html_url": "https://github.com/siddhantshah1986",
#         "followers_url": "https://api.github.com/users/siddhantshah1986/followers",
#         "following_url": "https://api.github.com/users/siddhantshah1986/following{/other_user}",
#         "gists_url": "https://api.github.com/users/siddhantshah1986/gists{/gist_id}",
#         "starred_url": "https://api.github.com/users/siddhantshah1986/starred{/owner}{/repo}",
#         "subscriptions_url": "https://api.github.com/users/siddhantshah1986/subscriptions",
#         "organizations_url": "https://api.github.com/users/siddhantshah1986/orgs",
#         "repos_url": "https://api.github.com/users/siddhantshah1986/repos",
#         "events_url": "https://api.github.com/users/siddhantshah1986/events{/privacy}",
#         "received_events_url": "https://api.github.com/users/siddhantshah1986/received_events",
#         "type": "User",
#         "site_admin": false
#     },
#     "html_url": "https://github.com/siddhantshah1986/Django-Projects",
#     "description": "Projects based on Django",
#     "fork": false,
#     "url": "https://api.github.com/repos/siddhantshah1986/Django-Projects",
#     "forks_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/forks",
#     "keys_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/keys{/key_id}",
#     "collaborators_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/collaborators{/collaborator}",
#     "teams_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/teams",
#     "hooks_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/hooks",
#     "issue_events_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/issues/events{/number}",
#     "events_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/events",
#     "assignees_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/assignees{/user}",
#     "branches_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/branches{/branch}",
#     "tags_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/tags",
#     "blobs_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/git/blobs{/sha}",
#     "git_tags_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/git/tags{/sha}",
#     "git_refs_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/git/refs{/sha}",
#     "trees_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/git/trees{/sha}",
#     "statuses_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/statuses/{sha}",
#     "languages_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/languages",
#     "stargazers_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/stargazers",
#     "contributors_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/contributors",
#     "subscribers_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/subscribers",
#     "subscription_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/subscription",
#     "commits_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/commits{/sha}",
#     "git_commits_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/git/commits{/sha}",
#     "comments_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/comments{/number}",
#     "issue_comment_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/issues/comments{/number}",
#     "contents_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/contents/{+path}",
#     "compare_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/compare/{base}...{head}",
#     "merges_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/merges",
#     "archive_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/{archive_format}{/ref}",
#     "downloads_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/downloads",
#     "issues_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/issues{/number}",
#     "pulls_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/pulls{/number}",
#     "milestones_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/milestones{/number}",
#     "notifications_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/notifications{?since,all,participating}",
#     "labels_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/labels{/name}",
#     "releases_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/releases{/id}",
#     "deployments_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/deployments",
#     "created_at": "2020-01-04T13:31:47Z",
#     "updated_at": "2020-01-19T07:45:59Z",
#     "pushed_at": "2020-01-19T07:45:57Z",
#     "git_url": "git://github.com/siddhantshah1986/Django-Projects.git",
#     "ssh_url": "git@github.com:siddhantshah1986/Django-Projects.git",
#     "clone_url": "https://github.com/siddhantshah1986/Django-Projects.git",
#     "svn_url": "https://github.com/siddhantshah1986/Django-Projects",
#     "homepage": null,
#     "size": 2084,
#     "stargazers_count": 0,
#     "watchers_count": 0,
#     "language": "JavaScript",
#     "has_issues": true,
#     "has_projects": true,
#     "has_downloads": true,
#     "has_wiki": true,
#     "has_pages": false,
#     "forks_count": 0,
#     "mirror_url": null,
#     "archived": false,
#     "disabled": false,
#     "open_issues_count": 0,
#     "license": null,
#     "forks": 0,
#     "open_issues": 0,
#     "watchers": 0,
#     "default_branch": "master"
# }


#     "sha": "1d8c1dc43b0d1ca57acda0ca0957a64ea2d24024",
#     "node_id": "MDY6Q29tbWl0MjMxNzY4NzEyOjFkOGMxZGM0M2IwZDFjYTU3YWNkYTBjYTA5NTdhNjRlYTJkMjQwMjQ=",
#     "commit": {
#       "author": {
#         "name": "Siddhant",
#         "email": "siddhant.shah.1986@gmail.com",
#         "date": "2020-01-19T07:45:50Z"
#       },
#       "committer": {
#         "name": "Siddhant",
#         "email": "siddhant.shah.1986@gmail.com",
#         "date": "2020-01-19T07:45:50Z"
#       },
#       "message": "Updated Readme File",
#       "tree": {
#         "sha": "f0976261c8d446c081f09ae98c78dec7ef717298",
#         "url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/git/trees/f0976261c8d446c081f09ae98c78dec7ef717298"
#       },
#       "url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/git/commits/1d8c1dc43b0d1ca57acda0ca0957a64ea2d24024",
#       "comment_count": 0,
#       "verification": {
#         "verified": false,
#         "reason": "unsigned",
#         "signature": null,
#         "payload": null
#       }
#     },
#     "url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/commits/1d8c1dc43b0d1ca57acda0ca0957a64ea2d24024",
#     "html_url": "https://github.com/siddhantshah1986/Django-Projects/commit/1d8c1dc43b0d1ca57acda0ca0957a64ea2d24024",
#     "comments_url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/commits/1d8c1dc43b0d1ca57acda0ca0957a64ea2d24024/comments",
#     "author": {
#       "login": "siddhantshah1986",
#       "id": 59141234,
#       "node_id": "MDQ6VXNlcjU5MTQxMjM0",
#       "avatar_url": "https://avatars2.githubusercontent.com/u/59141234?v=4",
#       "gravatar_id": "",
#       "url": "https://api.github.com/users/siddhantshah1986",
#       "html_url": "https://github.com/siddhantshah1986",
#       "followers_url": "https://api.github.com/users/siddhantshah1986/followers",
#       "following_url": "https://api.github.com/users/siddhantshah1986/following{/other_user}",
#       "gists_url": "https://api.github.com/users/siddhantshah1986/gists{/gist_id}",
#       "starred_url": "https://api.github.com/users/siddhantshah1986/starred{/owner}{/repo}",
#       "subscriptions_url": "https://api.github.com/users/siddhantshah1986/subscriptions",
#       "organizations_url": "https://api.github.com/users/siddhantshah1986/orgs",
#       "repos_url": "https://api.github.com/users/siddhantshah1986/repos",
#       "events_url": "https://api.github.com/users/siddhantshah1986/events{/privacy}",
#       "received_events_url": "https://api.github.com/users/siddhantshah1986/received_events",
#       "type": "User",
#       "site_admin": false
#     },
#     "committer": {
#       "login": "siddhantshah1986",
#       "id": 59141234,
#       "node_id": "MDQ6VXNlcjU5MTQxMjM0",
#       "avatar_url": "https://avatars2.githubusercontent.com/u/59141234?v=4",
#       "gravatar_id": "",
#       "url": "https://api.github.com/users/siddhantshah1986",
#       "html_url": "https://github.com/siddhantshah1986",
#       "followers_url": "https://api.github.com/users/siddhantshah1986/followers",
#       "following_url": "https://api.github.com/users/siddhantshah1986/following{/other_user}",
#       "gists_url": "https://api.github.com/users/siddhantshah1986/gists{/gist_id}",
#       "starred_url": "https://api.github.com/users/siddhantshah1986/starred{/owner}{/repo}",
#       "subscriptions_url": "https://api.github.com/users/siddhantshah1986/subscriptions",
#       "organizations_url": "https://api.github.com/users/siddhantshah1986/orgs",
#       "repos_url": "https://api.github.com/users/siddhantshah1986/repos",
#       "events_url": "https://api.github.com/users/siddhantshah1986/events{/privacy}",
#       "received_events_url": "https://api.github.com/users/siddhantshah1986/received_events",
#       "type": "User",
#       "site_admin": false
#     },
#     "parents": [
#       {
#         "sha": "5c63efc40a7ec4d64481153b9fec01c9db76987d",
#         "url": "https://api.github.com/repos/siddhantshah1986/Django-Projects/commits/5c63efc40a7ec4d64481153b9fec01c9db76987d",
#         "html_url": "https://github.com/siddhantshah1986/Django-Projects/commit/5c63efc40a7ec4d64481153b9fec01c9db76987d"
#       }
#     ]
#   }