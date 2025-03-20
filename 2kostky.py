import random   #zadání: 2 kostky hází se dokud nejsou stejné a počítají se pokusy
counter = 0
while True:   
    counter += 1
    kostka1 = random.randint(1,6)
    kostka2 = random.randint(1,6)

    print(str(kostka1) + " " +str(kostka2))
    if kostka1 == kostka2:
        break
print("počet hodů nutných k úspěchu byl: " + str(counter))
