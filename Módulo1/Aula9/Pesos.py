# Inicializa as variáveis para armazenar os maiores e menores valores
maior = 0
menor = 0

# Loop para solicitar 5 pesos ao usuário
for n in range(1, 6):
    # Solicita o peso do usuário e converte para inteiro
    num = int(input('Introduza o {}º peso: '.format(n)))

    # No primeiro loop (n == 1), define o primeiro peso como maior e menor
    if n == 1:
        maior = menor = num

    # Verifica se o peso atual é maior que o maior peso registrado
    if num > maior:
        maior = num

    # Verifica se o peso atual é menor que o menor peso registrado
    if num < menor:
        menor = num

# Linha em branco para melhor formatação da saída
print()

# Exibe o maior peso registrado
print("O peso maior é:", maior)

# Exibe o menor peso registrado
print("O peso menor é:", menor)
