import pandas as pd
#Abrir Arquivo
file_path = 'C:/Users/caiom/OneDrive/Desktop/Novo Bolsa Familia/202411_NovoBolsaFamilia.csv'
df = pd.read_csv(file_path, sep=';', encoding='latin1')
#Verificar colunas
df.columns
#Retirar colunas nao desejadas e ajustar o nome das colunas
df.drop(columns=['MÊS COMPETÊNCIA'], inplace=True)
df.rename(columns={
    'MÊS REFERÊNCIA':'mes_referencia', 
    'UF':'uf',
    'CÓDIGO SIAFI MUNICÍPIO':'codigo_siafi_municipio',
    'NOME MUNICÍPIO':'nome_municipio',
    'CPF FAVORECIDO':'cpf_favorecido',
    'NIS FAVORECIDO':'nis_favorecido',
    'NOME FAVORECIDO':'nome_favorecido',
     'VALOR PARCELA':'valor_parcela',
    },inplace=True)

#Vericar o formato das colunas e formatar de acordo com a necessidade
df.info()

 #Verificando se as colunas estão no formato int64 antes de adicionar '01' no final para transformar sem erros
if df['mes_referencia'].dtype == 'int64':
    df['mes_referencia'] = df['mes_referencia'].astype(str) + '01'

# Converter as colunas para datetime
df['mes_referencia'] = pd.to_datetime(df['mes_referencia'], format='%Y%m%d', errors='coerce')

# Verificar a conversão
df.info()
print(df.head(2))

#Convertendo colunas para float
df['valor_parcela'] = df['valor_parcela'].str.replace(',', '.').astype(float)