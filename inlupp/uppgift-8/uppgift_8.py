# Uppgift 8
# Skapa en funktion count_letters(string) som returnerar en dictionary med varje bokstav som nyckel och antalet förekomster som värde.

def count_letters(x: str) -> dict:
    count_letters = {}
    for i in x:
        if i in count_letters:
            count_letters[i] += 1
        else:
            count_letters[i] = 1
    return count_letters
print(count_letters("hello"))
print(count_letters(""))
print(count_letters("aaa"))