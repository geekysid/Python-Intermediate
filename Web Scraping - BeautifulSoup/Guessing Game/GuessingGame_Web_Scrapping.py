# In this project we'll be building a quotes guessing game. When run, this program will scrape a website for a collection of quotes. Pick one at random and display it. 
# The player will have four chances to guess who said the quote. After every wrong guess they'll get a hint about the author's identity.

# Requirements:
# 1. Create a file called `GuessingGame_Web_Scrapping.py` which, when run, grabs data on every quote from the website http://quotes.toscrape.com
# 2. We will use `bs4` and `requests` to get the data. For each quote we will grab the text of the quote, the name of the person who said the quote, 
#   and the href of the link to the person's bio. Store all of this information in a list.
# 3. Next, display the quote to the user and ask who said it. The player will have four guesses remaining.
# 4. After each incorrect guess, the number of guesses remaining will decrement. If the player gets to zero guesses without identifying the author,
#   the player loses and the game ends. If the player correctly identifies the author, the player wins!
# 5. After every incorrect guess, the player receives a hint about the author. 
# 6. For the first hint, make another request to the author's bio page (this is why we originally scrape this data),
#   and tell the player the author's birth date and location.
# 7. The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, 
#   the number of letters in one of the names, etc.
# 8. When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.
# Good luck!

import requests
from bs4 import BeautifulSoup
from random import randint


def requests_quotes(url):
    """Method that fetches datat from the given url using requests library"""
    resp = requests.get(url)
    return resp


def author_details(url, quotes_count):
    """ Method that uses response object to fetch auther details from a given url. We use beautifulSoup to get the data from resp oject.
        We will update author_dict dictionary here that will be used to give hints about author by sharing his information

        Args:
            url (str): url of the author
            quotes_count (int): count of quotation stored in the quotes_dict ductionay. This is also the key of the before mentioned dictionary.
    """

    resp = requests_quotes(url)     # fetching data from author url
    if resp.status_code == 200:     # executing only if status code is 200
        soup = BeautifulSoup(resp.text, 'html.parser')      # parsing data into html to get soup obj
        authorName = soup.find('h3', class_="author-title").get_text()  # fetching auther name
        
        # fethcing initials of author
        authorInitials = ""
        for name in authorName.split():
            authorInitials = authorInitials + str(name[0]) + '. '
        
        authorDOB = soup.find('span', class_='author-born-date').get_text()     # fetching author's date of birth
        authorBirthPlace = soup.find('span', class_='author-born-location').get_text()     # fetching author's palce of birth
        authorNameLength = [len(authorName.split()[0]), len(authorName.split()[1])]     # getting total characters in author's 1st and last name and storing as a list

        #  appenind fetched author details in the diction with author name as key and details and value of key
        author_dict[authorName] = [authorName, authorInitials, authorDOB, authorBirthPlace, authorNameLength, [quotes_count]]


def guess_check(quote_numb, guess):
    """ Used to check if user has guessed right answer or not. Tru if he has guess it right, else false
        
        Args:
            quote_numb (int): key of the quote_dict ductionay
            guess (str): user guess
    """
    if guess.lower().replace(' ', '').replace('.', '') == quote_dict[quote_numb]['author'].lower().replace(' ', '').replace('.', ''):
        return True
    else:
        return False


def ask_for_guess(query, hint, random_quote_numb):
    """ Method that promts message to the user, takes his input, checks if the guess is right and accoring to the result of check returns True or False

        Args:
            query (str): query that will we displayed to user.
            hint (str): hint that will we displayed to user.
            random_quote_numb (int): key of the quote_dict dictionary
    """

    print(query)
    
    if not hint == '':  # not to be printed for the very 1st call
        print(f'\nHere is a small hint for you. \"{hint}\"')
    
    guess = input('Now take a guess: ')     # asking for user guess

    result = guess_check(random_quote_numb, guess)  # calling function guess_check to know if guess is correct or not. 
    
    # if user guess correctly
    if result == True:
        print('\nBingo... You hits the bull\'s eye.')
        flag = True
    # if user guess is not correct
    else:
        flag = False

    return flag        


def game():
    """ This is where actual game begins.

        Args:
    """
    random_quote_numb = randint(1, len(quote_dict))     # generating random number depending on the number of quotes in quote_dict dictionary
    
    guess_remain = 4    #number of guess user has
    
    random_quote = quote_dict[random_quote_numb]['quote']   # fetching a quote from quote_dict dictionary with key as random number generated before
    quote_author = quote_dict[random_quote_numb]['author']  # fetching a author of quote from quote_dict dictionary with key as random number generated before

    # fetching author details form author_dict to be used as hints when user gives wrongs answer
    hint1_DOB = 'Author was born on ' + author_dict[quote_author][2] + ' ' + author_dict[quote_author][3] + '.'
    hint2_initials = 'Author\'s initials are ' + author_dict[quote_author][1]
    hint3_lastname_len = f'Author\'s last name has {author_dict[quote_author][4][1]} characters.'

    hint = [hint3_lastname_len, hint2_initials, hint1_DOB, '']  # list of all the hints. Last hint is blank as we dont want to give any hint during user's 1st guess

    print(f'\n{random_quote}\n\nPlease enter author of Quote.')     # pritning quote
    flag = False
    
    while flag == False:
        if guess_remain == 4:   # to be executed only during 1st call
            query = f'You have {guess_remain} guess remaining.'
        else:
            query = f'\nOpps.. Thats not the correct answer.\nBut dont worry. You still got {guess_remain} guess.'
        
        flag = ask_for_guess(query, hint[guess_remain-1], random_quote_numb)    # calling function ask_for_guess(0 to get the result of user's guess)
        
        # if user guessed correctly
        if flag == True:
            pass
        # if user guessed wrong
        else:
            guess_remain = guess_remain - 1     # user looses a guess chance
            if guess_remain == 0:   # if user has use all his guess chance
                print(f'\nOpps.. Thats not the correct answer.\nSorry. You have exhausted all your guessing chance.\nCorrect answer is {quote_author}\n')
                break


base_url = 'http://quotes.toscrape.com'
url = 'http://quotes.toscrape.com'

quote_dict = {}     # dictionary that holds all quotes
author_dict = {}     # dictionary that holds all authors
quotes_count = 0    # count of quotes fetched and also keys of quote_dict dictionary
page_count = 1      

flag = True

# fetching data from http://quotes.toscrape.com
while flag:
    
    resp = requests_quotes(url)     # fetching data
    
    if resp.status_code == 200:     # to be executed if url reaches desired location

        soup = BeautifulSoup(resp.text, 'html.parser')
        quote_divs = soup.find_all('div', class_='quote')   # fetching all div tags having quotes
        
        if len(quote_divs) > 0 :    # if we have more then 0 dic tags in the data fetched from url

            for quote_div in quote_divs:    # looping through dic tags 

                quotes_count = quotes_count + 1     # increaing count of quotes with every loop
                
                quote = quote_div.find('span', class_="text").get_text()    # fetching quote
                author = quote_div.find('small', class_='author').get_text()    # fetching author

                # if author_dict dictionary has the author then append quote number to the list
                # (author_dict dictionary) having keys of quote_dict dictionary for that particular author.
                if author in author_dict:
                    author_dict[author][5].append(quotes_count)
                #else create a new author in author_dict dictionary 
                else:
                    author_bio_link = base_url + quote_div.a['href']
                    author_details(author_bio_link, quotes_count)

                # adding quotes and author name to the quote_dict dictionary with quote number as the key.
                quote_dict[quotes_count] = {'quote': quote, 'author': author}

            page_count = page_count + 1     # increaing page number by 1
            url = base_url + '/page/' + str(page_count)     # generating a new url for next page from which the data is to be fetched

        else:   # if page from which data is fetchd has no desired div tags taht conatin quotes
            flag = False

    else:   # if response code is not 200
        flag = False

# run game
while True:
    game()
    if not input("\nPress 1 if you wanna continue or anyother key to quit: ") == '1':
        break