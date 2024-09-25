# Demonstração de operadores lógicos em condicionais...
print("O que você vai fazer amanhã de manhã")
print("dormir / estudar / planejar")
MANHA = input()
print("O que você vai fazer amanhã de tarde?")
print("jogar / treinar / trabalhar")
TARDE = input()

if not MANHA or not TARDE:
    print("Você precisar dizer o que vai fazer!")
else:
    if MANHA == "dormir" or TARDE == "jogar":
       print("Você está desperdiçando o seu dia!")
    elif MANHA == "estudar" or TARDE == "treinar":
     print("Que bom! você irá se aperfeiçoar!")
    elif MANHA == "planejar" and TARDE == "trabalhar":
     print("Para trabalhar melhor, devo planejar!")
    else:
      print("Não cobinamos estas ações...")

    print("Tenha um bom dia!")

