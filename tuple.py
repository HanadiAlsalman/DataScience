# ● Skapa och iterera:
# ○ Skapa en tuppel colors = ("röd", "grön", "blå").
# ○ Iterera genom den med en for-loop och skriv ut varje färg.


colors = ("röd", "grön", "blå")
for color in colors:
    print(color)

numbers = (1, 2, 3, 4, 5)
print(numbers[0:3])

# Dictionary för en produkt:
# Skapa en dictionary för en produkt med namn, pris och lager.
# Uppdatera lager och lägg till en nyckel för kategori.

product = {
    "name": "Bok",
    "price": 100,
    "stock": 5
}
print(product)
product["stock"] = 10
product["category"] = "Böcker"
print(product)
