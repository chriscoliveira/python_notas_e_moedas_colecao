import collections

pais = ['dinamarca', 'brasil']
repetido = ['EUA', 'brasil', 'brasil', 'dinamarca', 'brasil', 'dinamarca']

resultado = collections.Counter(repetido)
for v in range(len(pais)):
    print(f'{pais[v]} - {resultado[pais[v]]}')
