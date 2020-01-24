import requests
from bs4 import BeautifulSoup

# url fo the match
base_url = 'https://www.espncricinfo.com/series/19286/game/1185307/south-africa-vs-england-4th-test-icc-world-test-championship-2019-2021'

resp = requests.get(base_url)   # fetching data from the url
if resp.status_code == 200:     # executing further only if we have successfully fetched data from the url
    soup = BeautifulSoup(resp.text, 'html.parser')      # parsing data into beautifulsoup object using html parser

    # match data
    match_div = soup.find('div', class_='cscore_overview')
    match_status = match_div.find('span', class_='cscore_time').get_text()  # status of match, live, result, Abandoned, Date of match to be held in future and more
    match_date = match_div.find('span', class_='cscore_date').get_text()    # date of match
    match_detail = match_div.find('div', class_='cscore_info-overview').get_text()  # detail of match played
    
    print()
    print(match_status)
    print(match_detail)
    print()
    
    # Displying scores for home team
    home_team = soup.find('li', class_='cscore_item--home')     # fetching list tag for home team
    home_team_name = home_team.find('span', class_='cscore_name--long').get_text()  # fetching name of home team
    home_team_name_abbrev = home_team.find('span', class_='cscore_name--abbrev').get_text() # fetching short name of homr team
    home_team_score = home_team.find('div', class_='cscore_score').get_text()   # fetching score home team
    
    # Displying scores for away team
    away_team = soup.find('li', class_='cscore_item--away')     # fetching list tag for away team
    away_team_name = away_team.find('span', class_='cscore_name--long').get_text()  # fetching name of away team
    away_team_name_abbrev = away_team.find('span', class_='cscore_name--abbrev').get_text() # fetching short name of away team
    away_team_score = away_team.find('div', class_='cscore_score').get_text()   # fetching score away team

    # current detail of match
    score_note = soup.find('span', class_='cscore_notes_game').get_text()

    print(f'{home_team_name}({home_team_name_abbrev}): {home_team_score}')
    print(f'{away_team_name}({away_team_name_abbrev}): {away_team_score}')
    print()
    print(score_note)
    print()

    # score summary for live match
    if match_status == 'Live':

        scoreboard_summary_block = soup.find('table')   # fetching html 'table' which holds scoreboard summary
        batsman_header_row = scoreboard_summary_block.find('thead')     # fetching 1st 'thead' element which holds header row for batsman
        batsman_header = batsman_header_row.find_all('th')   # fetching all 'th' element inside 1st 'thead' element

        # looping through and printing all fetched 'th' elements
        for tag in batsman_header:
            if tag.get_text() == 'mat':     # breaking current loop after we have read all required
                break
            elif tag.get_text() in ['', 'T20I CAREER', 'TEST CAREER', 'ODI CAREER']:    # omitting unwanted data
                pass
            elif tag.get_text() in ['BATSMEN']:     # printing header coloumn
                print(tag.get_text() + '\t\t', end='')
            else:
                print(tag.get_text() + '\t', end='')    # printing header coloumn
        
        print()

        # fetching all details of current 2 batsmen
        batsman = batsman_header_row.next_sibling.find_all('tr')
        
        # looping through the 2 'tr' element which holes batsmen's innings detail
        for batsman_row in batsman:
            td_counter = 1     # holds number of 'td' element

            # looping through and printing all the batsman details for current innings
            for batsman_detail in batsman_row.find_all('td'):
                if td_counter == 1:    # fteching batsman's name for the 1st 'td' element
                    player_name = batsman_detail.find('a', class_='short-name').get_text()
                    print(player_name + '\t', end='')
                elif td_counter == 9:  # breaking out of current loop when we have fetched all required data
                    break
                elif td_counter == 7:
                    print(batsman_detail.get_text() + '\t\t', end='')
                else:
                    print(batsman_detail.get_text() + '\t', end='')
                td_counter = td_counter + 1
            print()
        
        print()

        # fetching bowler header details
        bowler_header_row = batsman_header_row.next_sibling.next_sibling # fetching 2nd 'thead' element which holds header row for bowler
        bowler_header = bowler_header_row.find_all('th')    # fetching all 'th' element inside 2nd 'thead' element
        
        # looping through and printing all fetched 'th' elements
        for tag in bowler_header:
            if tag.get_text() == 'mat':     # breaking current loop after we have read all required
                break
            elif tag.get_text() in ['BOWLERS']:     # printing header coloumn
                print(tag.get_text() + '\t\t', end='')
            else:
                print(tag.get_text() + '\t', end='')     # printing header coloumn
        
        print()

        bowler_counter = 1    # holds bowler row count
        partnership_tag = ''    # holds element for partnership detail
        recent_ball_tag = ''    # holds element for last 18 balls update

        # fetching all details of current 2 bowlers
        bowler = bowler_header_row.next_sibling.find_all('tr')
        
        # looping through the 'tr' element which holes bowler's innings detail
        for bowler_row in bowler:
            td_counter = 1      # holds number of 'td' element

            # looping through and printing all the bowler details for current innings
            for bowler_detail in bowler_row.find_all('td'):
                if td_counter == 1:     # fteching bowler's name for the 1st 'td' element
                    player_name = bowler_detail.find('a', class_='short-name').get_text()
                    print(player_name + '\t', end='')
                elif td_counter == 11:  # breaking out of current loop when we have fetched all required data
                    break
                else:
                    print(bowler_detail.get_text() + '\t', end='')
                td_counter = td_counter + 1     # increasing 'td' element count by 1

            bowler_counter = bowler_counter + 1     # increasing 'tr' element count by 1

            print()
            
            # if 'tr' element count is 3 the we fetch partnership_tag and recent_ball_tag and break out of loop
            if bowler_counter > 2:
                partnership_tag = bowler_row.next_sibling
                recent_ball_tag = partnership_tag.next_sibling
                break

        print()
        # printing partnership detail
        print(partnership_tag.find('div', class_=['label', 'full']).get_text(), partnership_tag.find('span').get_text())
        print()

        # printing runs scored of last 18 ball 
        ball_update = recent_ball_tag.find('div', class_='label')
        print(ball_update.get_text()+ ': ', end='')
        for balls in ball_update.next_siblings:
            print(balls.get_text() + ' ', end='')

    # score summary for match played in past
    elif match_status == 'Result':
        print('Scoreboard')
        scoreboard = soup.find('article', class_=['sub-module', 'scorecard'])
        print(scoreboard.name)

    print()
    
else:
    print('Error')

print()