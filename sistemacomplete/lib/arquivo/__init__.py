from time import sleep
from sistemacomplete.lib.interface import *

def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve uma falha na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerarquivo1(nome):
    try:
        a = open(nome, 'at')
    except:
        print('ERRO AO ESCREVER O ARQUIVO')
    else:
        num1 = leiaint('Digite um número: ')
        num2 = leiaint('Digite outro número: ')
        print(f'{num1} + {num2} = {num1 + num2}')
        a.write(f'{num1} + {num2} = {num1 + num2}\n')
        historico = input('Deseja ver o histórico da calculadora ? [S/N]').strip().upper()[0]
        if historico in 'S':
            try:
                a = open(nome, 'rt')
            except:
                print('ERRO AO LER O ARQUIVO')
            else:
                cabecalho('HISTORICO CALCULADORA')
                for linha in a:
                    print(linha.strip())
            finally:
                a.close()
        else:
            print('CÁLCULO SALVO NO HISTÓRICO')
    sleep(1)

def lerarquivo2(nome):
    try:
        a = open(nome, 'at')
    except:
        print('ERRO AO ESCREVER O ARQUIVO')
    else:
        num1 = leiaint('Digite um número: ')
        num2 = leiaint('Digite outro número: ')
        print(f'{num1} - {num2} = {num1 - num2}')
        a.write(f'{num1} - {num2} = {num1 - num2}\n')
        historico = input('Deseja ver o histórico da calculadora ? [S/N]').strip().upper()[0]
        if historico in 'S':
            try:
                a = open(nome, 'rt')
            except:
                print('ERRO AO LER O ARQUIVO')
            else:
                cabecalho('HISTORICO CALCULADORA')
                for linha in a:
                    print(linha.strip())
            finally:
                a.close()
        else:
            print('CÁLCULO SALVO NO HISTÓRICO')
    sleep(1)

def lerarquivo3(nome):
    try:
        a = open(nome, 'at')
    except:
        print('ERRO AO ESCREVER O ARQUIVO')
    else:
        num1 = leiaint('Digite um número: ')
        num2 = leiaint('Digite outro número: ')
        print(f'{num1} * {num2} = {num1 * num2}')
        a.write(f'{num1} * {num2} = {num1 * num2}\n')
        historico = input('Deseja ver o histórico da calculadora ? [S/N]').strip().upper()[0]
        if historico in 'S':
            try:
                a = open(nome, 'rt')
            except:
                print('ERRO AO LER O ARQUIVO')
            else:
                cabecalho('HISTORICO CALCULADORA')
                for linha in a:
                    print(linha.strip())
            finally:
                a.close()
        else:
            print('CÁLCULO SALVO NO HISTÓRICO')
    sleep(1)

def lerarquivo4(nome):
    try:
        a = open(nome, 'at')
    except:
        print('ERRO AO ESCREVER O ARQUIVO')
    else:
        num1 = leiaint('Digite um número: ')
        num2 = leiaint('Digite outro número: ')
        print(f'{num1} / {num2} = {num1 / num2}')
        a.write(f'{num1} / {num2} = {num1 / num2}\n')
        historico = input('Deseja ver o histórico da calculadora ? [S/N]').strip().upper()[0]
        if historico in 'S':
            try:
                a = open(nome, 'rt')
            except:
                print('ERRO AO LER O ARQUIVO')
            else:
                cabecalho('HISTORICO CALCULADORA')
                for linha in a:
                    print(linha.strip())
            finally:
                a.close()
        else:
            print('CÁLCULO SALVO NO HISTÓRICO')
        sleep(1)




                    






