#!/usr/bin/env python3
# scraping_with_selenium.py - Seleniumを使ったスクレイピング

# drivers/chromedriver.exeを使用しています。
#
# このスクリプトは、GitHub Pagesで公開された練習用の静的サイトを対象にしています。


import os, openpyxl, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver_path = os.path.join("drivers", "chromedriver.exe")

url = 'https://nyaataco.github.io/scraping_practice_site/page1.html'

output_dir = 'output'
output_file = 'output_selenium.xlsx'

title_font_style = openpyxl.styles.Font(size=20, bold=True)
header_fill = openpyxl.styles.PatternFill(start_color='CCE5FF', end_color='CCE5FF', fill_type='solid')
header_font_size = openpyxl.styles.Font(bold=True)
header_alignment = openpyxl.styles.Alignment(horizontal='center', vertical='center')
row = 4


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


def get_elements(url):
    try:
        service = Service(driver_path)
        browser = webdriver.Chrome(service=service)
        browser.get(url)

        return browser
    except:
        print('error')


count = 1
has_next = True

while has_next:
    # ページを取得
    print(f"ページを取得しています。: {url}")
    browser = get_elements(url)
    time.sleep(1)

    cards = browser.find_elements(by="class name", value="jobsearch-card-link")
    for card in cards:
        link = card.get_attribute("href")
        status = card.find_element(by="class name", value="employment-status").text
        title = card.find_element(by="class name", value="jobsearch-title").text
        description = card.find_element(by="class name", value="description").text
        location = card.find_element(by="class name", value="jobsearch-location").text
        industry = card.find_element(by="class name", value="jobsearch-industry").text
        salary = card.find_element(by="class name", value="jobsearch-salary").text
        company = card.find_element(by="class name", value="jobsearch-company").text

        sheet[f'A{row}'] = title
        sheet[f'B{row}'] = description
        sheet[f'C{row}'] = industry
        sheet[f'D{row}'] = status
        sheet[f'E{row}'] = salary
        sheet[f'F{row}'] = company
        sheet[f'G{row}'] = location
        sheet[f'H{row}'] = link

        row += 1

    # 次のページへのリンクを探す
    next_url = None
    pagenator = browser.find_element(by="class name", value="pagenator")
    pages = pagenator.find_elements(By.TAG_NAME, "a")

    for page in pages:
        div = page.find_element(by="class name", value="pagenator-num")
        classes = div.get_attribute("class")

        if "current-page" in classes:
            continue

        if int(page.text) > count:
            next_url = page.get_attribute("href")
            break

    if next_url:
        url = next_url
        count += 1
    else:
        has_next = False
        print("最後のページに到達しました。")
    

browser.quit()


for cell in sheet[3]:
    cell.fill = header_fill
    cell.font = header_font_size
    cell.alignment = header_alignment
    sheet.column_dimensions[cell.column_letter].width = 25
    

for row in range(4, sheet.max_row + 1):
    sheet.row_dimensions[row].height = 20


wb.save( os.path.join(output_dir, output_file))
