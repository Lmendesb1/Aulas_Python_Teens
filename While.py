x = int(input('Introduza um número: '))
soma = 0
while x >= 0:
    soma += x
    x = int(input('\nIntroduza um número: '))

print()
print('\nA soma de todos os números que você introduziu é',soma)