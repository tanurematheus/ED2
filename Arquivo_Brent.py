import pandas as pd     

MAX = 29

dadosIniciais = 'Sem dados\n'

dadosDeletados = 'Ja teve dados\n'

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
    with open("test_brent.txt",'w') as f:
        for element in range(MAX):
            f.write(dadosIniciais)

def make_str(x, df):
    key = df.loc[x, 'Nome do País']
    cdp = df.loc[x, 'Código do País']
    continente = df.loc[x, 'Continente']
    subcontinente = df.loc[x, 'Subcontinente']
    capital = df.loc[x, 'Capital']
    populacao = df.loc[x, 'População']
    idh = df.loc[x, 'IDH']
    pib = df.loc[x, 'PIB']       
    string = (key + ';' + "{}" + ';' + continente + ';' + subcontinente + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + "{}" + ';' + "\n").format(capital, cdp, populacao, idh, pib)
    return string

def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % MAX

def get_deslocamento(key):
    deslocamento = 0
    for char in key:
        deslocamento += ord(char)
    deslocamento = (deslocamento/MAX) % MAX
    return int(deslocamento)

def get_novaPosicao(posicao, deslocamento):
    novaPosicao = posicao + deslocamento
    if novaPosicao >= MAX:
        novaPosicao = novaPosicao - MAX
    return novaPosicao

def write_in_file(lines):
    with open("test_brent.txt",'w') as f:
        f.writelines(lines)

def numeroBuscas(key, lines):
    numeroBuscas = 0
    deslocamento = get_deslocamento(key)
    key_hash = get_hash(key)
    posicao = key_hash   

    while 1:
        if ((lines[posicao] == dadosIniciais) or (lines[posicao] == dadosDeletados)):
            return numeroBuscas
        posicao = get_novaPosicao(posicao, deslocamento)
        numeroBuscas += 1 
      
def make_line(x, df): 
    key = df.loc[x, 'Nome do País']
    key_hash = get_hash(key)
    novaString = make_str(x, df)

    with open("test_brent.txt",'r') as f:
        
        lines = f.readlines()

        if ((lines[key_hash] == dadosIniciais) or (lines[key_hash] == dadosDeletados)):                       
            lines[key_hash] = novaString 

        else:            
            deslocamento = get_deslocamento(key)
            posicao = get_novaPosicao(key_hash, deslocamento)            
            if ((lines[posicao] == dadosIniciais) or (lines[posicao] == dadosDeletados)):                           
                lines[posicao] = novaString 

            else:
                testeNova = numeroBuscas(key, lines)
                line = lines[key_hash].strip().split(';')
                keyVelha = line[0]
                testeVelha = numeroBuscas(keyVelha, lines)

                if testeNova >= testeVelha:                    
                    while 1:
                        if ((lines[posicao] == dadosIniciais) or (lines[posicao] == dadosDeletados)):
                            break
                        posicao = get_novaPosicao(posicao, deslocamento)
                        lineTeste = lines[posicao]
                    lines[posicao] = novaString

                else:
                    deslocamento = get_deslocamento(keyVelha)
                    posicao = get_novaPosicao(key_hash, deslocamento)
                    line = lines[key_hash]
                    lines[key_hash] = novaString                   

                    while 1:
                        if ((lines[posicao] == dadosIniciais) or (lines[posicao] == dadosDeletados)):
                            break
                        posicao = get_novaPosicao(posicao, deslocamento)
                        lineTeste = lines[posicao]
                    lines[posicao] = line

        write_in_file(lines)            

def get_line(key):
    key_hash = get_hash(key)
  
    with open("test_brent.txt",'r') as f:
        lines = f.readlines()

        if lines[key_hash] == dadosIniciais:
            print('Pais não encontrado\n')
        else:
            line = lines[key_hash].strip().split(';')            
            if line[0] == key:
                print(lines[key_hash])
                print('1 busca\n')            
            else:
                x=1
                posicao = key_hash
                deslocamento = get_deslocamento(key)   

                while line[0] != key:                   
                    posicao = get_novaPosicao(posicao, deslocamento)
                    line = lines[posicao].strip().split(';')

                    if lines[posicao] == dadosIniciais:
                        print('Pais não encontrado\n',x, 'buscas\n')     
                        break      
                                   
                    x = x+1


                print(lines[posicao])
                print(x,'buscas\n')        
           
def delete_line(key):
    key_hash = get_hash(key)   

    with open("test_brent.txt",'r') as f:
        lines = f.readlines()
        
        if lines[key_hash] == 'Sem dados\n':
            print('Pais não encontrado\n')

        else:
            line = lines[key_hash].strip().split(';') 

            if line[0] == key:
                lines[key_hash] = dadosDeletados
                write_in_file(lines)  
                         
            else:
                posicao = key_hash
                deslocamento = get_deslocamento(key)   

                while line[0] != key:
                   posicao = get_novaPosicao(posicao, deslocamento)
                   line = lines[posicao].strip().split(';')

                lines[posicao] = dadosDeletados            
                write_in_file(lines)                      

#df = iniciar_dados()
#print(df)

#iniciar_arquivo()

#for i in df.index:
#    key = df.loc[i, 'Nome do País']
#    print(get_hash(key))

#for i in df.index:
#    make_line(i,df)

#get_line('Chile')

#delete_line('El Salvador')

#get_line('El Salvador')