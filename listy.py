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

mylist.append("grep")
print(mylist)
