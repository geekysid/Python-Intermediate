from bs4 import BeautifulSoup
import requests, json, csv

page = 1
url = 'https://www.rithmschool.com/blog'


with open('rithmSchoolBlog.csv', 'w') as csv_file:
    
    writer = csv.writer(csv_file)
    writer.writerow(['SL. No''Heading', 'Blog Link', 'Desc', 'Date'])
    blogCounter = 0
    while True:
        params = f'page={page}'

        resp = requests.get(url, params=params)

        # print(f"\nPAGE: {page}\n")

        soup = BeautifulSoup(resp.text, 'html.parser')

        blog_posts = soup.find_all('article')

        if(len(blog_posts) > 0):

            for post in blog_posts:

                post_heading = post.find('h4', class_='section-heading').text.replace('\n', '').strip()
                post_link = url + post.h4.a.attrs['href']

                post_desc = ""
                paras = post.find_all('p')
                for para in paras:
                    post_desc = post_desc + '\n' + para.get_text().replace('\n', '').strip()

                post_date = post.find('h4', class_='service-heading').get_text()

                blogCounter = blogCounter + 1
                csv_data = [blogCounter, post_heading, post_link, post_desc, post_date]
                writer.writerow(csv_data)

            page = page + 1 

        else:
            break