max = input("zadejte číslo")
for i in range(9):
    cislo = input("zadejte číslo")
    if cislo > max:
        max = cislo
print("největší číslo bylo " + str(max))