from numpy.core.arrayprint import IntegerFormat
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

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)
      sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i

        while position>=gap and nlist[position-gap]>current_value:
            nlist[position]=nlist[position-gap]
            position = position-gap

        nlist[position]=current_value

#######################################################
df = pd.read_csv('Ordenação\Municipios_Ordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    shellSort(array_index)
    
###########################################################
df = pd.read_csv('Ordenação\Municipios_Desordenados.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    shellSort(array_index)
##############################################################
df = pd.read_csv('Ordenação\Municipios_Ordem_Inversa.csv')

array_index = df.loc[:,'IBGE']

array_index = array_index.values

with timeit():
    shellSort(array_index)

    
