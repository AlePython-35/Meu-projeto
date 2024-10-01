# Conversao de temperaturas...
GRAU = int(input("Digite a temperatura: "))
SISTEMA = input("Celsius / Kelvin / Fahrenheit? ")

if SISTEMA == "Celsius":
    #Criar as 2 formulas para converter em Kelvin e Fahrenheit...
    kelvin = GRAU + 273.15
    fahrenheit = (GRAU * 9/5) - 32
    print("O valor de Celsius: ", GRAU)
    print("A conversão para Kelvin :",  kelvin)
    print("A conversão para Fahrenheit: ",  fahrenheit)
elif SISTEMA == "Kelvin": 
    # Criar as 2 fórmulas para coverter em Celsius e Fahrenheit...
    celsius = GRAU - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("O valor de Kelvin: ", GRAU)
    print("A conversão para Celsius: ",  celsius)
    print("A conversão para Fahrenheit: ",  fahrenheit)
elif SISTEMA == "Fahrenheit":
    # Criar as 2 fóermulas para converter em Celsius e Kelvin...
    celsius = (GRAU - 32) * 5/9
    kelvin = celsius + 273.15
    print("O valor de Fahrenheit: ", GRAU)
    print("A conversão para Celsius: ",  celsius)
    print("A conversão para kelvin: ",  kelvin)
else:
    print("Sistema inexistente")


    

