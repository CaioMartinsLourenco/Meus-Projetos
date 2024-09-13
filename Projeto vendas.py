##Projeto: vendas online##

#desafio 1: abrir a base de dados com Pandas e aplicar o json_normalize.

import pandas as pd
import numpy as np

dados = pd.read_json('C:\\Users\\caiom\\Desktop\\Projetos\\dados_vendas_clientes.json')
dados.head(5)

dados = pd.json_normalize(dados['dados_vendas'])
dados


#Desafio 2:


# Remover os dados em listas dentro do DataFrame;
colunas = list(dados.columns)
colunas

dados = dados.explode(colunas[1:])
dados.reset_index(drop=True,inplace=True)
dados

#Verificar os tipos de dados;
dados.info()

#Identificar colunas numéricas;
coluna_numerica =['Valor da compra']
coluna_numerica

#Transformar a coluna numérica para o tipo numérico.
import numpy as np
dados['Valor da compra'] = dados['Valor da compra'].apply(lambda x: x.replace('R','').replace('$','').replace(',','').strip())
dados['Valor da compra'] = dados['Valor da compra'].astype(np.float64)

dados.info()
dados

#Desafio 3:manipule os textos presentes na coluna Cliente para que seja obtido como resultado os nomes dos clientes em letras minúsculas, com a ausência de caracteres especiais ou números.
dados.head(5)

dados['Cliente']= dados['Cliente'].str.lower()
dados.head(4)

dados['Cliente'] = dados['Cliente'].str.replace('[^a-z^]','',regex=True)
dados.head(4)

#Desafio 4: Na coluna Data de venda, temos datas em formato 'dia/mês/ano' (dd/mm/AAAA). Transforme esses dados para o tipo datetime e busque uma forma de visualização de subconjunto que possa contribuir no objetivo do contexto que os dados estão inseridos.

dados['Data de venda'] = pd.to_datetime(dados['Data de venda'],format='%d/%m/%Y')

dados.head(500)

#Desafio 5: Saber quais foram os clientes que mais gastaram
total_compras = dados.groupby(['Cliente'])['Valor da compra'].sum()

total_compras



