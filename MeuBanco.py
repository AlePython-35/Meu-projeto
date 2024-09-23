# Demonstração de uso de diferentes operadores...
print("Qual é o saldo atual da sua conta bancária?")
print("Obs.: utilize ponto para representar os centavos...")
SALDO = float(input())

if SALDO < 0:
    print("Putz! Você está devendo o banco!")
elif SALDO == 0:
    print("impossível! Deve ter ai alguns centavos...")
elif SALDO < 1:
    print("Putz! Só míseros centavinhos na conta?")
elif SALDO <= 9:
    print("Opa! Já da para comprar umas balinhas")
elif SALDO >= 1000000:
    print("Eita, você tem mais de um milhão")

if SALDO != 0:
    print("Ao menos, você está movimentando a conta...")

