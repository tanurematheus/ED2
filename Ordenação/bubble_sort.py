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

def bubble_sort(array):

    for final in range(len(array), 0, -1):
        exchanging = False
        for current in range(0, final - 1):
            if array[current] > array[current + 1]:
                array[current + 1], array[current] = array[current], array[current + 1]
                exchanging = True
        if not exchanging:
            break
               
#######################################################
df = pd.read_csv('Ordenação\Municipios_Ordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    bubble_sort(array_index)
###########################################################
df = pd.read_csv('Ordenação\Municipios_Desordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    bubble_sort(array_index)
##############################################################
df = pd.read_csv('Ordenação\Municipios_Ordem_Inversa.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    bubble_sort(array_index)

