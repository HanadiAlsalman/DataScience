# Uppgift 4
# Skapa en funktion fibonacci(n) som returnerar en lista med de första n Fibonacci-talen.

def fibonacci_list(n: int) -> list:
    mylist = fibonacci_list(n-1)
    mylist.append(mylist[-1] + mylist[-2])
    return mylist
print(fibonacci_list(1))