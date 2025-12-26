try:
    # Lê um número inteiro digitado pelo usuário
    numero = int(input("Digite um número inteiro: "))

    # Verifica se o número é negativo e ímpar
    if numero < 0 and numero % 2 != 0:
        print("O número é negativo e ímpar")

    # Verifica se o número é negativo e par
    elif numero < 0 and numero % 2 == 0:
        print("O número é negativo e par")

    # Verifica se o número é positivo e ímpar
    elif numero > 0 and numero % 2 != 0:
        print("O número é positivo e ímpar")

    # Verifica se o número é positivo e par
    elif numero > 0 and numero % 2 == 0:
        print("O número é positivo e par")

    # Caso o número seja zero
    else:
        print("O número é zero")

except ValueError:
    print("Erro: digite apenas número inteiro!")
