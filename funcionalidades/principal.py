from random import randint


def valida_cpf(cpf):
    """
    verifica se um cpf é valido.
    O cpf pode conter ou não pontuação e espaços em branco.

    :param cpf: str - cpf
    :return: bool - True se valido e False se invalido
    """
    # removendo a pontuação.
    cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')

    # verificanto tamanho do cpf
    if len(cpf) != 11:
        return False

    # criando novo cpf sem os digitos validadores
    n_cpf = cpf[:-2]

    # gerando numeros finais validos
    sequenciador = 10
    soma = 0
    for c in range(0, 2):
        if c == 1:
            sequenciador = 11
            soma = 0
        for num in n_cpf:
            soma += int(num) * sequenciador
            sequenciador -= 1
        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0
        n_cpf += str(digito)

    # verificando se os digitos do cpf são iguais aos do novo cpf
    if not cpf == n_cpf:
        return False
    return True


def criar_cpf():
    """
    Cria um numero de cpf aleatorio valido

    :return: str - numero de CPF valido
    """
    # Criando numeros aleatorio para o cpf
    cpf = ''
    for c in range(0, 9):
        cpf += str(randint(0, 9))

    # adicionando digitos validadores
    sequenciador = 10
    soma = 0
    for c in range(0, 2):
        if c == 1:
            sequenciador = 11
            soma = 0
        for num in cpf:
            soma += int(num) * sequenciador
            sequenciador -= 1
        digito = 11 - (soma % 11)
        if digito > 9:
            digito = 0
        cpf += str(digito)
    return cpf
