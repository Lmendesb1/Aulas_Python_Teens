def conversor(temperatura):
    return (temperatura - 32) * (5 / 9)

# Solicita ao utilizador para inserir a temperatura em Fahrenheit
temperatura = float(input('Introduza a temperatura em Fahrenheit:'))

# Chama a função e exibe o resultado
resultado = conversor(temperatura)
print(f'A temperatura em Celsius é: {resultado:.2f}')
