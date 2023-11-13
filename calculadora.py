from os import system
system("cls")

print(f"{'Olá, seja muito bem vindo(a)!' : ^140}")
print(f"{'Essa é uma calculadora que decidi desenvolver envolvendo as funções básicas, que geralmente existem em uma': ^140}")
print(f"{'calculadora padrão de celular.' : ^140}\n")

input(f"{'Aperte Enter para continuar...' : ^140}")

system("cls")

while True:
    system("cls")
    print("Seleciona a função que deseja fazer:")
    print("[ 1 ] - Somar")
    print("[ 2 ] - Subtração")
    print("[ 3 ] - Divisão")
    print("[ 4 ] - Multiplicação")
    print("[ 5 ] - Potência")
    print("[ 6 ] - Raiz Quadrada\n")
    print("[ 'Sair'] - Encerrar o programa.\n")
    escolha = input()

    system("cls")

    if escolha == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print()
        print(f"O resultado da equação é de: {num1+num2}\n")
        input("Aperte qualquer tecla para continuar...")
            
    elif escolha == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print()
        print(f"O resultado da equação é de: {num1-num2}\n")
        input("Aperte qualquer tecla para continuar...")

    elif escolha == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print()
        print(f"O resultado da equação é de: {num1/num2}\n")
        input("Aperte qualquer tecla para continuar...")
            
    elif escolha == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        print()
        print(f"O resultado da equação é de: {num1*num2}\n")
        input("Aperte qualquer tecla para continuar...")

    elif escolha == "5":
        num1 = float(input("Digite o número da base: "))
        num2 = float(input("Digite o expoente: "))
        print()
        print(f"O resultado da equação é de: {num1**num2}\n")
        input("Aperte qualquer tecla para continuar...")

    elif escolha == "6":
        num1 = float(input("Digite o número desejado: "))
        print()
        print(f"O resultado da equação é de: {num1**0.5}\n")
        input("Aperte qualquer tecla para continuar...")

    elif escolha.lower() == 'sair':
        break

    else:
        print("Opção inválida, por favor, digite o número correto.")
        input("Aperte qualquer tecla para continuar...")





