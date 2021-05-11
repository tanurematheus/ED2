import pandas as pd     

MAX = 29

def iniciar_dados():
    database = pd.read_excel('base.xlsx')

    df = pd.DataFrame(database)

    df = df[['Local', 'Continente', 'Região', 'Capital', 'População', 'IDH', 'PIB nominal']]

    df = df.loc[df['Continente'] == 'América']
    df = df.loc[df['Região'] != 'Caribe']  
    df.reset_index(inplace = True)
    df.rename(columns = {'index' : 'Código do País', 'Local' : 'Nome do País', 'Região' : 'Subcontinente', 'PIB nominal' : 'PIB'}, inplace = True)
    return df

def iniciar_arquivo():
    with open("test.txt",'w') as f:
        for i in range(MAX):
            f.write( 'Sem dados\r')

def make_str(x, df, next):
    key = df.loc[x, 'Nome do País']
    cdp = df.loc[x, 'Código do País']
    continente = df.loc[x, 'Continente']
    subcontinente = df.loc[x, 'Subcontinente']
    capital = df.loc[x, 'Capital']
    populacao = df.loc[x, 'População']
    idh = df.loc[x, 'IDH']
    pib = df.loc[x, 'PIB']       
    string = (key + ';' + "{}" + ';' + continente + ';' + subcontinente + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + '{}' + ';' + "\n").format(capital, cdp, populacao, idh, pib, next)
    return string

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % MAX

def write_in_file(lines):
    with open("test.txt",'w') as f:
        f.writelines(lines)

def redefine_line(line, next):
    string =  ("{}" + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + '{}' + ';' + "\n").format(line[0], line[1], line[2], line[3], line[4],line[5], line[6], line[7], next)
    return string

def make_line(x, df):
    key = df.loc[x, 'Nome do País']
    key_hash = get_hash(key)

    with open("test.txt",'r') as f:
          
        lines = f.readlines()

        if lines[key_hash] == 'Sem dados\n':
            next = 'nan'
            string = make_str(x, df, next)            
            lines[key_hash] = string   

        else:
            line = lines[key_hash].strip().split(';')
            next = key_hash
            ponteiro = line[-2]
            
            while ponteiro != 'nan':
                key_hash = int(ponteiro)
                line = lines[key_hash].strip().split(';')
                next = key_hash
                ponteiro = line[-2]

            while lines[next] != 'Sem dados\n':
                next = next + 1
                if next == MAX:
                    next = 0

            string =  redefine_line(line, next)
            lines[key_hash] = string

            string = make_str(x, df, 'nan')
            lines[next] = string  
            
        write_in_file(lines)            

def get_line(key):
    key_hash = get_hash(key)
  
    with open("test.txt",'r') as f:
        lines = f.readlines()

        if lines[key_hash] == 'Sem dados\n':
            print('Pais não encontrado\n')
        else:
            line = lines[key_hash].strip().split(';')
            ponteiro = line[-2]
            if line[0] == key:
                print(lines[key_hash])
                print('1 busca\n')            
            else:
                x=2
                while ponteiro != 'nan':
                    key_hash = int(ponteiro)
                    line = lines[key_hash].strip().split(';')
                    ponteiro = line[-2]
                    if line[0] == key:
                        print(lines[key_hash])
                        print(x,'buscas\n')
                        break 
                    else:
                        x = x+1
                if line[0] != key:
                    print('Pais não encontrado\n',x, 'buscas\n')    

def delete_line(key):
    key_hash = get_hash(key)

    with open("test.txt",'r') as f:
        lines = f.readlines()
        
        if lines[key_hash] == 'Sem dados\n':
            print('Pais não encontrado\n')
        else:
            line = lines[key_hash].strip().split(';')
            ponteiro = line[-2]
            if line[0] == key:
                lines[key_hash] = 'Sem dados\n'
                write_in_file(lines)            
            else:                
                while ponteiro != 'nan':
                    anterior = key_hash
                    key_hash = int(ponteiro)
                    line = lines[key_hash].strip().split(';')
                    ponteiro = line[-2]
                    if line[0] == key:
                        line = lines[anterior].strip().split(';')
                        lines[anterior] = redefine_line(line,ponteiro)

                        lines[key_hash] = 'Sem dados\n'
                        write_in_file(lines)   
                        break                     

df = iniciar_dados()
#print(df)

iniciar_arquivo()

#for i in df.index:
#    key = df.loc[i, 'Nome do País']
#    print(get_hash(key))

for i in df.index:
  make_line(i,df)

#get_line('El Salvador')

#delete_line('El Salvador')

#get_line('El Salvador')