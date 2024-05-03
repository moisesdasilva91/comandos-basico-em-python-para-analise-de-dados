import pandas as pd #conferir a biblioteca Pandas https://pandas.pydata.org/
import numpy as np #conferir a bibiloteca Numpy https://numpy.org/
import seaborn as sns #conferir a biblioteca seaborn https://seaborn.pydata.org/introduction.html
import matplotlib.pyplot as plt #conferir a biblioteca matplotlib https://matplotlib.org

dic = {"coluna 1": ['linha1', 'linha2', 'linha3'], "coluna2": ['linha1', 'linha2', 'linha3']}
tabela = pd.DataFrame(dic)
#importando base de dados (df = dataframe)
df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv')
print(df.head(10))
print(df.shape) #mostra quantas linhas e colunas a importação possui
print(df.info) #mostra as primeiras 5 linhas e colunas e as 5 ultimas
print(df.describe()) #resumo estatistico
print(df.isnull().sum()) #dados das tabelas que são nulos
print(df.isnull().sum() / len(df) *100) #transformando os dados nulos em porcentagem 
print(df['country']) #puxando alguma coluna em especifico atraves do nome
print(df['country'][:10]) #puxando alguma coluna em especifico, colocando como parametro as 10 primeiras colunas 
#Contar o quanto de cerveja bebem no mundo
print(df['beer_servings'].value_counts())
#Contar o quanto que bebem só de destilados no mundo
print(df['spirit_servings'].value_counts())
#Contar o quanto bebem de vinho ao redor do mundo
print(df['wine_servings'].value_counts())
#Contar o quanto bebem de alcool puro ao redor do mundo
print(df['total_litres_of_pure_alcohol'].value_counts())
#Arrumando em ordem crescente 
print(df['total_litres_of_pure_alcohol'].value_counts().sort_values())
#Quanto consomem de alcool só no Brasil
brasil = df[df['country']=='Brazil']
print(brasil)
#plotando um grafico a partir do nosso dataset
sns.countplot(df['total_litres_of_pure_alcohol'])
plt.ylabel('Consumo de alcool por pais')
plt.show()
#Vamos diminuir o grafico colocando apenas os paises com consumo maior ou igual a 7 litros
consumo = df[df['total_litres_of_pure_alcohol'] >= 7]
print(consumo.head(10))
#Criar um grafico apenas com nosso subset consumo
sns.countplot(consumo['total_litres_of_pure_alcohol'])
plt.ylabel('Porcentagem de consumo')
plt.show()