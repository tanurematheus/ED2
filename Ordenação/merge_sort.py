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

def merge_sort(array):
    sort_half(array, 0, len(array) - 1)


def sort_half(array, start, end):
    if start >= end:
        return

    middle = (start + end) // 2

    sort_half(array, start, middle)
    sort_half(array, middle + 1, end)

    merge(array, start, end)


def merge(array, start, end):
    array[start: end + 1] = sorted(array[start: end + 1])

#######################################################
df = pd.read_csv('Ordenação\Municipios_Ordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    merge_sort(array_index)
###########################################################
df = pd.read_csv('Ordenação\Municipios_Desordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    merge_sort(array_index)
##############################################################
df = pd.read_csv('Ordenação\Municipios_Ordem_Inversa.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    merge_sort(array_index)
