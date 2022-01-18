# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def buscar(url):
    colecao = []
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    itens = soup.find_all('div', class_='coin')
    with open('resultado.txt', 'a', encoding='utf-8') as arquivo:

        for item in itens:
            try:
                pais = item.find('a', class_='blue-15').text
                pais = pais.split('\xa0')
                ano = pais[2]
                moeda = pais[1]
                pais = pais[0]
            except:
                pais = ''

            fotos = []

            try:
                krause = item.find('div', class_='gray-11').text
                krause = krause.split('·')

                krause = krause[1]
            except:
                krause = ''

            contador = 0
            for imgs in item.find_all('td', class_='coin-img'):

                for img in imgs.find_all('img'):
                    fotos.append(img['src'])

                    if contador == 0:
                        imagem1 = img['src']
                        contador += 1
                    else:
                        imagem2 = img['src']
                        contador = 0

            arquivo.write(
                f'{pais};{ano};{krause};{fotos}\n')


if __name__ == '__main__':
    buscar('https://pt.ucoin.net/gallery/?uid=26638&page=110')
