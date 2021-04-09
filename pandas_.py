import pandas as pd

df = pd.read_csv('bancoNotas.csv',usecols=['pais','ano','krause','valor','moeda','qualidade','diametro'])
print(df.head())
print('#'*30)
print(df.info())
print('#'*30)
print(df.loc[[1,2,3],['pais','ano','krause','valor','moeda']])

print(df.query('pais=="Brasil"').head(10))