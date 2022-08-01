import requests
import pandas as pd
import numpy as np
from datetime import datetime

# Setando a data do nome do arquivo
DATA_ATUAL = datetime.today().strftime('%d_%m_%Y')

url = 'https://www.fundsexplorer.com.br/ranking'

response = requests.get(url)
if response.status_code == 200:
    df = pd.read_html(response.content, encoding='utf-8')[0]

df.sort_values('Códigodo fundo', inplace=True)
df.describe(include='all')
df['Setor'].unique()
df.columns
df.isna().sum()
categorical_columns = ['Códigodo fundo','Setor']
idx = df[df['Setor'].isna()].index
df.drop(idx, inplace=True)

df[categorical_columns].isna().sum()
df[categorical_columns] = df[categorical_columns].astype('category')
df.info()
df.isna().sum()
col_floats = list(df.iloc[:,2:-1].columns)
## Dados nulos
df[col_floats] = df[col_floats].fillna(value=0)
df[col_floats]
df[col_floats].head()
df[col_floats] = df[col_floats].applymap(lambda x: str(x).replace('R$', '').replace('.','').replace('%','').replace(',','.'))
df[col_floats] = df[col_floats].astype('float')
df.info()
df.head()
df.describe()
## Check infinity values pandas
df[np.isinf(df[col_floats]).any(1)]
idx = df[np.isinf(df[col_floats]).any(1)].index
df.drop(idx, inplace=True)

df['P/VPA'] = df['P/VPA']/1000
df['Liquidez Diária'] = df['Liquidez Diária']/10
df['DividendYield'] = df['DividendYield']/100
df['DY (3M)Acumulado'] = df['DY (3M)Acumulado']/100
df['DY (6M)Acumulado'] = df['DY (6M)Acumulado']/100
df['DY (12M)Acumulado'] = df['DY (12M)Acumulado']/100
df['DY (3M)Média'] = df['DY (3M)Média']/100
df['DY (6M)Média'] = df['DY (6M)Média']/100
df['DY (12M)Média'] = df['DY (12M)Média']/100
df['DY Ano'] = df['DY Ano']/100
df['Variação Preço'] = df['Variação Preço']/100
df['Rentab.Período'] = df['Rentab.Período']/100
df['Rentab.Acumulada'] = df['Rentab.Acumulada']/100
df['DYPatrimonial'] = df['DYPatrimonial']/100
df['VariaçãoPatrimonial'] = df['VariaçãoPatrimonial']/100
df['Rentab. Patr.no Período'] = df['Rentab. Patr.no Período']/100
df['Rentab. Patr.Acumulada'] = df['Rentab. Patr.Acumulada']/100
df['VacânciaFísica'] = df['VacânciaFísica']/100
df['VacânciaFinanceira'] = df['VacânciaFinanceira']/100

df.to_excel(f'FIIcoleta {DATA_ATUAL}.xlsx', index = False)
