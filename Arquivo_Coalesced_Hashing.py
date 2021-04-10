import pandas as pd     
import Coalesced_Hashing as ch

database = pd.read_excel('base.xlsx')

database = pd.DataFrame(database)

test = ch.HashTable()

test.__setitem__(database.loc[1,'Local'], database.loc[1,'IDH'])

print(test.get_hash(database.loc[1,'Local']))