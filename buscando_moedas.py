# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


def baixar(url, nome):
    with open('fotos/' + nome, 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print
            response

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


def buscar(url):
    colecao = []
    req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(req.content, 'html.parser')
    itens = soup.find_all('div', class_='coin')
    arquivo = open('resultado.txt', 'a')

    for item in itens:
        try:
            pais = item.find('a', class_='blue-15').text
            pais = pais.split('\xa0')
            ano = pais[2]
            moeda = pais[1]
            pais = pais[0]
        except:
            pais = ''

        try:
            desc = item.find('div', class_='desc').text
            desc = desc.split('\xa0')
            material = desc[0]
            peso = desc[1]
            diametro = desc[2]
        except:
            desc = ''

        try:
            marca = item.find('div', class_='gray-13').text
        except Exception as e:
            marca = ''

        try:
            assunto = item.find('div', class_='dgray-13').next_element
        except Exception as e:
            assunto = ''
        try:
            valor = item.find('a', class_='blue-12').text
            valor = valor.replace('€ ', '')
            valor = float(valor) * 6.97
            valor = round(valor, 2)
        except Exception as e:
            valor = ''
        fotos = []
        try:
            krause = item.find('div', class_='gray-11').text
            krause = krause.split('·')
            circulacao = krause[0]
            krause = krause[1]
        except:
            krause = ''

        contador = 0
        # for imgs in item.find_all('td', class_='coin-img'):
        #     for img in imgs.find_all('img'):
        #         if contador == 0:
        #             baixar(img['src'], pais + '_1.jpg')
        #             contador += 1
        #         else:
        #             baixar(img['src'], pais + '_2.jpg')
        #             contador = 0

        print(
            f'Pais {pais}\nAno {ano}\nMoeda {moeda}\nCunhagem {marca}\nMaterial {material}\nPeso {peso}\n'
            f'Diametro {diametro}\nInfo {assunto}\nValor Venda R${valor}\nCatalogo {krause}\nCirculacao {circulacao}')
        print('-' * 40)
        # arquivo.write(f'Pais : {pais}\n'
        #               f'marca {marca}\n'
        #               f'Desc : {desc}\n'
        #               f':{assunto}\n'
        #               f'valor: {valor}\n'
        #               f'Krause {krause}\n\n')
    arquivo.close()


if __name__ == '__main__':
    buscar('https://pt.ucoin.net/gallery/?uid=26638&page=0')
    # for i in range(100):
    #     buscar('https://pt.ucoin.net/gallery/?uid=26638&page=' + str(i))
    #     print('https://pt.ucoin.net/gallery/?uid=26638&page=' + str(i))
