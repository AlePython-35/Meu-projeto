# Demonstração de estrutura repetitiva...
CONTADOR = 0; SENHA = ""
while SENHA != "S3nh4":
    print("Digite a senha:")
    SENHA = input()

    if SENHA == "S3nh4":
            print("Senha correta!")
            break
    else:
        print("Senha errada...")

    CONTADOR += 1
    if CONTADOR == 3:
        print("3 tentativas excedidas!")
        break

    
    #Demonstração do uso de estrutura repetitiva...
    NUMERO = 1
    while NUMERO >= 0:
        print("Digite um número negativo para sair:")
        NUMERO = int(input())
        break
        print("Este texto não será ixibido! Mas...")
    else:
        print("O número digitado foi:", NUMERO)    