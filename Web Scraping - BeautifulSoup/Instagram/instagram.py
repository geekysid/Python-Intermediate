# # # # # # # # # # # # # # # # # # # # #
#                                       #
#   Name: Siddhant Shah                 #
#   Date: 19/02/2020                    #
#   Desc: Instragram Hashtag Fetcher    #
#                                       #
# # # # # # # # # # # # # # # # # # # # #

import requests
from urllib import request, parse, error
from bs4 import BeautifulSoup
import ssl, json
import time, csv
from random import choice


# FETCHING CREDENTIALS FROM FILE STARTS
def fetch_user_credentials():
    with open('userdetails.json', 'r') as cred:
        credentials = json.load(cred)

    username_list = credentials.keys()
    username = choice(list(username_list))
    password = credentials[username]
    
    return [username, password]
# FETCHING CREDENTIALS FROM FILE ENDS


# FETCHING SESSION ID STARTS
def fetch_session_id():
    credentials = fetch_user_credentials()

    # Repeating loop till we get a proper sessionid without ant error
    while True:
        try:
            url = 'https://www.instagram.com/accounts/login/'
            url_main = url + 'ajax/'
            csrf_resp = requests.get(url)
            auth = {'username': credentials[0], 'password': credentials[1]}
            headers = {
                    'origin': "https://www.instagram.com",
                    'x-instagram-ajax': "1",
                    'content-type': "application/x-www-form-urlencoded",
                    'accept': "*/*",
                    'x-requested-with': "XMLHttpRequest",
                    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
                    'x-csrftoken': csrf_resp.cookies['csrftoken'],
                    'referer': "https://www.instagram.com/accounts/login/",
                    'accept-encoding': "gzip, deflate, br",
                    'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                    'cookie': "fbm_124024574287414=base_domain=.instagram.com; ig_or=landscape-primary; ig_pr=1; ig_vw=1920; mid=Wcp3vAALAAGjSka8GEnPwijnia6-; rur=FTW; ig_vh=949; csrftoken="+csrf_resp.cookies['csrftoken']+"; fbsr_124024574287414=jSVsTpoGuOgZQB0vEP_X70hrO2-LlfD9EnUz9nwGTXo.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUMyM1FOT2ZwQU1oRVVudldzeGp1dHpwckEyODBLbUZseVo4VjVMMVVRVkJYbUVadHFyd25nekdtdzg2ejFTajRIYzVSWVRISHlvTjZXU29ScEdDZXB5RnRTMDloRXlLT3dXbU5uTTloQV9PTFE2VUI2ZFhPWW5Qa3pBNlNSZkFpSWZiU2N2anEyRFZna2FMdkdDWkRBQklCbElhYVAya2JNZzJBQW9fU0lzS3Z5NDhHRXB2RjFwQmdKOHNrdjltZWtYbFF1Z1dib040UXlzM2lwUTVfRUsxTjJUaHBpb3g1QUF2SDNpSVE2Qm1fdTFSeTZTVHFZMWR1M2NCSU5FRHpiZXRaRjFvSXY1MGJzLWFWQk4tcmFsVHY1dGE2VS13ajZCUXE0UlFEQjVHZEdqeDZpZkdlc0JsYnZvQUNlVFFJQ3pVSl9id1F1eGpyc0UxbEFzalRWZCIsImlzc3VlZF9hdCI6MTUxODg4NDA1MCwidXNlcl9pZCI6IjEwMDAyMzcyMDI5NTQyNyJ9",
                    'x-compress': "null",
                    'cache-control': "no-cache"
                }
            session_resp = requests.post(url_main,data=auth,headers=headers)
            session_id = session_resp.cookies['sessionid']
            return session_id
        except Exception as e:
            print(str(e))
            continue
# FETCHING SESSION ID ENDS


# FETCHING POST DATA ----- STARTS
def fetch_post_detail(post):
    indv_post = {}
    indv_post['post_id'] = post['node']['id']
    indv_post['time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(post['node']['taken_at_timestamp'])))
    indv_post['thumbnail'] = post['node']['thumbnail_src']
    indv_post['caption'] = post['node']['edge_media_to_caption']['edges'][0]['node']['text']
    indv_post['total_comments'] = post['node']['edge_media_to_comment']['count']
    indv_post['total_like'] = post['node']['edge_liked_by']['count']
    indv_post['is_video'] = post['node']['is_video']
    indv_post['user_id'] = post['node']['owner']['id']

    user_ids.add(indv_post['user_id'])

    return indv_post
# FETCHING POST DATA ----- ENDS


# FETCHING All POST ----- STARTS
def fetch_post_data(resp_json, page):
    post_counter = 1
    posts_list = resp_json['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['edges']
    
    for post in posts_list:
        all_posts.append(fetch_post_detail(post))
        post_counter = post_counter+1

        # # breaking after fetching 5 post
        # if post_counter > 50:
        #     break
# FETCHING ALL POST ----- ENDS


# FETCHING TOP POST ----- STARTS
def fetch_top_post_data(resp_json):
    top_post_list = resp_json['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_top_posts']['edges']
    for post in top_post_list:
        all_posts.append(fetch_post_detail(post))
        # pass
# FETCHING TOP POST ----- ENDS


# FETCHING QUERY_HASH & VARIABLE_DATA ----- STARTS
def fetch_queryHash(soup):
    hashquery_js = soup.select_one('script[src*="ConsumerLibCommons.js"]')['src']
    hashquery_js_url = 'https://www.instagram.com' + hashquery_js
    resp_hashquery = requests.get(hashquery_js_url)
    hash_query = resp_hashquery.text.split('e.FEED_QUERY_ID=')[1].split(',')[0].replace('\"', '')
    # print(f'Hash_Query: {hash_query}')
    return hash_query
    
# FETCHING QUERY_HASH & VARIABLE_DATA  ----- ENDS


# FETCHING RELATED TAGS ----- STARTS
def fetch_related_tags(resp_json):
    related_tags_list = resp_json['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_related_tags']['edges']
    related_tags = []
    for tag in related_tags_list:
        related_tags.append(tag['node']['name'])
# FETCHING RELATED TAGS ----- ENDS


# CREATE DUMMY USER ---- STARTS
def add_dummy_user(user_id):
    user = {}

    user['username'] = ''
    user['biography'] = ''
    user['profile_pic_url'] = ''
    user['media_count'] = ''
    user['follower_count'] = ''
    user['following_count'] = ''
    user['is_private'] = ''
    user['is_verified'] = ''
    user['external_url'] = ''
    user['city_name'] = ''
    user['zip'] = ''
    user['contact_phone_number'] = ''
    user['latitude'] = ''
    user['longitude'] = ''
    user['public_email'] = ''
    user['public_phone_country_code'] = ''
    user['public_phone_number'] = ''
    user['instagram_location_id'] = ''
    user['is_business'] = ''
    
    user_details[user_id] = user
# CREATE DUMMY USER ---- ENDS


# METHOD TO MAKE SURE NO ERROR OCCURES WHILE FETCHING USER DATA ----- STARTS
def user_data_exception_free(data_json, field):
    try:
        value = data_json[field]
    except:
        value = ''
    
    return value
# METHOD TO MAKE SURE NO ERROR OCCURES WHILE FETCHING USER DATA ----- ENDS


# FETCHING USER DETAILS FROM POST ----- STARTS
def fetch_user_data():
    user_count = 0

    sessionid = fetch_session_id()

    for user_id in user_ids:
        user_count = user_count + 1
        print('Fething User Detail')

        headers = {
                'origin': "https://www.instagram.com",
                'x-instagram-ajax': "1",
                'content-type': "application/x-www-form-urlencoded",
                'accept': "*/*",
                'x-requested-with': "XMLHttpRequest",
                'user-agent': "User-Agent: Instagram 9.5.1 (iPhone9,2; iOS 10_0_2; en_US; en-US; scale=2.61; 1080x1920) AppleWebKit/420+",
                'accept-encoding': "gzip, deflate, br",
                'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
                'cookie': "sessionid="+sessionid,
                'x-compress': "null",
                'cache-control': "no-cache"
            }

        try:
            resp_user = requests.get('https://i.instagram.com/api/v1/users/'+user_id+'/info/', headers=headers)
            user_json = resp_user.json()['user']
            
            if resp_user.status_code == 200:
                user = {}
                user['username'] = user_data_exception_free(user_json, 'username')
                user['biography'] = user_data_exception_free(user_json, 'biography')
                user['profile_pic_url'] = user_data_exception_free(user_json, 'profile_pic_url').replace('\u0026', '&')
                user['media_count'] = user_data_exception_free(user_json, 'media_count')
                user['follower_count'] = user_data_exception_free(user_json, 'follower_count')
                user['following_count'] = user_data_exception_free(user_json, 'following_count')
                user['is_private'] = user_data_exception_free(user_json, 'is_private')
                user['is_verified'] = user_data_exception_free(user_json, 'is_verified')
                user['external_url'] = user_data_exception_free(user_json, 'external_url')
                user['city_name'] = user_data_exception_free(user_json, 'city_name')
                user['zip'] = user_data_exception_free(user_json, 'zip')
                user['contact_phone_number'] = user_data_exception_free(user_json, 'contact_phone_number')
                user['latitude'] = user_data_exception_free(user_json, 'latitude')
                user['longitude'] = user_data_exception_free(user_json, 'longitude')
                user['public_email'] = user_data_exception_free(user_json, 'public_email')
                user['public_phone_country_code'] = user_data_exception_free(user_json, 'public_phone_country_code')
                user['public_phone_number'] = user_data_exception_free(user_json, 'public_phone_number')
                user['instagram_location_id'] = user_data_exception_free(user_json, 'instagram_location_id')
                user['is_business'] = user_data_exception_free(user_json, 'is_business')
                
                user_details[user_id] = user

                username = user['username']
                profile_pic = user['profile_pic_url']
                email = user['public_email']
                private = user['is_private']
                print('='*5, f'User with Username "{username}" Fetched')
                print(' '*5, '='*5, f'Email Address: {email}')
                print(' '*5, '='*5, f'Is Private: {private}')
                print(' '*5, '='*5, f'Profile Pic: {profile_pic}', '\n')
        
        except Exception as e:
            print(' '*5, '='*5, f'No Data retrived for userid: {user_id}')
            print(' '*5, '='*5, f'Error: {str(e)}', '\n')
            add_dummy_user(user_id)

        time.sleep(5) # pausing programm for 5 seconds before making another request to server

        if user_count > 3:
            sessionid = fetch_session_id()
# FETCHING USER DETAILS FROM POST ----- ENDS


# STORING DATA IN CSV FILE ----- STARTS
def save_data_to_csv():
    consolidated_data = []
    
    for post in all_posts:
        post_dict = post
        
        userid = post['user_id']
        user_dict = user_details[userid]

        consolidated_data.append({**post_dict, **user_dict})
    
    csv_header = [x for x in consolidated_data[0].keys()]
    filename = hashtag+'.csv'

    with open(filename, 'w') as file:
        writer = csv.DictWriter(file, fieldnames = csv_header)
        writer.writeheader()
        for data in consolidated_data:
            writer.writerow(data)
# STORING DATA IN CSV FILE ----- ENDS


# MAIN ----- STARTS
def main(url):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    next_page_flag = True
    page_count = 1

    while next_page_flag:
        print('='*5, f'Fetching Post from Page # {page_count}')
        response = request.urlopen(url, context = context)
        status_code = response.getcode()
        resp = response.read()
        print(' '*5, '='*5, f'URL: {hasgTag_url}')
        print(' '*10, '='*5, f'Response Code: {status_code}')

        if status_code == 200:
            try:
                soup = BeautifulSoup(resp, 'html.parser')
                scripts = soup.find_all('script', type='text/javascript')
                resp_script = scripts[3]
                resp_json = json.loads(resp_script.text.split(' = ', 1)[1].rstrip(';'))
                
                # hashtag_id = resp_json['entry_data']['TagPage'][0]['graphql']['hashtag']['id']

                fetch_post_data(resp_json, page_count)
                fetch_top_post_data(resp_json)
                
                # query_hash = fetch_queryHash(soup)

                # has_next_page = resp_json['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['has_next_page']
                break

                # if has_next_page == True:
                #     variable_after = resp_json['entry_data']['TagPage'][0]['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
                #     hasgTag_url = base_url+'/graphql/query/?query_hash='+query_hash+'&variables=%20{"tag_name":%20"'+hashtag+'","first":%203,"after":%20"'+variable_after+'"}'
                #     print(hasgTag_url)
                #     next_page_flag = True
                # else:
                #     fetch_related_tags(resp_json)
                #     next_page_flag = False
            except Exception as e:
                print(soup)
                print(str(e))

        page_count = page_count + 1

        if page_count > 3:
            break

        time.sleep(5)   # pausing programm for 5 seconds before making another request to server

    fetch_user_data()   # fetching user data by userid fecthed for each post

    save_data_to_csv()  # storing all our fetched data to csv
# MAIN ----- ENDS


start_time = time.time()

hashtag = 'championsleague'
base_url = 'https://www.instagram.com'
hasgTag_url = base_url + '/explore/tags/' + hashtag + '/'

user_ids = set()    # creating set of userid
user_details = {}   # dictionary that stores details of all user in the form of dictionary with user_id as key

hash_query = ''

all_posts = []      # list that stores details of all post in the form of dictionary
top_posts = []      # list that stores details of all top post in the form of dictionary

main(hasgTag_url)

end_time = time.time()

print('*'*50, '\n', f'Total Scraping Took : {end_time-start_time} seconds', '\n', '*'*50)

print()