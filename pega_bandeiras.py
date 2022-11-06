import requests
import sqlite3
from playwright.sync_api import sync_playwright
from time import sleep
import os
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.62 Safari/537.36'}


def lista():
    url = 'https://pt.ucoin.net/catalog'

    with sync_playwright() as p:
        browser = p.chromium.launch(channel='chrome')
        page = browser.new_page()
        page.goto(url)
        html = page.content()

        soup = BeautifulSoup(html, 'html.parser', from_encoding='UTF-8')

        paises = soup.find_all('li', class_='cntry')
        with open('lista_paises.txt', 'w', encoding='utf-8') as f:
            for pais in paises:
                xnome = BeautifulSoup(str(pais), 'html.parser')
                nome = xnome.find('a').get('title').replace(
                    'Catálogo de Moedas - ', '')
                url = 'https://pt.ucoin.net'+xnome.find('a').get('href')

                session = requests.Session()
                response = session.get(url, headers=headers)
                soup = BeautifulSoup(
                    response.text, 'html.parser', from_encoding='utf-8')
                band = soup.find('img', class_='flg')
                print(band)
                f.write(f'{nome},https://pt.ucoin.net{band}\n')
        browser.close()


lista()
