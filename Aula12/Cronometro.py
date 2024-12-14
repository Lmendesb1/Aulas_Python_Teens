from time import sleep
import sys

contador = int(input("Qual o tempo de lançamento? "))
print("O foguete será lançado em:")

while contador > 0:
    print(f"\r{contador}   ", end="")
    sys.stdout.flush()
    sleep(1)
    contador -= 1
print("\rLançar ...      ")
