i = 1
end = int(input("zadejte číslo jehož faktoriál chcete "))
faktorial = 1
for i in range(end):
    i = i + 1
    faktorial = int(faktorial * i)
    print("faktorial = " + str(faktorial)) 