#!/usr/bin/env python3
 
import json
import os

with open('jobs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

jobs_per_page = 10
max_page = (len(data) + jobs_per_page - 1) // jobs_per_page

output_dir = 'scraping_practice_site'
if not os.path.exists(output_dir):
    os.mkdir(output_dir)


for page in range(1, max_page+1):

    header = f'''
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Scraping Practice {page}</title>
        <link rel="stylesheet" href="../style.css">
    </head>
    <body>
        <div class="main">

            <h1>Scraping Practice</h1>

            <p class="caution">
                Pythonスクレイピングの練習用サイトです。<br>
                実際に存在する求人情報ではありません！！
            </p>

            <div class="container">
    '''

    card = ''
    start = (page - 1) * jobs_per_page
    end = start + jobs_per_page

    for job in data[start:end]:
        title = job['title']
        company = job['company']
        location = job['location']
        salary = job['salary']
        status = job['status']
        industry = job['industry']
        description = job['description']
        link = job['link']

        card += f'''
                <a href="{link}" class="jobsearch-card-link" target="_blank" rel="noopener noreferrer">
                    <div class="jobsearch-card">
                        <div class="employment-status">{status}</div>
                        <div class="jobsearch-header">
                            <h2 id="JobInfoHeader-title" class="jobsearch-title">{title}</h2>
                            <span class="description">{description}</span>
                        </div>
                        <div class="jobsearch-details">
                            <div class="jobsearch-location">
                                <span>勤務地所在地:</span> {location}
                            </div>
                            <div class="jobsearch-industry">
                                <span>職種:</span> {industry}
                            </div>
                            <div class="jobsearch-employment">
                                <span>雇用形態:</span> {status}
                            </div>
                            <div class="jobsearch-salary">
                                <span>給与:</span> {salary}
                            </div>
                            <div class="jobsearch-company">
                                <span>企業名:</span> {company}
                            </div>
                        </div>
                    </div>
                </a>
        '''

    footer = f'''
            </div>

            <div class="pagenator">
    '''

    for j in range (1, max_page+1):
        if page == j:
            current_class = "current-page"
        else:
            current_class = ''

        footer += f'''
            <a href="page{j}.html">
                <div class="pagenator-num {current_class}"><span>{j}</span></div>
            </a>
            '''
    
    footer += '''         
            </div>

        </div> 
    </body>
    </html>
    '''

    html = header + card + footer

    file_name = f'''{output_dir}/page{page}.html'''

    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html)


