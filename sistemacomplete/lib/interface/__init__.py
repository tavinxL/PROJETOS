def leiaint(num):
    while True:
        try:
            valor = int(input(num))
        except (ValueError, TypeError):
            print('\033[0;31mERRO, DIGITE UM NÚMERO INTEIRO VALIDO\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuario preferiu não digitar nenhum valor')
            return 0
        else:
            return valor

def linha(tam=42):
    return '='*tam

def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaint('Escolha sua opção: ')
    return opc