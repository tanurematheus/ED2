import pandas as pd
 
df = pd.read_csv('Ordenação\Municipios_Ordenados.csv')

#df = df.sort_values(by=['IBGE'], ascending=False) 

#df.to_csv(r'Ordenação\Municipios_Ordem_Inversa.csv',index = False)

df = df.sort_values(by=['UF'])

df.to_csv(r'Ordenação\Municipios_Desordenados.csv',index = False)  