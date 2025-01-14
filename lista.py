reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]

for index, number in enumerate(reallyLongList):
    print(index, number)

# Reverse

my_list = ["äpple", "banan", "körsbär"]

my_list.reverse()
print(my_list)


reallyLongList = ["äpple", "banan", "körsbär", "druva", "apelsin", "päron", "kiwi", "mango", "passionsfrukt", "ananas"]
print("Length: ")
print(len(reallyLongList))
x = 1
for i, fruit in enumerate(reallyLongList):
    if i == (i+1):
        continue
    if (i+1) % 3 == 0:
        print(fruit)
    x += 1


    # Funkar inte
    # x++

    # Unset variable
x = None
print(my_list)
my_list[1] = "blåbär"
print(my_list)
my_list.insert(1, "orange")
print(my_list)
my_list.append("jordgubbe")
my_list.append("blåbär")
my_list.append("blåbär")
my_list.append("blåbär")
my_list.append("Blåbär")
my_list.append("BlåBär")


# Bygger en egen prepend-funktion
def prepend(prependList, value):
    prependList.insert(0, value)
prepend(my_list, "hallon")
print(my_list)
try:
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
    my_list.remove("blåbär")
except ValueError:
    print("Det gick inte att ta bort blåbär")
print(my_list)
my_list.pop()
print(my_list)

mylist= list[1, 2, 3]
for index, number in

