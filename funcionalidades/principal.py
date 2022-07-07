from random import randint


def criar_cpf():
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


if __name__ == "__main__":
    vezes = int(input("digite o numero de CPFs quer deseja gerar: "))
    for c in range(vezes):
        r = criar_cpf()
        print(r)
