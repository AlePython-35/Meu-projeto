# Meu clube de coração...
ESTADO = input(("Rio, São Paulo e Minas Gerais (RJ/SP/MG)? "))

match ESTADO:
    case "RJ":
        CLUBE = print ("Flamengo", "Vasco", "Botafogo", "Fluminense")
        if CLUBE == "Flamengo":
           print ("Parabéns você e melhor do seu estado")
        elif CLUBE == "Vasco" or CLUBE == "Botafogo" or CLUBE == "Fluminense":
            print("Pobres coitados...")
        else:
                print("Opção errada")
    case "SP":
        CLUBE = print ("Palmeiras", "Corinthias", "São Paulo", "Santos")
        if CLUBE == "Palmeiras":
           print ("Parabéns você e melhor do seu estado")
        elif CLUBE == "Corinthias" or CLUBE == "São Paulo" or CLUBE == "Santos":
            print("Pobres coitados...")
        else:
                print("Opção errada")
    case "MG":
        CLUBE = print ("Atletico Mineiro", "Cruzeiro")
        if CLUBE == "Cruzeiro":
           print ("Parabéns você e melhor do seu estado")
        elif CLUBE == "Atletico Mineiro" or CLUBE == "Cruzeiro":
            print("Pobres coitados...")
        else:
                print("Opção errada")


