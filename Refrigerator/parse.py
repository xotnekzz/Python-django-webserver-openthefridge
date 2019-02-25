import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Refrigerator_Sever.settings")

import django
django.setup()
import requests
# HTTP GET Request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from Refrigerator.models import Recipe

def parse_recipe():
    #pageNumber = 1
    #strPageNumber = str(pageNumber)
    #list_url = "http://board.miznet.daum.net/gaia/do/cook/recipe/mizr/list?pageIndex="+ strPageNumber +"&bbsId=MC001"
    #html = requests.get(list_url).text
    #soup = BeautifulSoup(html, 'html.parser')

    pageNumber = 10
    number = 1
    menu_list = []
    for i in range(1,151):
        strPageNumber = str(i)
        list_url = "http://board.miznet.daum.net/gaia/do/cook/recipe/mizr/list?pageIndex=" + strPageNumber + "&bbsId=MC001"
        html = requests.get(list_url).text
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.select("#page_body > div.body_center > form > ul > li"):
            a_tag = tag.select('div p a')[0]
            name = a_tag.text
            detail_url = urljoin(list_url, a_tag['href'])
            img_url = tag.select('a img')[0]['src'].strip()
            menu_list.append([name, detail_url, img_url])

    return  menu_list






