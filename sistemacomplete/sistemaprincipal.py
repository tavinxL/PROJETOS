from time import sleep

from sistemacomplete.lib.interface import *
from sistemacomplete.lib.arquivo import *

arq = 'historicocalculadora.txt'

if arqexiste(arq):
    print('Arquivo encontrado com sucesso')
else:
    print('Arquivo não encontrado')
    criarquivo(arq)


while True:
    resposta = menu(['SOMA', 'SUBTRAÇÃO', 'MULTIPLICAÇÃO', 'DIVISÃO', 'SAIR DO SISTEMA'])
    if resposta == 1:
        lerarquivo1(arq)
    elif resposta == 2:
        lerarquivo2(arq)
    elif resposta == 3:
        lerarquivo3(arq)
    elif resposta == 4:
        lerarquivo4(arq)
    elif resposta == 5:
        print('SAINDO DO SISTEMA, ATÉ MAIS...')
        break
    else:
        print('\033[0;31mESCOLHA UMA OPÇÃO VÁLIDA\033[m')





