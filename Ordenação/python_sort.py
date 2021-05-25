import pandas as pd
import contextlib
import time

@contextlib.contextmanager
def timeit():
    start = time.time()
    yield
    end = time.time()
    took = end - start
    print(f"Took {took:.4f}s")

#######################################################
df = pd.read_csv('Ordenação\Municipios_Ordenados.csv')

with timeit():
    df = df.sort_values(by=['IBGE']) 
###########################################################
df = pd.read_csv('Ordenação\Municipios_Desordenados.csv')

with timeit():
    df = df.sort_values(by=['IBGE']) 
##############################################################
df = pd.read_csv('Ordenação\Municipios_Ordem_Inversa.csv')

with timeit():
    df = df.sort_values(by=['IBGE']) 
