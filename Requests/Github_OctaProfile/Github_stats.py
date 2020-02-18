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
from datetime import datetime
import pandas as pd

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
    # print(f'Account Holder\'s Name: {name}')
    # print(f'Account Holder\'s Website: {website}')
    # print(f'Account Holder\'s Avatar: {avatar}')
    # print(f'Account Holder\'s Location: {location}')
    # print(f'Account Holder\'s Github Link: {html_url}')
    # print(f'Account Holder\'s Bio: {bio}')
    # print(f'Account Holder\'s email: {email}')
    # print(f'This Github account was created on: {created_at}')
    # print(f'This Github account was last updated on: {updated_at}')
    # print(f'Number of people following this Github Account: {followers}')
    # print(f'Number of people this account is following: {followings}')

    language_chart_data = {}
    starsPerRepo_chart_data = []
    starsPerLanguage_chart_data = {}
    sizePerLanguage_chart_data = {}

    # using repos api link to fetch data about user's repositary
    repos_url = json_user['repos_url']+'?per_page=100'
    resp_repos = requests.get(repos_url)

    if resp_repos.status_code == 200:   # executing if user have atleast one repository
        json_repos = json.loads(resp_repos.text)    # converting the received reponse object into json

        # print(f'Total number of repository user has: {len(json_repos)}')
        # print('\nUser\'s Repository Information\n' + '='*30 + '\n')

        repository_details = []

        # looping through all of repos
        for repo in json_repos:
            repo_name = repo['name']
            repo_desc = repo['description']
            repo_privary = repo['private']
            repo_starCount = int(repo['stargazers_count'])
            repo_viewCount = repo['watchers_count']
            repo_url = repo['html_url']
            repo_issuesCount = repo['open_issues']
            repo_forksCount = int(repo['forks_count'])
            repo_created_at = repo['created_at']
            repo_updated_at = repo['updated_at']
            repo_language = repo['language']
            repo_size = repo['size']
            repo_size_int = int(repo['size'])

            date = datetime.strptime(repo_updated_at, "%Y-%m-%dT%H:%M:%SZ")
            update_date = date.strftime('%d/%m/%Y')
            # print(update_date)

            # dict of all repos with required details to be displayed
            repository_details.append({
                'repo': repo_name,
                'detail': repo_desc,
                'language': repo_language,
                'fork_count': repo_forksCount,
                'star_count': repo_starCount,
                'last_updated': update_date,
                'size': int(repo_size),
                'size_kb': '{:,} KB'.format(int(repo_size))
            })

            # # creating list of dictonary that has language and its counts to get languages used in repos
            # if repo_language in [x['language'] for x in language_chart_data]:
            #     for item in language_chart_data:
            #         if repo_language == item['language']:
            #             item['count'] = int(item['count']) + 1
            # else:
            #     language_chart_data.append({'language': repo_language, 'count':1})
                
            if repo_language in [x for x in language_chart_data.keys()]:
                language_chart_data[repo_language] += 1
            else:
                language_chart_data[repo_language] = 1
            
            # creating list of dictonary that has repos and its starcounts to get star count per repos
            if repo_name in [x['repo'] for x in starsPerRepo_chart_data]:
                for item in starsPerRepo_chart_data:
                    if repo_name == item['repo']:
                        item['starCount'] = int(item['starCount']) + int(repo_starCount)
            else:
                # starsPerRepo_chart_data[repo_name] = 'starCount': int(repo_starCount)
                starsPerRepo_chart_data.append({'repo': repo_name, 'starCount': int(repo_starCount)})

            # if repo_name in [x for x in starsPerRepo_chart_data.keys()]:
            #     starsPerRepo_chart_data[repo_name] += repo_starCount
            # else:
            #     starsPerRepo_chart_data[repo_name] = repo_starCount

            # # creating list of dictonary that has language and its starcounts to get star count per languages
            # if repo_language in [x['language']  for x in starsPerLanguage_chart_data]:
            #     for item in starsPerLanguage_chart_data:
            #         if repo_language == item['language']:
            #             item['starCount'] = int(item['starCount']) + int(repo_starCount)
            # else:
            #     starsPerLanguage_chart_data.append({'language': repo_language, 'starCount': int(repo_starCount)})

            if repo_language in [x for x in starsPerLanguage_chart_data.keys()]:
                starsPerLanguage_chart_data[repo_language] += repo_starCount
            else:
                starsPerLanguage_chart_data[repo_language] = repo_starCount

            
            # creating list of dictonary that has language and its sizes to get star count per languages
            if repo_language in [x for x in sizePerLanguage_chart_data.keys()]:
                sizePerLanguage_chart_data[repo_language] += repo_size_int
            else:
                sizePerLanguage_chart_data[repo_language] = repo_size_int

            # if repo_language in starsPerLanguage_chart_data.keys():
            #     starsPerLanguage_chart_data[repo_language] = starsPerLanguage_chart_data[repo_language] + int(repo_starCount)
            # else:
            #     starsPerLanguage_chart_data[repo_language] = int(repo_starCount)

            # print(f'*** {repos_url} ***')
            # print(f'*** {repo_name} ***')
            # print(f'\tDescription: {repo_desc}')
            # print(f'\tPrivate: {repo_privary}')
            # print(f'\tURL: {repo_url}')
            # print(f'\tTotal Views: {repo_viewCount}')
            # print(f'\tTotal Number of Stars: {repo_starCount}')
            # print(f'\tTotal Number of Forks: {repo_forksCount}')
            # print(f'\tTotal Number of Isusses: {repo_issuesCount}')
            # print(f'\tCreated On: {repo_created_at}')
            # print(f'\tLast Updated On: {repo_updated_at}')
            # print(f'\tRepo Language: {repo_language}')
            # print(f'\tRepo Size: {repo_size}')

        # dataframe that hold all repository details
        df = pd.DataFrame(repository_details)

        # Dataframe that hold repository details sorted for FORK_COUNT values
        fork_df = df.sort_values(by='fork_count', ascending=False)
        fork_list = fork_df.head(9).values.tolist()

        # Dataframe that hold repository details sorted for SIZE values
        size_df = df.sort_values(by='size', ascending=False)
        size_list = size_df.head(9).values.tolist()

        # Dataframe that hold repository details sorted for STAR_COUNT values
        star_df = df.sort_values(by='star_count', ascending=False)
        star_list = star_df.head(9).values.tolist()

        # Dataframe that hold repository details sorted for UPDATED_DATE values
        df2 = pd.DataFrame(starsPerRepo_chart_data)
        starsPerRepo_df = df2.sort_values(by='starCount', ascending=False)
        starsPerRepo_list = starsPerRepo_df.head(6).values.tolist()
        starsPerRepo_dict = {}

        for item in starsPerRepo_list:
            starsPerRepo_dict[item[0]] = item[1]

        # for item in size_list:
        #     print(item)

    else:
        print("Sorry.. We are unable to connect to the user's repositaries. Please make sure user have atleats one repositary")
    
    print()
    print(starsPerLanguage_chart_data)
    print()
    print(starsPerRepo_dict)
    print()
    
    # print()
    # print(f'language_chart_data: {language_chart_data}')
    # print()
    # print(f'starsPerRepo_chart_data: {starsPerRepo_chart_data}')
    # print()
    # print(f'starsPerLanguage_chart_data: {starsPerLanguage_chart_data}')
    # print()
    # print(f'sizePerLanguage_chart_data: {sizePerLanguage_chart_data}')

else:   # if there is no github account with the username provided by user
    if resp.status_code == 403:
        print(f'Opps..... Something went wrong. You might have hit the rate limit of 60 searches per hour. Please try after an hour or so.')
    else:
        print("Sorry this is not a valid username")
