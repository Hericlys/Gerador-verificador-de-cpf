from funcionalidades.úteis import *
from funcionalidades.principal import *

lista_funcao = [criar_cpf, valida_cpf]
lista_op_principal = ['Criar CPF', 'Valida CPF', "Finalizar"]
lista_op_criar_cpf = ['Criar um CPF', 'Criar varios CPFs', 'Voltar']
lista_op_valida_cpf = ['Validar um CPF', 'Validar varios CPFs', 'Voltar']
lista_funcao_menu = [lista_op_criar_cpf, lista_op_valida_cpf]

print("Bem vindo ao sistema de criação e validação de CPF")
while True:
    r_menu_principal = criar_menu('Menu principal! O que deseja fazer?', lista_op_principal)
    limpar()
    if r_menu_principal == 2:
        break
    r_escolha = criar_menu(lista_op_principal[r_menu_principal], lista_funcao_menu[r_menu_principal])
    limpar()
    if r_menu_principal == 0:
        r = 1
        if r_escolha == 2:
            continue
        if r_escolha == 1:
            r = valida_int("quantos CPFs precisa criar? ")
            limpar()
        criar_linha()
        for c in range(r):
            cpf = criar_cpf()
            print(cpf)
        criar_linha()
        print(f"{r} CPFs criado(s)")
        criar_linha()
        cont = input("aperte enter para continuar!")
        limpar()
    if r_menu_principal == 1:
        if r_escolha == 2:
            continue
        if r_escolha == 0:
            cpf = input("digite o CPF: ")
            criar_linha()
            validade = valida_cpf(cpf)
            print(f"{cpf} | ", end="")
            print('Valido' if validade else "Invalido")

        if r_escolha == 1:
            r = input('digite os CPFs e separe eles por ",": ').replace(' ', '').split(",")
            criar_linha()
            for cpf in r:
                validade = valida_cpf(cpf)
                print(f"{cpf} | ", end="")
                print('Valido' if validade else "Invalido")
        cont = input("aperte enter para continuar!")
        limpar()
