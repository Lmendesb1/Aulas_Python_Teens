def acharletra():
   palavra = input("Introduza a palavra desejada:")
   letra = input ("Introduza a letra que você quer procurar na palavra:")

   if letra in palavra:
       print("A letra está na palavra!")
   else:
       print("A letra não está na palavra")


acharletra()