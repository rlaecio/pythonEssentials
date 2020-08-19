'''
    3. Dado um arquivo .txt qualquer, modifica-lo para numerar as linhas, exemplo:
    1 - texto, texto
    2 - texto
    3 - texto
'''
try:
    with open('texto.txt', 'r') as arq:
        conteudo = [x for x in arq if x != '\n']
        for x in range(len(conteudo)):
            conteudo[x] = '{} - {}'.format(x+1, conteudo[x])
        print(conteudo)
        #cont = 1
        #conteudo = []
        #for linha in arq:
        #    if linha != '\n':
        #        conteudo.append('{0}-  {1}'.format(cont, linha))
        #        cont += 1

    with open('texto.txt', 'w') as arq:
        arq.writelines(conteudo)
except FileNotFoundError:
    print('Arquivo não existe')
except Exception as e:
    print('Erro: {}'.format(e))

              