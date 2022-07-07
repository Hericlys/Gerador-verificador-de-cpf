def valida_escolha(lista_de_opções=[1,2,3]):
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
        print(f'Você escolheu a opção {escolha_usuario}')
        return escolha_usuario


def criar_linha(tamanho=42, formato='-'):
    print(formato * tamanho)


def criar_titulo(titulo='Titulo Padrão', tamanho=42, formato='-'):
    if tamanho < len(titulo):
        tamanho = len(titulo) + 4

    criar_linha(tamanho, formato)
    print(titulo.center(tamanho))
    criar_linha(tamanho, formato)


def criar_menu(titulo="Titulo Padrão", lista_de_opções=['opc01', 'opc02', 'opc03'], tamanho=42, formato='-'):
    opc_disponiveis = []
    if tamanho < len(titulo):
        tamanho = len(titulo) + 4

    criar_titulo(titulo, tamanho, formato)
    for num, item in enumerate(lista_de_opções):
        print(f"{num} - {item}")
        opc_disponiveis.append(num)
    criar_linha(tamanho, formato)
    resposta = valida_escolha(opc_disponiveis)
    return resposta


if __name__ == "__main__":
    resposta = criar_menu()

