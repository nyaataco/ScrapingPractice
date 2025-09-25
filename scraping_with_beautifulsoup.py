#!/usr/bin/env python3
# scraping_with_beautifulsoup.py - Beautiful Soupを使ったスクレイピング
#
# このスクリプトは、GitHub Pagesで公開された練習用の静的サイトを対象にしています。
# ページは `page1.html`, `page2.html`, ... のように連番で構成されており、
# ページの途中に抜けはない（例: page3.html が存在しないなどのケースはない）ことを前提としています。
# ページが存在しない場合（404エラー）でループを終了します。


import requests, os, bs4, openpyxl, time

url = 'https://nyaataco.github.io/scraping_practice_site/'

output_dir = 'output'
output_file = 'output_bs4.xlsx'

title_font_style = openpyxl.styles.Font(size=20, bold=True)
header_fill = openpyxl.styles.PatternFill(start_color='CCE5FF', end_color='CCE5FF', fill_type='solid')
header_font_size = openpyxl.styles.Font(bold=True)
header_alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')

os.makedirs(output_dir, exist_ok=True)

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = 'JobList'
sheet['A1'] = 'スクレイピングした情報一覧'
sheet['A1'].font = title_font_style
sheet.row_dimensions[1].height = 30
sheet.row_dimensions[3].height = 22
sheet['A3'] = '求人タイトル'
sheet['B3'] = '説明'
sheet['C3'] = '職種'
sheet['D3'] = '雇用形態'
sheet['E3'] = '給与'
sheet['F3'] = '企業名'
sheet['G3'] = '所在地'
sheet['H3'] = 'リンク'



i = 1
row = 4
while True:
    try:
        print(f'page{i}をダウンロード中...')
        res = requests.get(url + f'/page{i}.html')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        card = soup.select('.jobsearch-card-link')

        for info in card:
            status_tag = info.select_one('.employment-status')
            title_tag = info.select_one('.jobsearch-title')
            description_tag = info.select_one('.description')
            location_tag = info.select_one('.jobsearch-location')
            industry_tag = info.select_one('.jobsearch-industry')
            salary_tag = info.select_one('.jobsearch-salary')
            company_tag = info.select_one('.jobsearch-company')

            link = info['href'] if info.has_attr('href') else ''
            status = status_tag.get_text().strip() if status_tag else ''
            title = title_tag.get_text().strip() if title_tag else ''
            description = description_tag.get_text().strip() if description_tag else ''
            location = location_tag.get_text().replace('勤務地所在地:', '').strip() if location_tag else ''
            industry = industry_tag.get_text().replace('職種:', '').strip() if industry_tag else ''
            salary = salary_tag.get_text().replace('給与:', '').strip() if salary_tag else ''
            company = company_tag.get_text().replace('企業名:', '').strip() if company_tag else ''

            sheet[f'A{row}'] = title
            sheet[f'B{row}'] = description
            sheet[f'C{row}'] = industry
            sheet[f'D{row}'] = status
            sheet[f'E{row}'] = salary
            sheet[f'F{row}'] = company
            sheet[f'G{row}'] = location
            sheet[f'H{row}'] = link

            row += 1

        i += 1
        time.sleep(1)
        
    except requests.exceptions.HTTPError as e:
        print(f'終了: 最後のページに到達しました。')
        break

    except requests.exceptions.RequestException as e:
        print(f'ネットワークエラーです。: ({e})')
        break



for cell in sheet[3]:
    cell.fill = header_fill
    cell.font = header_font_size
    cell.alignment = header_alignment
    sheet.column_dimensions[cell.column_letter].width = 25
    

for row in range(4, sheet.max_row + 1):
    sheet.row_dimensions[row].height = 20


wb.save( os.path.join(output_dir, output_file))
