cislo1 = float(input("zadejte první číslo: "))
cislo2 = float(input("zadejte druhé číslo: "))
if cislo2 == 0:
    print("zadejte jiné číslo než 0")
elif cislo2 != 0:
    print(cislo1 - cislo2)
    print(cislo1 + cislo2)
    print(cislo1 / cislo2)
    print(cislo1 * cislo2)