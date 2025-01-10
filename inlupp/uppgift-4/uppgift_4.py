# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci(x: int) -> list:
   if x== 0:
       return []
   elif x== 1:
       return [0]
   elif x== 2:
       return [0, 1]
   else:
       resultat = fibonacci(x-1)
   resultat.append(resultat[-1] + resultat[-2])
   return resultat
print(fibonacci(5))
print(fibonacci(0))
print(fibonacci(1))