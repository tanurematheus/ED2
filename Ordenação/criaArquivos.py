import pandas as pd
 
df = pd.read_csv('Municipios.csv')

df = df.sort_values(by=['IBGE'], ascending=False)

print(df)