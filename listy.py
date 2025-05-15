mylist = ["pomeranč", "jablko", "citron", "kumqat", "meloun", "švestka",]
print(mylist)
print(len(mylist))
print(mylist[2])
#print(mylist[int(input("zadejte pozici"))])
duplist = mylist[2:5]
print(mylist)
print(duplist)

if "jablko" in mylist:
    print("Jablko tam je")

mylist[-2] = "samice hrabáče"
print(mylist)

mylist.append("grep") #přidání podle obsahu
print(mylist)

mylist.insert(1,"ananas") #přidání podle obsahu na první místo listu
print(mylist)

mylist2 = ["paprika","mrkev","okurka"]
mylist.extend(mylist2) #rozšíření podle obsahu
print(mylist)

mylist.remove("ananas") #odstranění podle obsahu
print(mylist)

mylist.pop(2) #odstraní místo které chceme
print(mylist)

print(mylist2)
mylist2.clear()
print(mylist2)

del mylist2
#print(mylist2)

for i in mylist:
    print(i)

for i in range(len(mylist)):
    print(i, mylist[i])

abeceda = ["A", "F", "Z", "C"]
print(abeceda)
abeceda.sort() #vypíše to podle abecedy
print(abeceda)

abeceda.sort(reverse=True) #vypíše podle abecedy ale odzadu
print(abeceda)

mylist.sort
print(mylist)

mylist.sort(key=str.lower) #dá vše malé písmenka
print(mylist)

nums=[100,50,65,82,23]
nums.sort()
print(nums)

nums.reverse() #otočí pořaří v poli
print(nums)

mylist2 = mylist
print(mylist)
print(mylist2)

mylist2[0] = "rajče"
print(mylist)
print(mylist2)

copylist = mylist.copy()
copylist[0] = "pistácie"
print(mylist)
print(copylist)

