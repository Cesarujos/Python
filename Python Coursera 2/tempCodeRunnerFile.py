def es_primo(numero):

   resultado = True
   contador = 0
   for divisor in range(2, numero):

       if (numero % divisor) == 0:
           contador +=1
           resultado = False

           break

   return contador 

print(es_primo(13))