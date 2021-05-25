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

def selection_sort(array):
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            if array[right] < array[min_index]:
                min_index = right

        array[index], array[min_index] = array[min_index], array[index]
               
#######################################################
df = pd.read_csv('Ordenação\Municipios_Ordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    selection_sort(array_index)
###########################################################
df = pd.read_csv('Ordenação\Municipios_Desordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    selection_sort(array_index)
##############################################################
df = pd.read_csv('Ordenação\Municipios_Ordem_Inversa.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    selection_sort(array_index)
