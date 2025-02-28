from playwright.async_api import async_playwright

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from re import match, sub

from utils.redis import set_cache, get_cache

def date_parse(string: str):
    string = string.lower()
    regex = match(r'publicado: há (\d+) (\w+)', string)

    if regex:
        amount = int(regex.group(1))
        unit = regex.group(2)
        if unit.endswith('s'): unit = unit[:-1]

        hours = amount
        if unit != 'hora': hours *= 24
        if unit == 'semana': hours *= 7

        date = datetime.now() - timedelta(hours = hours)
        return int(date.timestamp())

    days_back = timedelta(days = 1) if 'Ontem' in string else timedelta(days = 0)

    date = datetime.now() - days_back
    return int(date.timestamp())
    

mounths = {
    'janeiro': 'January',
    'fevereiro': 'February',
    'março': 'March',
    'abril': 'April',
    'maio': 'May',
    'junho': 'June',
    'julho': 'July',
    'agosto': 'August',
    'setembro': 'September',
    'outubro': 'October',
    'novembro': 'November',
    'dezembro': 'December'
}

def translate(date: str):
    for pt, en in mounths.items():
        date = date.replace(pt, en)

    return date

url = 'https://www.workana.com'

async def workana_crawler():
    data = get_cache('workana')
    if data:
        print('cache')
        return data

    data = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless = True)
        page = await browser.new_page()

        await page.goto(f'{url}/pt/jobs?category=it-programming&language=pt&page=1')

        await page.click('button#onetrust-accept-btn-handler')

        html = await page.content()

        soup = BeautifulSoup(html, 'html.parser')
        projects = soup.find_all('div', class_ = 'project-item')

        for project in projects:
            job = {}
            element = project.find('h2', class_ = 'project-title')

            job['title'] = element.text.strip()
            job['link'] = url + element.find('a').get('href').strip().replace('?ref=projects_1', '')

            element_description = project.find('div', class_ = 'project-details')
            description = element_description.find('span').text.strip()
            job['description'] = sub(r'Categoria:.*', '', description)

            time = project.find('span', class_ = 'date').text
            time = translate(time)
            job['timestamp'] = date_parse(time)


            data.append(job)

    set_cache('workana', data)
    print('save cache')
    return data
