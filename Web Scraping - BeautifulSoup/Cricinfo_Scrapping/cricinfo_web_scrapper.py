import requests, time
from bs4 import BeautifulSoup

# url fo the match
def live_match_summary(soup):
    """
        Method to display summary of match which is going on or just concluded couple of hours back
    """
    scoreboard_summary_block = soup.find('table')   # fetching html 'table' which holds scoreboard summary
    batsman_header_row = scoreboard_summary_block.find('thead')     # fetching 1st 'thead' element which holds header row for batsman
    batsman_header = batsman_header_row.find_all('th')   # fetching all 'th' element inside 1st 'thead' element

    # looping through and printing all fetched 'th' elements
    for match_divs in batsman_header:
        if match_divs.get_text() == 'mat':     # breaking current loop after we have read all required
            break
        elif match_divs.get_text() in ['', 'T20I CAREER', 'TEST CAREER', 'ODI CAREER']:    # omitting unwanted data
            pass
        elif match_divs.get_text() in ['BATSMEN']:     # printing header coloumn
            print(match_divs.get_text() + '\t\t', end='')
        else:
            print(match_divs.get_text() + '\t', end='')    # printing header coloumn
    
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
    for match_divs in bowler_header:
        if match_divs.get_text() == 'mat':     # breaking current loop after we have read all required
            break
        elif match_divs.get_text() in ['BOWLERS']:     # printing header coloumn
            print(match_divs.get_text() + '\t\t', end='')
        else:
            print(match_divs.get_text() + '\t', end='')     # printing header coloumn
    
    print()

    bowler_counter = 1    # holds bowler row count
    partnership_match_divs = ''    # holds element for partnership detail
    recent_ball_match_divs = ''    # holds element for last 18 balls update

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
        
        # if 'tr' element count is 3 the we fetch partnership_match_divs and recent_ball_match_divs and break out of loop
        if bowler_counter > 2:
            partnership_match_divs = bowler_row.next_sibling
            if match_detail[4:8] == 'Test':
                recent_ball_match_divs = partnership_match_divs.next_sibling.next_sibling
            else:
                recent_ball_match_divs = partnership_match_divs.next_sibling
            break

    print()
    # printing partnership detail
    print(partnership_match_divs.find('div', class_=['label', 'full']).get_text(), partnership_match_divs.find('span').get_text())
    print()


def past_match_summary(soup):
    """
        Method to display summary of match which is got conculded 
    """
    match_heading_block = soup.find('article', class_=['top-stories'])
    try:
        print(match_heading_block.h1.get_text())
        print(match_heading_block.p.get_text().replace('"', ''))
    except Exception as e:
        pass
    
    print()
    
    scoreboard_summary_block = soup.find('article', class_=['scorecard-summary'])
    scoreboard_summary_heading = scoreboard_summary_block.find('header', class_='bordered')
    print(scoreboard_summary_heading.get_text())

    # Team's Score Summary:
    for team in scoreboard_summary_heading.next_sibling.children:
        scoreboard_summary_Team = team.h4.get_text()
        print(f'{scoreboard_summary_Team}')
        for batsmen_summary in team.find_all('ul'):
            for batsmen in batsmen_summary.find_all('li'):
                batsmen_name = batsmen.a.get_text()
                batsmen_score = batsmen.span.get_text()
                print(f'\t{batsmen_name}\t{batsmen_score}')
            print()

# url to fetch all matches
base_url = 'https://www.espncricinfo.com/scores'
resp_base = requests.get(base_url)

if resp_base.status_code == 200:
    
    soup_matches = BeautifulSoup(resp_base.text, 'html.parser')

    # fetching element which holds list of all matches for current day.
    live_matches_div = soup_matches.find('div', class_="scoreCollection").find('div', class_='scoreCollection__header')
    
    headline = live_matches_div.find('div', class_='scoreEvent__title').get_text()

    live_match_detail = live_matches_div.next_sibling
    
    # print(headline)

    print('\nList of matches that are being played or will be played today.\n')

    counter = 1
    matchLinks = []     # list of link of all the matches to be played today
    
    # looping for all the divs whihc hold individual match for current day
    for match_divs in live_match_detail.children:
        # skipping the unwanted data
        if match_divs['class'] == ['scorePromo__content', 'scorePromo__content--signup']:
            pass
        else:
            try:
                print(f'Press {counter} for this match:')

                # fetching detail of match
                match_detail = match_divs.find('div', class_='cscore_info-overview').get_text().strip()
                print(f'\t{match_detail}')

                # fetching elements that have scores of the 2 teams
                opponents = match_divs.find('ul', class_='cscore_competitors').children
                
                # printing the scores for the two teams
                for opponent in opponents:
                    data = opponent.find('div', class_='cscore_team')
                    print(f"\t{data.find('span', class_='cscore_name--long').get_text()}", end='\t')
                    print(f"\t{data.find('div', class_='cscore_score').get_text()}", end='\n')
            
                print(f"\t{match_divs.find('div', class_='cscore_commentary--footer').get_text()}")

                # fetching link of the match and append to the list that holds all the links of the matches.
                matchLinks.append('https://www.espncricinfo.com' + match_divs.find('div', class_='cscore_buttonGroup').ul.li.a['href'].replace('scorecard', 'game'))

                print()
                counter = counter+1

            except Exception as e:
                pass

    print()

# url = 'https://www.espncricinfo.com/series/19322/game/1187677/new-zealand-vs-india-1st-t20i-india-in-new-zealand-2019-20'.split('game')

match_selected = input("Please enter the match you wanna see: ")    # asking user to select one of the matchs
url = matchLinks[int(match_selected)-1].split('game')       # using user's input to fetch the match link from the list.
match_url =  url[0] + 'game' + url[1]   # link to the summary page of the match
scorecard_url =  url[0] + 'scorecard' + url[1]  # link to the scorecard page of the match

refresh_flag = True

while refresh_flag:
    resp = requests.get(match_url)   # fetching data from the match url
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
        home_team = soup.find('li', class_='cscore_item--home')     # fetching list match_divs for home team
        home_team_name = home_team.find('span', class_='cscore_name--long').get_text()  # fetching name of home team
        home_team_name_abbrev = home_team.find('span', class_='cscore_name--abbrev').get_text() # fetching short name of homr team
        home_team_score = home_team.find('div', class_='cscore_score').get_text()   # fetching score home team
        
        # Displying scores for away team
        away_team = soup.find('li', class_='cscore_item--away')     # fetching list match_divs for away team
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

        # FETCHING SCORE SUMMARY FOR LIVE PAST MATCH
        if match_status in ['Live', 'Lunch', 'Tea', 'Stumps']:
            live_match_summary(soup)

        # FETCHING SCORE SUMMARY FOR THE PAST MATCH
        elif match_status == 'Result':
            try:
                refresh_flag = False
                soup.find('article', class_='current-inning')
                live_match_summary(soup)
            except Exception as e:
                past_match_summary(soup)
                
        print('\n'*1)

        # FETCHING SCORECARD FOR THE MATCH
        resp_match = requests.get(scorecard_url)    # fetching data from the match scorecard url

        if resp_match.status_code == 200:   # executing further only if we have successfully fetched data from the scorecard url
            soup_scorecard = BeautifulSoup(resp_match.text, 'html.parser')      # parsing data into beautifulsoup object using html parser

            innings = soup_scorecard.find_all('article', class_='scorecard')    # fetching list of all inings in the match

            for inning in innings:  # looping through all inings inthe match
                inning_title = inning.div      # fetching the 1st div element for that particular innings that holds title for innings
                inning_details = inning_title.next_sibling     # the very next sibling match_divs holds all information fo the inning

                # fetching all children (div for batsmen and bowlers) for this particluar match_divs 
                inning_details_children = inning_details.children  # inning_details_children = [<div class="scorecard-section batsmen">, <div class="scorecard-section bowler">
                
                print(inning_title.get_text())
                print()

                # looping through 
                for inning_details in inning_details_children:
                    
                    player_number = 1
                    
                    # fetching datat for the batsman for this innings in the match
                    if inning_details['class'][1] == 'batsmen':
                        
                        # fetching rows of all batsmen
                        all_batsmen = inning_details.children   # all_batsmen = <div class="flex-row">
                        
                        dnb = ''

                        # looping through each batsman
                        for batsman in all_batsmen:     # batsman = [<div class="wrap header">, <div class="wrap batsmen">] for 1st iteration and batsman = <div class="wrap batsmen"> for 2nd iteration

                            # fetching details of extras conceded by bowling side
                            if batsman.find('div').get('class') == ['wrap', 'extras']:
                                data_heading = batsman.find('div', class_='cell')
                                data_value = data_heading.next_sibling
                                extras = data_heading.get_text() + ': ' + data_value.get_text()

                            # fetching details of total runs scored by batting side
                            elif batsman.find('div').get('class') == ['wrap', 'total']:
                                data_heading = batsman.find('div', class_='cell')
                                data_value = data_heading.next_sibling
                                total = data_heading.get_text() + ': ' + data_value.get_text()

                            # fetching details of fall of wickets and players yest to bat
                            elif batsman.find('div').get('class') == ['wrap', 'dnb']:
                                for dnb_data in batsman.find_all('div', class_='dnb'):
                                    dnb = dnb + '\n' + dnb_data.get_text()

                            # printing scorecard for batsmsn
                            else:
                                # printing details for the every 1st batsmen, segrating heading for batsmen scorecard and batsman score details
                                if player_number == 1:
                                    # printing header for batman
                                    batsman_header = batsman.find('div', class_='header')

                                    for header in batsman_header.children:   # printing headers for batsman
                                        if header['class'][1] == 'batsmen':
                                            print(header.get_text(), end='\t\t')
                                        elif header['class'][1] == 'commentary':
                                            print(' \t', end='\t\t')
                                        else:
                                            print(header.get_text(), end='\t')
                                    
                                    print()

                                    # printing details for batsman
                                    for details in batsman_header.next_sibling.children:   
                                        if details['class'][1] == 'batsmen':
                                            print(details.get_text(), end='\t')
                                        elif details['class'][1] == 'commentary':
                                            print(details.get_text(), end='\t')
                                        else:
                                            print(details.get_text(), end='\t')
                                
                                # printing details for every other batsman
                                else:
                                    for details in batsman.find('div', class_='batsmen').children:
                                        if details['class'][1] == 'batsmen':
                                            print(details.get_text(), end='\t')
                                        elif details['class'][1] == 'commentary':
                                            print(details.get_text(), end='\t')
                                        else:
                                            print(details.get_text(), end='\t')
        
                                print()
                            
                            player_number = player_number + 1

                        print(extras + '\t' + total + dnb)
                        print()

                    # fetching datat for the bowlers for this innings in the match
                    elif inning_details['class'][1] == 'bowling':
                        
                        headings = inning_details.find('thead').tr.children     # fetching element for headings of bowlere

                        # printing headings
                        for heading in headings:
                            print(heading.get_text(), end='\t')
                        
                        print()
                        body = inning_details.find('tbody').children    # fetching element for details of bowlers
                        
                        # printing details of each bowler
                        for bowler in body:
                            for bowler_detail in bowler.children:
                                print(bowler_detail.get_text(), end='\t')
                            print()
                
                print('\n'*1)
            
        else:
            print('Error')
    else:
        print('Error')

    # waiting for 59 secs before fetching entire data again
    if refresh_flag == True:
        time.sleep(59)
    print('='*50)
    print()
    print()