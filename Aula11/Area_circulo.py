from math import pi

# Solicitar o raio do círculo ao utilizador
raio = float(input("Por favor, insira o raio do círculo: "))

# Calcular a área do círculo
area = pi * (raio ** 2)

# Exibir o resultado
print(f"A área do círculo com raio {raio} é {area:.2f}")