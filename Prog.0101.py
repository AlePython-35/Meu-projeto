# Gabarito
GABARITO = ["B", "C", "A", "E", "D"]
RESPOSTAS = ["", "", "", "", ""]
ACERTOS = 0

for X in range(len(GABARITO)):
    print(f"Digite a resposta {X+1}:")
    RESPOSTAS[X] = input()
    if GABARITO[X] == RESPOSTAS[X]:
        print("Acerto, mizerávI!")
        ACERTOS = ACERTOS + 1
    else:
        print("Errô, mané!")

    print("Total de acertos:", ACERTOS)    



    




        
