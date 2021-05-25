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

def insertion_sort(array):
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            array[p] = array[p - 1]
            p -= 1

        array[p] = current_element

#######################################################
df = pd.read_csv('Ordenação\Municipios_Ordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    insertion_sort(array_index)
###########################################################
df = pd.read_csv('Ordenação\Municipios_Desordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    insertion_sort(array_index)
##############################################################
df = pd.read_csv('Ordenação\Municipios_Ordem_Inversa.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    insertion_sort(array_index)
