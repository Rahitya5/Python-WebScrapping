from bs4 import BeautifulSoup
import requests
import time
import os
 
print('put some skill that you are not familiar with')
unfamiliar_skill = input('> ').lower().strip()
print(f'Filtering out {unfamiliar_skill}')
 
#ensure the 'posts' directory exists
 
if not os.path.exists('posts'):
    os.makedirs('posts')
 
#to get specific information from the website
def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    for index, job in enumerate(jobs):
        posted_time = job.find('span', class_ = 'sim-posted').span.get_text(strip=True)
        if 'few' in posted_time:
            company_name = job.find('h3', class_ = 'joblist-comp-name').get_text(strip=True)
            skills = job.find('div', class_ = 'more-skills-sections').get_text(strip=True).lower()
            more_info = job.header.h2.a['href']
            if unfamiliar_skill not in skills:
                with open(f'posts/{index}.txt','w') as f:
 
                    f.write(f"Comapany Name: {company_name}\n")
                    f.write(f"Required Skills: {skills}\n")
                    f.write(f"More Information: {more_info}\n")
                    f.write(f"Posted Time: {posted_time}\n")
                print(f'File Saved: {index}')
 
if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)