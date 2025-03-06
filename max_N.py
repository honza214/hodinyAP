while True:   #cyklus který bude probíhat pořád
    cislo = input("zadejte číslo: ")
    if cislo.lstrip("-").isdigit():
        max = int(cislo)
        break
    else:
        print("nezadali jste číslo.")

while input("pro ukončení zadejte písmeno K") != "K":
    cislo = input("zadejte číslo: ")
    if cislo.lstrip("-").isdigit():
        cislo = int(cislo)
        if max < cislo:
            max = cislo
    else:
        print("nezadali jste číslo")

print("největší číslo bylo: " + str(max))
