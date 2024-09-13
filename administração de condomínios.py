##Projeto: administração de condomínios##

#desafio 1: abrir a base de dados com Pandas e aplicar o json_normalize.


import pandas as pd


dados = pd.read_json('dados_locacao_imoveis.json')
dados.head(5)

dados = pd.json_normalize(dados['dados_locacao'])
dados

#Desafio 2:

## Remover os dados em listas dentro do DataFrame;
colunas = list(dados.columns)
colunas

dados = dados.explode(colunas[1:])
dados

dados.reset_index(drop=True,inplace=True)

#Verificar os tipos de dados;
dados.info()

#Identificar colunas numéricas;
coluna_numerica = 'valor aluguel'

#Transformar a coluna numérica para o tipo numérico.

import numpy as np
dados['valor_aluguel'] = dados['valor_aluguel'].apply(lambda x: x.replace('$ ', '').replace(' reais', '').replace(',','.').strip())
dados['valor_aluguel'] = dados['valor_aluguel'].astype(np.float64)

dados.info()
dados

#Desafio 3: Manipule os textos na coluna apartamento para remover o texto (blocoAP) do DataFrame.

dados.head(4)

dados['apartamento'] = dados['apartamento'].str.replace('(blocoAP)','',regex=True)
dados['apartamento'] = dados['apartamento'].str.replace('[()]','',regex=True)
dados.head(5)

#Desafio 4: Nas colunas datas_de_pagamento e datas_combinadas_pagamento, temos datas em formato 'dia/mês/ano' (dd/mm/AAAA). Transforme esses dados para o tipo datetime e busque uma forma de visualização de subconjunto que possa contribuir no objetivo do contexto que os dados estão inseridos.

dados.head(3)

dados['datas_combinadas_pagamento'] = pd.to_datetime(dados['datas_combinadas_pagamento'], format='%d/%m/%Y')
dados['datas_de_pagamento'] = pd.to_datetime(dados['datas_de_pagamento'],format='%d/%m/%Y')


#Desafio 5: Saber a media de atraso do pagamento do aluguel

dados['atraso'] = (dados['datas_de_pagamento'] - dados['datas_combinadas_pagamento']).dt.days

dados

media_de_atraso = dados.groupby(['apartamento'])['atraso'].mean()

media_de_atraso