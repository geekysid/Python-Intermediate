# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#   Name: Siddhant Shah                                         #
#   Date: 18/02/2020                                            #
#   Desc: Scraping a website (offstagejobs.com) and storing     #
#         data in a csv                                         #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import requests
from bs4 import BeautifulSoup
import time
import csv
import time


url = 'http://offstagejobs.com/jobs.php'    # link to scrape
post_data = {
        'MIME Type': 'application/x-www-form-urlencoded',
        'selectRegionID': '',
        'selectDeptID': '',
        'selectJobClassID': '',
        'sortQueryID': '1',
        'postedDate': '01-01-1990',
        'page': '-1',
        'query_check': 'Search'
    }

# job_count = 0
resp = requests.post(url, data=post_data)
# print(resp.status_code)
# print(resp.text)

start_time = time.time()

soup = BeautifulSoup(resp.text, 'html.parser')
jobs = soup.find('table', id='Content').find_all('tr')

#list that hold dictionary of data scraped
job_dict_list = []

# fetching 1st 1001 jobs
for job in jobs[2:1003]:
    
    # job_count = job_count + 1

    # print(f'Started Reading Job # {job_count}')
    try:
        post = job.find('div', class_='itemh1').get_text().strip()
        # print(f'post: {post}')
    except:
        # print('Post field for this job seems to be Empty')
        post = ''

    try:
        company = job.find('div', class_='itemh2').get_text().strip()
        # print(f'company: {company}')
    except:
        # print('Company field for this job seems to be Empty')
        company = ''
        
    try:
        event = job.find('div', class_='itemh3').get_text().strip('  ').strip()
        # print(f'event: {event}')
    except:
        # print('Post field for this job seems to be Empty')
        event = ''
        
    try:
        expires = job.find('div', class_='itemDate').get_text().strip('Expires: ').strip()
        # print(f'expires: {expires}')
    except:
        # print('Expiry field for this job seems to be Empty')
        expires = ''

    try: 
        date_pay = job.find_all('div', class_='itemd1')
            
        try:
            job_dates = date_pay[0].p.get_text().strip()
            # print(f'job_dates: {job_dates}')
        except:
            # print('job Date field for this job seems to be Empty')
            job_dates= ''
            
        try:
            pay = date_pay[1].p.get_text().strip()
            # print(f'pay: {pay}')
        except:
            # print('Pay field for this job seems to be Empty')
            pay = ''
    except:
        # print('Pay a,d Job Date field for this job seems to be Empty')
        pay, job_dates = ''

        
    try:
        description = job.find('div', class_='itemDescr').p.get_text().strip()
        # print(f'description: {description}')
    except:
        # print('Job Description field for this job seems to be Empty')
        description = ''
    
    try:
        contact = job.find('div', class_='itemContact')

        try:
            contact_name_tag = contact.h4
            contact_name = contact_name_tag.get_text().strip()
            # print(f'contact_name: {contact_name}')
        except:
            # print('Contact Name field for this job seems to be Empty')
            contact_name = ''
            
        try:
            contact_designation_tag = contact_name_tag.next_sibling
            contact_designation = contact_designation_tag.get_text().strip()
            # print(f'contact_designation: {contact_designation}')
        except:
            # print('Contact Designation field for this job seems to be Empty')
            contact_designation = ''
            
        try:
            contact_email_tag = contact_designation_tag.next_sibling
            contact_email = contact_email_tag.get_text().strip()
            # print(f'contact_email: {contact_email}')
        except:
            # print('Contact Email field for this job seems to be Empty')
            contact_email = ''
            
        try:
            contact_website_tag = contact_email_tag.next_sibling
            contact_website = contact_website_tag.get_text().strip()
            # print(f'contact_website: {contact_website}')
        except:
            # print('Contact Website field for this job seems to be Empty')
            contact_website = ''
    except:
        # print('Contact Information for this job seems to be Empty')
        contact_website, contact_email, contact_designation, contact_name = ''
        
    try:
        business_address_paras = job.find('div', class_='itemVenue').find_all('p')
        business_address = ''
        for para in business_address_paras:
            business_address += para.get_text().strip()
        # print(f'business_address: {business_address}')
    except:
        # print('Address field for this job seems to be Empty')
        business_address = ''

    try:
        job_categories = job.find('div', class_='itemDetailLink').p.get_text().strip()
        if 'Report this Listing for abuse' in job_categories:
            # print('Job Category field for this job seems to be Empty')
            job_categories = ''
        else:
            # print(f'job_categories: {job_categories}')
            pass
    except:
        # print('Job Category field for this job seems to be Empty')
        job_categories = ''

    try:
        job_post_date_h3s = job.find('div', class_='itemDetailLink').find_all('h3')

        try:
            job_post_date = job_post_date_h3s[0].get_text().replace('Posted: ', '').strip()
            # print(f'job_post_date: {job_post_date}')
        except:
            # print('Post Date field for this job seems to be Empty')
            job_post_date = ''

        try:
            job_last_update = job_post_date_h3s[1].get_text().replace('Last Updated: ', '').strip()
            # print(f'job_last_update: {job_last_update}')
        except:
            # print('Last Update field for this job seems to be Empty')
            job_last_update = ''

        try:
            job_trackback = job_post_date_h3s[2].get_text().replace('Trackback: ', '').strip()
            # print(f'job_trackback: {job_trackback}')
        except:
            # print('Job Traceback field for this job seems to be Empty')
            job_trackback = ''
    except:
        # print('Job Post Date, Last Update, Traceback field for this job seems to be Empty')
        job_trackback = ''
        job_last_update = ''
        job_post_date = ''

    # creating dictioanry of data scraped for current job
    job_dict = {
        'post': post,
        'company': company,
        'event': event,
        'expires': expires,
        'job_dates': job_dates,
        'pay': pay,
        'description': description,
        'contact_name': contact_name,
        'contact_designation': contact_designation,
        'contact_email': contact_email,
        'contact_website': contact_website,
        'business_address': business_address,
        'job_categories': job_categories,
        'job_post_date': job_post_date,
        'job_last_update': job_last_update,
        'job_trackback': job_trackback
    }

    # adding dictionary of current job to the list
    job_dict_list.append(job_dict)

    # print(f'Added Job # {job_count} to List')

# creatimng list that will be used as csv header
csv_headers = []
for key in job_dict_list[0]:
    csv_headers.append(key)

# entry_count = 1

# creating a new csv and storing scraped data
with open(f'offstagejobs.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()

    for jobs in job_dict_list:
        writer.writerow(jobs)

        # print(f'*****JOB # {entry_count} DETAILS*****\n')

        # for job in jobs:
        #     print(f'{job} : {jobs[job]}')
        # print(f'Added Job # {entry_count} to CSV')
    
        # print('='*50 + '\n')

        # entry_count = entry_count + 1


end_time = time.time()

print(f'Total scraping and creating csv took {end_time - start_time} secs')
