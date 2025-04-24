import random

win = 0
lose = 0

opakovani = int(input("Zadejte počet opakování, který chcete simulovat: "))
for i in range(opakovani):
    print(i)
    car = random.randint(1,3)
    playerschoice = random.randint(1,3)
    while True:
        montychoice = random.randint(1,3)
        if montychoice != car and montychoice != playerschoice:
            break
    #print(car, playerschoice, montychoice)
    playersOld = playerschoice
    while True:
        playerschoice = random.randint(1,3)
        if playerschoice != montychoice and playerschoice != playersOld:
            break
    if playerschoice == car:
        win += 1
    else:
        lose += 1
print(f"Hráč prohrál v {lose} případech a zvítězil v {win} případech\nto znamená, že zvítězil v {((win/opakovani)*100):.2f} % případů a prohrál v {((lose/opakovani)*100):.2f} % případů")
