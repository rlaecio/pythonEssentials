'''
    Faça um modulo que tenha 3 funções,
    ler_arquivo que retorna o conteudo no formato de lista,
    escrever_arquivo recebe conteudo como parametro no formato de lista
    e escreve no arquivo
    contar_linhas que retorna a quantidade de linhas do arquivo
'''

def ler_arquivo(nome:str) -> list:
    '''Funçao que retorna o conteudo de um arquivo'''
    try: 
        with open(nome, 'r') as arq:
            return arq.readlines()
    except Exception as e:
        return 'Erro: {}'.format(e)

def escrever_arquivo(nome:str, conteudo: list) -> bool:
    ''' Função para escrever o conteudo no arquivo '''
    try:
        with open(nome, 'a') as arq:
            conteudo = [x+'\n' for x in conteudo]
            arq.writelines(conteudo)
            return True
    except Exception:
        return False
    

def contar_linas(nome: str) -> int:
    ''' Função para contar linhas de um arquivo'''
    return len(ler_arquivo(nome))



nomes = ['daniel', 'joão', 'pedro']
#print(escrever_arquivo('texto.txt', nomes))
print(ler_arquivo('texto.txt'))
#print(contar_linas('texto.txt'))
