from os import system


def limpar():
    """
    Limpa tudo que estiver no terminal do windows.

    :return: none
    """
    system('cls')


def valida_escolha(lista_de_opções=[1,2,3]):
    """
    Pede ao usuario para digitar um numero de sua escolhar e
    verifica se a entrada do usuario é um numero e se ele contém na lista de opções.

    :param lista_de_opções: list - lista de numeros inteiros
    :return: int - resposta do usuario validada.
    """
    escolha_usuario = None
    while True:
        try:
            escolha_usuario = int(input('Por favor, Digite um numero referente a sua escolha: '))
        except ValueError:
            print('\033[1;31mOpção invalida! Por favor, digite apenas um numero!\033[0;0m')
            continue
        if not escolha_usuario in lista_de_opções:
            print("\033[1;31mOpção invalida! Escolha uma opção dentro das disponiveis...\033[0;0m")
            continue
        criar_linha()
        return int(escolha_usuario)


def valida_int(msg='digite um numero:'):
    """
    pede uma entrada do usuario e verifica se é um numero inteiro.

    :param msg: str - mensagem explicativa para o usuario
    :return: int - resposta do usuario validada.
    """
    while True:
        try:
            r = int(input(msg))
        except ValueError:
            print("digite apenas numeros inteiros!")
            continue
        return r


def criar_linha(tamanho=42, formato='-'):
    """
    Cria uma linha no terminal.

    :param tamanho: int -  quantidade de caracteres para se usar na linha.
    :param formato: str -  caractere(s) a ser usado(s) para a criação da linha.
    :return: none.
    """
    print(formato * tamanho)


def criar_titulo(titulo='Titulo Padrão', tamanho=42, formato='-'):
    """
    cria um titulo entre duas linhas
     # se o tamanho do titulo for maior que o tamanho das linhas ela se ajustará automaticamente.

    :param titulo: str -  titulo
    :param tamanho: int - tamanho das linhas
    :param formato: str - caractere para formar a linha
    :return: none
    """
    if tamanho < len(titulo):
        tamanho = len(titulo) + 4

    criar_linha(tamanho, formato)
    print(titulo.center(tamanho))
    criar_linha(tamanho, formato)


def criar_menu(titulo="Titulo Padrão", lista_de_opções=['opc01', 'opc02', 'opc03'], tamanho=42, formato='-'):
    """
    Cria um menu com um titulo entre duas linhas e logo abaixo lista as opções de escolha para o usuario
    o usuario deve escolher uma opção que será validada.

    :param titulo: str - titulo do menu
    :param lista_de_opções: list:str - lista de opeções para a escolha do usuario
    :param tamanho: int - tamanho das linhas
    :param formato: caractere para formar a linha.
    :return:
    """

    opc_disponiveis = []
    if tamanho < len(titulo):
        tamanho = len(titulo) + 4

    criar_titulo(titulo, tamanho, formato)
    for num, item in enumerate(lista_de_opções):
        print(f"{num} - {item}")
        opc_disponiveis.append(num)
    criar_linha(tamanho, formato)
    resposta = valida_escolha(opc_disponiveis)
    print(f'\033[1;32mVocê escolheu a opção " {resposta} " - {lista_de_opções[int(resposta)]}\033[0;0m')
    return resposta
