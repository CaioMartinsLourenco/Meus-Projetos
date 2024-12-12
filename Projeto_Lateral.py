
import pandas as pd
import openpyxl
import xlsxwriter



#Abrindo o DF
df = pd.read_csv('premier-player-23-24 (1).csv')
df

#Criando um DF de acordo com os filtros que o treinador solicitou 
df.info()
df.columns
colunas_a_remover = ['90s','Gls','G-PK', 'PK', 'PKatt', 'CrdY', 'CrdR', 'xG', 'npxG',
       'xAG', 'npxG+xAG', 'PrgC', 'PrgP', 'PrgR', 'Gls_90', 'Ast_90', 'G+A_90',
       'G-PK_90', 'G+A-PK_90', 'xG_90', 'xAG_90', 'xG+xAG_90', 'npxG_90',
       'npxG+xAG_90',]
df.drop(colunas_a_remover,axis=1,inplace=True,errors='ignore')
#Treinador optou por remover jogadores africanos por nao serem afetados pela Data FIFA 
df['Nation'].nunique()
df['Nation'].unique()
paises_a_remover = ['eg EGY','nir NIR','cm CMR','gh GHA','sn SEN','ml MLI','ma MAR','tn TUN', 'jm JAM', 'bf BFA','dz ALG','ng NGA','gw GNB','ga GAB','cd COD','za RSA','tg TOG',]
df = df[~df['Nation'].isin(paises_a_remover)]
df['Nation'].unique()
df['Nation'].nunique()
#Filtrando por apenas jogadores defensivos
df['Pos'].unique()
posicoes_a_remover = ['MF','FW,MF','GK','MF,FW' 'FW','MF,FW','FW']
df = df[~df['Pos'].isin(posicoes_a_remover)]
df['Pos'].unique()
#Removendo jogadores com idade >= a 26 anos
df['Age'].unique()
dftratado= df[df['Age'] < 26]
dftratado['Age'].unique()
dftratado
#Organizando o DF para exportar para excel
DF_final = dftratado[['Player', 'Nation', 'Team','Pos', 'Age', 'MP', 'Starts','Ast', 'G+A', 'Min' ]]
DF_final 

#Salvando estes DF em excel
DF_final.to_excel('Potenciais_Laterais.xlsx', index=False)


